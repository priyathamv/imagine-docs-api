import os
from typing import List
import tiktoken
import openai
from openai.embeddings_utils import distances_from_embeddings, cosine_similarity

from src.constant import OPENAI_DEPLOYMENT_NAME, OPENAI_MODEL
from src.service.base_service import BaseService


class GPTService(BaseService):

    def __init__(self) -> None:
        super().__init__()
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def train_model(self, link_to_content_dict):
        content_to_token_dict = {}
        for link, content in link_to_content_dict:
            content_to_token_dict[content] = self.get_content_to_token_tuples(content, 500, self.tokenizer)

            if len(content_to_token_dict) > 0:
                # DataSource(link, SourceType.WEBSITE)
                for content, token_count in content_to_token_dict:
                    embedding = openai.Embedding.create(input=content, engine='text-embedding-ada-002')['data'][0][
                        'embedding']

                    # Content(data_source_id=1, content=content, token_count=token_count, embedding=embedding)

    # Azure OpenAI does not support multiple inputs, so input can only be a string
    # TODO: The maximum length of input text for our embedding models is 2048 tokens (equivalent to around 2-3 pages of text).
    def create_embeddings(self, input: str):
        deployment_id = os.environ.get(OPENAI_DEPLOYMENT_NAME)
        openai_model = os.environ.get(OPENAI_MODEL)

        response = openai.Embedding.create(
            input=input,
            deployment_id=deployment_id,
            engine=openai_model
        )
        return response['data'][0]['embedding']

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

    # TODO: We should not do this for code snippets
    def replace_newlines_with_spaces(self, text: str) -> str:
        return text.replace('\n', ' ') \
            .replace('\\n', ' ') \
            .replace('  ', ' ') \
            .replace('  ', ' ')
