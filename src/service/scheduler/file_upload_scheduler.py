import os
from concurrent.futures import ThreadPoolExecutor

from storage3.utils import StorageException
from supabase import Client

import string
import random

from src.configuration.supabase_client import SupabaseClient
from src.constant import MAX_WORKERS
from src.model.project.job_status import JobStatus
from src.repository.data_source_repository import DataSourceRepository
from src.service.base_service import BaseService
from src.service.data_source import DataSourceService


class FileUploadScheduler(BaseService):

    def __init__(self, supabase_client: SupabaseClient, data_source_service: DataSourceService):
        self.data_source_service = data_source_service
        self._supabase = supabase_client.get_instance()
        super().__init__()

    def process_files(self, folder, supabase_client: Client, f_to_ds_dict):

        files = os.listdir(folder)
        files = [f for f in files if os.path.isfile(folder + '/' + f)]  # Filtering only the files.

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(self.upload_to_supabase, folder, file, supabase_client, f_to_ds_dict) for file in
                       files]
            [future.result() for future in futures]

    def upload_to_supabase(self, folder, files, supabase_client: Client, f_to_ds_dict):
        folder_name = os.path.basename(folder)
        N = 5
        for file_name in files:
            # ds_dto = f_to_ds_dict.get(file_name)
            # ds = self.data_source_service.data_source_repository.fetch_by_id(ds_dto.id)
            try:
                supabase_client.storage.from_(folder_name).upload(file_name,
                                                                  os.path.abspath(''.join([folder, '/', file_name])))

                # ds.job_status = JobStatus.FILE_UPLOAD_SUCCESS
                # self.data_source_service.save(ds)

            except StorageException as e:
                if 'Duplicate' in e.args[0]['error']:
                    random_str = str.join('', random.choices(string.ascii_lowercase + string.digits, k=N))
                    new_file_name = ''.join([random_str, file_name])
                    supabase_client.storage.from_(folder_name).upload(new_file_name,
                                                                      os.path.abspath(
                                                                          ''.join([folder, '/', file_name])))
                    file_name = new_file_name

            finally:
                file_list = supabase_client.storage.from_(folder_name).list()
                # check whether the file is uploaded
                for list_item in file_list:
                    if list_item.get('name').__eq__(file_name):
                        os.remove(''.join([folder, '/', file_name]))
                        pass
                        # change the status of data source to NOT_INITIATED
                        # break
