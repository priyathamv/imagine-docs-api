import logging

from src.configuration.gpt_client import GPTClient
from src.configuration.supabase_client import SupabaseClient
from src.service.base_service import BaseService
from src.service.gpt_service import GPTService

log = logging.getLogger(__name__)

class GPTStreamService(BaseService):

    def __init__(self, gpt_service: GPTService, gpt_client: GPTClient, supabase_client: SupabaseClient) -> None:
        super().__init__()
        self.gpt_service = gpt_service
        self.openai = gpt_client.get_instance()
        self._supabase = supabase_client.get_instance()

    def get_response_stream(self):
        pass

    def create_context(self, query):
        query_embedding = self.gpt_service.create_embeddings(query)

        body = {
            'embedding_input': query_embedding,
            'match_threshold_input': 0.78,
            'min_content_length_input': 50,
            'match_count_input': 10
        }
        # response = self._supabase.functions().invoke('fetch_similar_content', invoke_options={'body': body})
        response = self._supabase.rpc('fetch_similar_content', body)
        log.info('response', response)


