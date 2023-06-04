from .base_repository import BaseRepository
from ..configuration.supabase_client import SupabaseClient


class DataSourceRepository(BaseRepository):

    def __init__(self, supabase_client: SupabaseClient, table: str):
        super().__init__(supabase_client, table)
