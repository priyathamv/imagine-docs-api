from src.service.base_service import BaseService
from src.service.file_service import FileService
from src.service.web_scraper.web_scraper_service import WebScraperService
from src.dto.core.website_training_request import WebsiteTrainingRequest


class TrainingService(BaseService):

    def __init__(self, file_service: FileService, web_scraper_service: WebScraperService):
        self.file_service = file_service
        self.web_scraper_service = web_scraper_service
        super().__init__()

    def train_files_data(self, files):
        self.logger.debug('Uploading files...')
        # Step 1: Upload the files to Supabase storage and get the links
        # Step 2: Update the project and source_metadata tables in Supabase with the details
        #         project(projectId, name, owner_id, status=IN_PROGRESS)
        #         source_metadata({id, project_id, type: file, path: location in Supabase}, {type: website, path: link of the site, metadata: {}})
        # Step 3: Extract the text/embedding from the files
        # Step 4: Save it in data_source/content tables in Supabase
        # Step 5: Update the project status to COMPLETED

        return self.file_service.upload_files(files)

    def train_website_data(self, training_request: WebsiteTrainingRequest):
        self.logger.debug('Training website data...')

        application_id = training_request.application_id
        url = training_request.url
        is_auth_enabled = training_request.is_auth_enabled
        is_recursive = training_request.is_recursive
        rules = training_request.rules

        return self.web_scraper_service.scrape_website(url, is_auth_enabled, is_recursive, rules)
