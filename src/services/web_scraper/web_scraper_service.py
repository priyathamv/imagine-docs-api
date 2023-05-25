import playwright.sync_api
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from pathlib import Path
import json
import re
import tiktoken
from urllib.parse import urlparse, urljoin, urldefrag
import trafilatura
from trafilatura.settings import use_config
from readability import Document
from playwright.sync_api import Playwright, sync_playwright

from src.constants import constant
from src.services.base_service import BaseService


class WebScraperService(BaseService):

    def __init__(self) -> None:
        super().__init__()

    def scrape_website(self, base_url, auth_enabled, include_rules, exclude_rules):
        domain_name = self.extract_domain_name(base_url)

        include_pattern = re.compile(include_rules)
        exclude_pattern = re.compile(exclude_rules)

        # Load the cl100k_base tokenizer which is designed to work with the ada-002 model
        tokenizer = tiktoken.get_encoding("cl100k_base")

        # TODO: We need to filter out all the links that do not fall under this regular expression (https://dx.walmart.com/documents/product/*)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=50)
            # Picking a User-Agent from the available pool
            user_agent = constant.USER_AGENTS[1]  # index % len(constant.USER_AGENTS)]

            # Creating a new browser context and opening a new page
            context = browser.new_context(user_agent=user_agent)
            page = context.new_page()

            links = [base_url]
            visited_links = []
            text_extracted = ''
            for index, link in enumerate(links):
                if link not in visited_links:
                    # TODO: not working (Blocking resources like image, video, css to improve performance)
                    # page.route('**/*', self.handle_route)

                    # Handling authentication in the first request if needed
                    if auth_enabled == True and index == 0:
                        # TODO: handle invalid tags/credentials
                        page.goto(link, wait_until=constant.NETWORK_IDLE)
                        page.fill("#username1", "****")
                        page.fill("#password", "****")
                        page.get_by_title("SIGN IN").click()
                        page.wait_for_load_state(constant.NETWORK_IDLE)
                    else:
                        page.goto(link, wait_until=constant.NETWORK_IDLE)

                    cur_content = page.content()
                    clean_links = self.get_links_from_html(cur_content, domain_name)

                    if include_pattern.search(link) and not exclude_pattern.search(link):
                        text_extracted += '\n' + self.extract_using_trafilatura(cur_content)

                    for cur_link in clean_links:
                        if cur_link not in links:
                            links.append(cur_link)

                    visited_links.append(link)

                    # TODO: pdf file on a html page *(https://drive.google.com/file/d/1U7khRKh12GlaSY73210oQd2170JiXEGY/view)

            return {'links': links}

    # def split_text(self, text, max_tokens, tokenizer):
    #     sentences = text.split('. ')
    #     tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]
    #
    #     for sentence, token in zip(sentences, tokens):


    def handle_route(self, route) -> None:
        # if route.request.resource_type == "document":
        if route.request.resource_type in constant.RESOURCE_EXCLUSIONS:
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
            favor_precision=True,
            no_fallback=False,
            config=config
        )

    def extract_using_beautiful_soup(self, content):
        """
        fallback function, in case Trafilatura fails to extract the text
        """
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script', 'nav', 'footer', 'aside', 'style', 'title'
        ]

        soup = BeautifulSoup(content, 'html.parser')

        # Extracting the text
        text = soup.find_all(text=True)

        # Iterating over all the elements and filtering out blacklisted tags
        clean_text = ''
        for item in text:
            if item.parent.name not in blacklist:
                clean_text += '{} '.format(item)

        # Removing tab separation and stripping the text
        clean_text = clean_text.replace('\t', '')

        return clean_text.strip()

    # def get_main_content(self, s, url):
    #     response = s.get(url, verify=False)
    #
    #     doc = Document(response.content)
    #
    #     return {
    #         'title': doc.title(),
    #         'summary': doc.summary()
    #     }

    # soup = BeautifulSoup(response.text, 'html.parser')
    # elements = soup.find_all()
    # max_density = 0
    # main_content = None
    #
    # for el in elements:
    #     if el.text.strip() == '':
    #         continue
    #     density = len(el.text) / len(el.get_text(strip=True))
    #     if density > max_density:
    #         max_density = density
    #         main_content = el
    #
    # return main_content.get_text()
