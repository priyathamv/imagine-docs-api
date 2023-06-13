import os
from typing import List
import tiktoken

from src.configuration.gpt_client import GPTClient
from src.constant import OPENAI_EMBEDDING_ENGINE, OPENAI_EMBEDDING_MODEL, OPENAI_COMPLETION_MODEL, OPENAI_COMPLETION_ENGINE
from src.model.content.content_model import ContentModel
from src.service.base_service import BaseService


class GPTService(BaseService):

    def __init__(self, gpt_client: GPTClient) -> None:
        super().__init__()
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
        self.openai = gpt_client.get_instance()
        self.embedding_model = os.environ.get(OPENAI_EMBEDDING_MODEL) # Probably not needed
        self.embedding_engine = os.environ.get(OPENAI_EMBEDDING_ENGINE)
        self.completion_model = os.environ.get(OPENAI_COMPLETION_MODEL)
        self.completion_engine = os.environ.get(OPENAI_COMPLETION_ENGINE)

    def extract_content_list(self, data_source_id: str, link_to_page_content_dict):
        content_list: List[ContentModel] = []
        for link, page_content in link_to_page_content_dict.items():
            content_to_token_tuples = self.get_content_to_token_tuples(page_content, 500)

            if len(content_to_token_tuples) > 0:
                for (chunk, token_count) in content_to_token_tuples:
                    embedding = self.create_embeddings(chunk)
                    content_list.append(ContentModel(data_source_id, chunk, token_count, embedding))

        return content_list

    # Azure OpenAI does not support multiple inputs, so input can only be a string
    # TODO: The maximum length of input text for our embedding models is 2048 tokens (equivalent to around 2-3 pages of text).
    def create_embeddings(self, input: str):
        response = self.openai.Embedding.create(
            input=input,
            engine=self.embedding_engine
        )
        return response['data'][0]['embedding']

    # Split the text into chunks of a maximum number of tokens
    def get_content_to_token_tuples(self, text: str, max_tokens: int):
        # OpenAI recommends replacing newlines with spaces
        text: str = self.replace_newlines_with_spaces(text)

        # Split the text into sentences
        sentences: List[str] = text.split('. ')

        # Get the number of tokens for each sentence
        # Space is prepended to ensure proper tokenization as some tokenizers treat the first char in a diff way
        tokens: List[int] = [len(self.tokenizer.encode(' ' + sentence)) for sentence in sentences]

        tokens_so_far = 0
        content_to_token_tuples: List[(str, int)] = []
        content_list: List[str] = []

        # Loop through the sentences and tokens joined together in a tuple
        for sentence, token in zip(sentences, tokens):
            if tokens_so_far + token > max_tokens:
                content_to_token_tuples.append(('. '.join(content_list) + '.', tokens_so_far))
                content_list = []
                tokens_so_far = 0

            if token > max_tokens:
                continue

            content_list.append(sentence)
            tokens_so_far += token + 1

        if content_list:
            content_to_token_tuples.append(('. '.join(content_list) + '.', tokens_so_far))

        return content_to_token_tuples

    # TODO: We should not do this for code snippets
    def replace_newlines_with_spaces(self, text: str) -> str:
        return text.replace('\n', ' ') \
            .replace('\\n', ' ') \
            .replace('  ', ' ') \
            .replace('  ', ' ')

    # def normalize_text(self, s):
    #     s = re.sub(r'\s+',  ' ', s).strip()
    #     s = re.sub(r". ,","",s)
    #     # remove all instances of multiple spaces
    #     s = s.replace("..",".")
    #     s = s.replace(". .",".")
    #     s = s.replace("\n", "")
    #     s = s.strip()
    #
    #     return s

    def get_completion(self, prompt):
        return self.openai.Completion.create(model=self.completion_model,
                                             engine=self.completion_engine,
                                             prompt=prompt,
                                             max_tokens=512,
                                             temperature=0,
                                             stream=True)
