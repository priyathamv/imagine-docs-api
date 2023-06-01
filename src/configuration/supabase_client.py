import supabase

# Singleton class to access Supabase instance
from supabase import Client


class SupabaseClient:
    def __init__(self, supabase_url: str, supabase_key: str):
        self._instance = supabase.create_client(supabase_url, supabase_key)

    def get_instance(self) -> Client:
        return self._instance

    # _instance = None
    # _lock = threading.Lock()
    #
    # @staticmethod
    # def get_instance():
    #     if not SupabaseClient._instance:
    #         with SupabaseClient._lock:
    #             if not SupabaseClient._instance:
    #                 load_dotenv()
    #                 SupabaseClient._instance = supabase.create_client(os.environ.get(SUPABASE_URL),
    #                                                                   os.environ.get(SUPABASE_KEY))
    #
    #     return SupabaseClient._instance
