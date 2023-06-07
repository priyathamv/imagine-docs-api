from postgrest import APIResponse

from .base_repository import BaseRepository
from ..configuration.supabase_client import SupabaseClient


class ContentRepository(BaseRepository):

    def __init__(self, supabase_client: SupabaseClient, table: str):
        super().__init__(supabase_client, table)

    def fetch_by_data_source_id(self, id: str) -> APIResponse:
        return self.supabase.table(self.table).select('*').eq('data_source_id', id).execute()
