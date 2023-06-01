from supabase import Client

from .base_repository import BaseRepository
from ..configuration.supabase_client import SupabaseClient


class ProjectRepository(BaseRepository):

    def __init__(self, supabase_client: SupabaseClient, table: str):
        super().__init__(supabase_client.get_instance(), table)
