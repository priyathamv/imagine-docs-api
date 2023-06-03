from postgrest import APIResponse
from src.configuration.supabase_client import SupabaseClient

from src.service.base_service import BaseService
from src.dto.project.create_project_dto import CreateProjectDTO
from src.dto.project.update_project_dto import UpdateProjectDTO


class BaseRepository(BaseService):

    def __init__(self, supabase_client: SupabaseClient, table):
        super().__init__()
        self.supabase = supabase_client.get_instance()
        self.table = table

    def fetch_by_id(self, id: str) -> APIResponse:
        return self.supabase.table(self.table).select('*').eq('id', id).execute()

    def fetch_all(self) -> APIResponse:
        return self.supabase.table(self.table).select('*').execute()

    def insert(self, data: CreateProjectDTO) -> APIResponse:
        data_str = CreateProjectDTO.to_dict(data)
        return self.supabase.table(self.table).insert(data_str).execute()

    def update_by_id(self, id, data: UpdateProjectDTO) -> APIResponse:
        data_str = UpdateProjectDTO.to_dict(data)
        return self.supabase.table(self.table).update(data_str).eq('id', id).execute()

    def delete_by_id(self, id) -> APIResponse:
        return self.supabase.table(self.table).delete().eq('id', id).execute()
