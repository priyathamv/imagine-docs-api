from .base_repository import BaseRepository
from src.configuration.supabase_client import SupabaseClient


class ProjectRepository(BaseRepository):

    def __init__(self, supabase_client: SupabaseClient, table: str):
        super().__init__(supabase_client, table)
