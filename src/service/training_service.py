import os
from storage3.utils import StorageException

from src.configuration.supabase_client import SupabaseClient
from src.service.base_service import BaseService
from src.service.file_service import FileService
from src.service.gpt.gpt_service import GPTService
from src.service.scheduler.file_upload_scheduler import process_files
from src.service.web_scraper.web_scraper_service import WebScraperService
from src.dto.core.website_training_request import WebsiteTrainingRequest
from src.constant import LINK_TO_CONTENT_DICT, TEMP_FOLDER


class TrainingService(BaseService):

    def __init__(self, file_service: FileService, web_scraper_service: WebScraperService, gpt_service: GPTService,
                 supabase_client: SupabaseClient):
        self.file_service = file_service
        self.web_scraper_service = web_scraper_service
        self.gpt_service = gpt_service
        self._supabase = supabase_client.get_instance()
        super().__init__()

    def train_files_data(self, files, bucket_name):
        self.logger.debug('Uploading files...')

        #bucket_response = self.create_or_get_bucket(bucket_name)

        for file in files:
            file_name = file.filename
            temp_folder_path = ''.join([os.path.abspath('.'), TEMP_FOLDER])

            # create a directory
            new_dir = ''.join([temp_folder_path, bucket_name])
            self.create_directory(new_dir)

            file_new_path = "".join([new_dir, '/', file_name])
            file.save(file_new_path)

            process_files(new_dir, self._supabase)

            # res = self._supabase.storage.from_(bucket_name).upload(file_name, file_new_path)
            # update data_source record to IN_PROGRESS

        # Step 1: Upload the files to Supabase storage and get the links
        # Step 2: Update the data_source tables in Supabase with the details
        #         source_metadata({id, project_id, type: file, path: location in Supabase}, {type: website, path: link of the site, metadata: {}})
        # Step 3: Extract the text/embedding from the files
        # Step 4: Save it in data_source/content tables in Supabase
        # Step 5: Update the project status to COMPLETED

        return self.file_service.upload_files(files)

    def train_website_data(self, training_request: WebsiteTrainingRequest):
        self.logger.debug('Training website data...')

        # application_id = training_request.application_id
        # url = training_request.url
        # is_auth_enabled = training_request.is_auth_enabled
        # is_recursive = training_request.is_recursive
        # rules = training_request.rules

        # link_to_content_dict = self.web_scraper_service.scrape_website(url, is_auth_enabled, is_recursive, rules)

        self.gpt_service.train_model(LINK_TO_CONTENT_DICT)

        return 'link_to_text_dict'

    def create_or_get_bucket(self, bucket_name):

        try:
            response = self._supabase.storage.get_bucket(bucket_name)
            return response
        except StorageException:
            return self._supabase.storage.create_bucket(bucket_name)

    def create_directory(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            print("Folder %s created!" % path)
        else:
            print("Folder %s already exists" % path)
