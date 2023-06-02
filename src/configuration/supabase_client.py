import supabase
from supabase import Client


class SupabaseClient:
    def __init__(self, supabase_url: str, supabase_key: str):
        self._instance = supabase.create_client(supabase_url, supabase_key)

    def get_instance(self) -> Client:
        return self._instance
