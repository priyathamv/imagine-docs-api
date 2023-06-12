from postgrest import APIResponse

from .base_repository import BaseRepository
from ..configuration.supabase_client import SupabaseClient
from ..model.project.job_status import JobStatus


class DataSourceRepository(BaseRepository):

    def __init__(self, supabase_client: SupabaseClient, table: str):
        super().__init__(supabase_client, table)

    def fetch_by_project_id(self, project_id: str) -> APIResponse:
        return self.supabase.table(self.table).select('*').eq('project_id', project_id).execute()

    def update_status(self, id: str, job_status: JobStatus):
        return self.supabase.table(self.table).update({'job_status': job_status.value}).eq('id', id).execute()
