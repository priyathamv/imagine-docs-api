from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urlparse, urldefrag
import trafilatura
from trafilatura.settings import use_config
from playwright.sync_api import sync_playwright
import tiktoken
import openai
# from openai.embeddings_utils import distances_from_embeddings, cosine_similarity

from src.constant import __init__
from src.service.base_service import BaseService
from src.dto.core.rule import Rule
from src.dto.core.rule_type import RuleType
from src.model.data_source.content import Content


class WebScraperService(BaseService):

    def __init__(self) -> None:
        super().__init__()

    # def scrape_website(self, base_url, auth_enabled, include_rules):
    def scrape_website(self, url, is_auth_enabled, is_recursive, rules):
        domain_name = self.extract_domain_name(url)

        tokenizer = tiktoken.get_encoding("cl100k_base")

        with sync_playwright() as p:
            # Launching a headless browser
            browser = p.chromium.launch(headless=False, slow_mo=50)

            # Picking a User-Agent from the available pool
            user_agent = __init__.USER_AGENTS[1]  # index % len(constant.USER_AGENTS)]

            # Creating a new browser context and opening a new page
            context = browser.new_context(user_agent=user_agent)
            page = context.new_page()

            # links = [url]
            links = [
                # 'https://dx.walmart.com/documents/product/DX.io/How-to-Contribute-to-DX-io-izdpqsncp9',
                # 'https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/overview',
                # 'https://dx.walmart.com/documents/product/Walmart%20Cloud%20Native%20Platform%20(WCNP)/overview',
                # 'https://dx.walmart.com/documents/product/DX.io/overview',
                'https://dx.walmart.com/documents/product/Starter%20Kit%20Contributor/857385746'
            ]
            visited_links = []
            # link_to_text_dict = dict()
            for index, link in enumerate(links):
                if link not in visited_links:
                    # TODO: not working (Blocking resources like image, video, css to improve performance)
                    # page.route('**/*', self.handle_route)

                    # Handling authentication in the first request if needed
                    if is_auth_enabled == True and index == 0:
                        # TODO: handle invalid tags/credentials
                        page.goto(link, wait_until=__init__.NETWORK_IDLE)
                        page.fill("#username1", "****")
                        page.fill("#password", "****")
                        page.get_by_title("SIGN IN").click()
                        page.wait_for_load_state(__init__.NETWORK_IDLE)
                    else:
                        page.goto(link, wait_until=__init__.NETWORK_IDLE)

                    cur_content = page.content()
                    # document: Document = Document(source_link=link, source_type=SourceType.WEBSITE)
                    # clean_links = self.get_links_from_html(cur_content, domain_name)

                    content_to_token_tuples: List[(str, int)] = []

                    if self.is_link_valid_to_extract_text(link, rules):
                        # TODO: Other alternatives to consider
                        '''
                        https://github.com/aaronsw/html2text
                        https://github.com/dragnet-org/dragnet
                        https://github.com/codelucas/newspaper
                        https://github.com/buriy/python-readability
                        '''
                        page_content: str = self.extract_using_trafilatura(cur_content)
                        # link_to_text_dict[link] = page_content
                        content_to_token_tuples += self.get_content_to_token_tuples(page_content, 500, tokenizer)

                        if len(content_to_token_tuples) > 0:
                            # Document(link, SourceType.WEBSITE)
                            for content_to_token_tuple in content_to_token_tuples:
                                content = content_to_token_tuple[0]
                                token_count = content_to_token_tuple[1]
                                embedding = openai.Embedding.create(input=content, engine='text-embedding-ada-002')['data'][0]['embedding']

                                Content(data_source_id=1, content=content, token_count=token_count, embedding=embedding)

                    # for cur_link in clean_links:
                    #     if cur_link not in links:
                    #         links.append(cur_link)

                    visited_links.append(link)

            return {'links': links}

    # Check if the link passed is a valid one to consider for text extraction
    def is_link_valid_to_extract_text(self, link: str, rules: List[Rule]) -> bool:
        for rule in rules:
            exact_match_list: List[str] = list(filter(None, rule.exact_match_list))
            starts_with_list: List[str] = list(filter(None, rule.starts_with_list))
            contains_list: List[str] = list(filter(None, rule.contains_list))

            if exact_match_list and len(exact_match_list) > 0:
                if link in exact_match_list:
                    return False if rule.rule_type == RuleType.EXCLUDE else True
            if starts_with_list and len(starts_with_list) > 0:
                for cur_starts_with in starts_with_list:
                    if link.startswith(cur_starts_with):
                        return False if rule.rule_type == RuleType.EXCLUDE else True
            if contains_list and len(contains_list) > 0:
                for cur_contains_str in contains_list:
                    if cur_contains_str in link:
                        return False if rule.rule_type == RuleType.EXCLUDE else True
        return False

    # Split the text into chunks of a maximum number of tokens
    def get_content_to_token_tuples(self, text: str, max_tokens: int, tokenizer) -> List[str]:
        # OpenAI recommends replacing newlines with spaces
        text: str = self.replace_newlines_with_spaces(text)

        # Split the text into sentences
        sentences: List[str] = text.split('. ')

        # Get the number of tokens for each sentence
        # Space is prepended to ensure proper tokenization as some tokenizers treat the first char in a diff way
        tokens: List[int] = [len(tokenizer.encode(' ' + sentence)) for sentence in sentences]

        tokens_so_far = 0
        chunks: List[(str, int)] = []
        chunk: List[str] = []

        # Loop through the sentences and tokens joined together in a tuple
        for sentence, token in zip(sentences, tokens):
            if tokens_so_far + token > max_tokens:
                chunks.append(('. '.join(chunk) + '.', tokens_so_far))
                chunk = []
                tokens_so_far = 0

            if token > max_tokens:
                continue

            chunk.append(sentence)
            tokens_so_far += token + 1

        if chunk:
            chunks.append(('. '.join(chunk) + '.', tokens_so_far))

        return chunks

    def replace_newlines_with_spaces(self, text: str) -> str:
        return text.replace('\n', ' ') \
            .replace('\\n', ' ') \
            .replace('  ', ' ') \
            .replace('  ', ' ')

    def handle_route(self, route) -> None:
        # if route.request.resource_type == "document":
        if route.request.resource_type in __init__.RESOURCE_EXCLUSIONS:
            print(f'Blocking request to: {route.request.url}')
            route.abort()
        else:
            route.continue_()
        # if route.request.resource_type in constant.RESOURCE_EXCLUSIONS:
        #     print(f'Blocking request to: {route.request.url}')
        #     route.abort()
        # else:
        #     route.continue_()

    def extract_domain_name(self, url) -> str:
        parsed_url = urlparse(url)

        return f"{parsed_url.scheme}://{parsed_url.netloc}"

    def get_links_from_html(self, content, domain_name) -> list[str]:
        soup = BeautifulSoup(content, 'html.parser')

        all_links = [link.get('href') for link in soup.find_all('a')]

        filtered_links = filter(lambda link: self.filter_link(link, domain_name), all_links)

        transformed_links = [self.transform_link(link, domain_name) for link in filtered_links]

        unique_links = list(sorted(set(transformed_links)))

        return unique_links

    def transform_link(self, link, domain_name) -> str:
        # Prepend the domain name url if not present
        link_with_domain = link if link.startswith('http') else domain_name + link

        # Strip off fragments in the URL
        link_with_out_frag, _ = urldefrag(link_with_domain)

        # Strip off the ending `/` if present
        return link_with_out_frag.rstrip('/')

    def filter_link(self, link, domain_name) -> bool:
        if (link is None or
                link == '' or
                link == '/' or
                link.startswith("#") or
                link.startswith("mailto:") or
                link.startswith("tel:")):
            return False
        return link.startswith(domain_name) or link.startswith('/')

    def extract_using_trafilatura(self, content):
        config = use_config()
        config.set("DEFAULT", "EXTRACTION_TIMEOUT", "0")

        return trafilatura.extract(
            content,
            include_links=True,
            include_comments=False,
            include_images=False,
            include_tables=False,
            favor_precision=False,
            favor_recall=True,
            deduplicate=True,
            no_fallback=False,
            config=config
        )
