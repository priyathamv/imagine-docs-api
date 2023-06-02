from postgrest import APIResponse

from src.configuration.supabase_client import SupabaseClient

from src.service.base_service import BaseService


class BaseRepository(BaseService):

    def __init__(self, supabase_client: SupabaseClient, table):
        super().__init__()
        self.supabase = supabase_client.get_instance()
        self.table = table

    def fetch_by_id(self, id: str) -> APIResponse:
        return self.supabase.table(self.table).select('*').eq('id', id).execute()

    def fetch_all(self) -> APIResponse:
        return self.supabase.table(self.table).select('*').execute()

    def insert(self, data) -> APIResponse:
        return self.supabase.table(self.table).insert(data).execute()

    def update_by_id(self, id, data) -> APIResponse:
        return self.supabase.table(self.table).update(data).eq('id', id).execute()

    def delete_by_id(self, id) -> APIResponse:
        return self.supabase.table(self.table).delete().eq('id', id).execute()

# # Fetching
# data1 = supabase.table('documents').select('*').execute()
# data2 = supabase.table('documents').select('id, name').eq('name', 'hello').execute()
# print(data1)
#
# # Inserting
# supabase.table('documents').insert({'name': 'Priyatham'}).execute()
#
# # Updating name where id is 1
# supabase.table('documents').update({'name': 'updated name'}).eq('id', 1).execute()
#
# # Deleting
# supabase.table('documents').delete().eq('id', 1).execute()
#
#
# # Authentication
# # Sign Up
# user = supabase.auth.sign_up(email='', password='')
#
# # Sign In
# from gotrue.errors import AuthApiError
# session = None
# try:
#     session = supabase.auth.sign_in_with_password(email='email', password='password')
# except AuthApiError:
#     print('Invalid credentials')
#
#
# supabase.auth.sign_out()
