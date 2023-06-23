import logging
import os
from typing import List

from storage3.utils import StorageException

from src.configuration.supabase_client import SupabaseClient
from src.constant import LINK_TO_PAGE_CONTENT_DICT
from src.dto.data_source.data_source_dto import DataSourceDTO
from src.model.document.document_model import DocumentModel
from src.model.data_source.data_source_model import DataSourceModel
from src.model.data_source.source_type import SourceType
from src.model.project.job_status import JobStatus
from src.service.base_service import BaseService
from src.service.document import DocumentService
from src.service.data_source import DataSourceService
from src.service.gpt_service import GPTService
from src.service.scheduler.file_upload_scheduler import FileUploadScheduler
from src.service.web_scraper import WebScraperService
from src.service.file_service import FileService, create_directory
from src.constant import TEMP_FOLDER

log = logging.getLogger(__name__)


class TrainingService(BaseService):

    def __init__(self, file_service: FileService, web_scraper_service: WebScraperService, gpt_service: GPTService,
                 supabase_client: SupabaseClient, data_source_service: DataSourceService,
                 document_service: DocumentService, file_upload_scheduler: FileUploadScheduler):
        self.file_service = file_service
        self.web_scraper_service = web_scraper_service
        self.gpt_service = gpt_service
        self._supabase = supabase_client.get_instance()
        self.data_source_service = data_source_service
        self.document_service = document_service
        self.file_upload_scheduler = file_upload_scheduler
        super().__init__()

    def train(self, project_id: str):
        data_sources: List[DataSourceDTO] = self.data_source_service.find_by_project_id(project_id)

        new_data_sources: List[
            DataSourceDTO] = data_sources  # list(filter(lambda cur_data_source: cur_data_source.job_status == JobStatus.NOT_INITIATED, data_sources))

        status: bool = False
        for data_source in new_data_sources:
            if data_source.source_type == SourceType.WEBSITE:
                status = self.train_website_data(data_source)
            else:
                status = self.train_file_data(data_source)
                if status:
                    self.data_source_service.update_data_source_status(data_source.id, JobStatus.SUCCESSFUL)

        return status

    def train_file_data(self, data_source: DataSourceDTO):
        documents = self.file_service.get_documents_from_file(data_source.source_link)

        document_list: List[DocumentModel] = []
        for document in documents:
            data_source_id = data_source.id
            content = document.page_content
            token_count = self.gpt_service.get_token_count(document.page_content)
            metadata = document.metadata
            embeddings = self.gpt_service.create_embeddings(document.page_content)
            document_list.append(DocumentModel(data_source_id, content, token_count, metadata, embeddings))

        save_status = self.document_service.save_all(document_list)
        return save_status

    def train_files_data(self, files, project_id):
        self.logger.debug('Uploading files...')

        # bucket_response = self.get_or_create_bucket(project_id)

        temp_folder_path = ''.join([os.path.abspath('.'), TEMP_FOLDER])

        # create a directory
        new_dir = ''.join([temp_folder_path, project_id])
        create_directory(new_dir)

        # ds_dto_list = []
        f_to_ds_dict = {}

        for file in files:
            file_name = file.filename
            file_new_path = "".join([new_dir, '/', file_name])
            file.save_project(file_new_path)

            ds = DataSourceModel()
            ds.job_status = JobStatus.IN_PROGRESS
            ds.source_type = SourceType.FILE
            ds.project_id = project_id
            saved_ds = self.data_source_service.save_data_source(ds)
            # ds_dto_list.append(saved_ds)
            f_to_ds_dict[file_name] = saved_ds

        self.file_upload_scheduler.process_files(new_dir, self._supabase, f_to_ds_dict)

        # update data_source record to IN_PROGRESS

        # Step 1: Upload the files to Supabase storage and get the links
        # Step 2: Update the data_source tables in Supabase with the details
        #         source_metadata({id, project_id, type: file, path: location in Supabase}, {type: website, path: link of the site, metadata: {}})
        # Step 3: Extract the text/embedding from the files
        # Step 4: Save it in data_source/content tables in Supabase
        # Step 5: Update the project status to COMPLETED

        return self.file_service.upload_files(files)

    def train_website_data(self, data_source_request: DataSourceDTO):
        self.logger.debug('Training website data...')
        data_source_id = data_source_request.id

        # Step 1: Update Data Source job status to IN_PROGRESS
        self.data_source_service.update_data_source_status(data_source_id, JobStatus.IN_PROGRESS)

        # Step 2: Fetch all the links to content dictionary for the given website
        link_to_page_content_dict = LINK_TO_PAGE_CONTENT_DICT  # self.web_scraper_service.scrape_website(data_source_request)

        # Step 3: Train the model with the content extracted
        document_list: List[DocumentModel] = self.gpt_service.extract_content_list(data_source_id,
                                                                                   link_to_page_content_dict)

        # Step 4: Save contents in the database
        content_save_status = self.document_service.save_all(document_list)

        # Step 5: Update Data Source job status to SUCCESSFUL
        job_status = JobStatus.SUCCESSFUL if content_save_status else JobStatus.FAILED
        data_source_status = self.data_source_service.update_data_source_status(data_source_id, job_status)

        return content_save_status and data_source_status

    def get_or_create_bucket(self, bucket_name):
        try:
            response = self._supabase.storage.get_bucket(bucket_name)
            return response
        except StorageException as e:
            return self._supabase.storage.create_bucket(bucket_name)
