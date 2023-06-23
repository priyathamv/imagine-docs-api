import logging
from typing import List

from langchain import PromptTemplate, OpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore

from src.configuration.supabase_client import SupabaseClient
from src.dto.document.similar_content import SimilarContent
from src.service.base_service import BaseService
from src.service.gpt_service import GPTService

log = logging.getLogger(__name__)


class GPTStreamService(BaseService):

    def __init__(self, gpt_service: GPTService, supabase_client: SupabaseClient) -> None:
        super().__init__()
        self.gpt_service = gpt_service
        self._supabase = supabase_client.get_instance()

    def create_context(self, project_id, query):
        query_embedding = self.gpt_service.create_embeddings(query)

        body = {
            'project_id_input': project_id,
            'embedding_input': query_embedding,
            'match_count_input': 10,
            'match_threshold_input': 0.7
        }
        # TODO: add similarity > 0.8 for better results
        response = self._supabase.rpc('fetch_similar_documents', body).execute()
        similar_content_list: List[SimilarContent] = SimilarContent.schema().load(response.data, many=True)

        tokens = 0
        context = ''
        content_list = []
        for similar_content in similar_content_list:
            if tokens + similar_content.token_count > 1500:
                break
            tokens += similar_content.token_count
            context += similar_content.content.strip() + '\n---\n'

            # if similar_content.similarity >= 0.5:
            content_list.append(similar_content.content)

        prompt_template = f"""Use the following pieces of context to answer the question at the end. If you don't know the answer, just say "Sorry, I could not find anything relevant", don't try to make up an answer.

        {context}
        
        Question: {query}
        Answer:"""

        gpt_response = self.gpt_service.get_completion(prompt_template)

        return gpt_response
