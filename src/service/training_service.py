import logging
from typing import List

from src.dto.data_source.data_source_dto import DataSourceDTO
from src.model.content.content_model import ContentModel
from src.model.data_source.data_source_model import DataSourceModel
from src.model.project.job_status import JobStatus
from src.service.base_service import BaseService
from src.service.content import ContentService
from src.service.data_source import DataSourceService
from src.service.file_service import FileService
from src.service.gpt_service import GPTService
from src.service.web_scraper import WebScraperService
from src.constant import LINK_TO_PAGE_CONTENT_DICT

log = logging.getLogger(__name__)


class TrainingService(BaseService):

    def __init__(self, file_service: FileService, web_scraper_service: WebScraperService, gpt_service: GPTService,
                 data_source_service: DataSourceService, content_service: ContentService):
        self.file_service = file_service
        self.web_scraper_service = web_scraper_service
        self.gpt_service = gpt_service
        self.data_source_service = data_source_service
        self.content_service = content_service
        super().__init__()

    def train_files_data(self, files):
        self.logger.debug('Uploading files...')
        # Step 1: Upload the files to Supabase storage and get the links
        # Step 2: Update the data_source tables in Supabase with the details
        #         source_metadata({id, project_id, type: file, path: location in Supabase}, {type: website, path: link of the site, metadata: {}})
        # Step 3: Extract the text/embedding from the files
        # Step 4: Save it in data_source/content tables in Supabase
        # Step 5: Update the project status to COMPLETED

        return self.file_service.upload_files(files)

    def train_website_data(self, data_source_request: DataSourceModel):
        self.logger.debug('Training website data...')

        # Step 1: Save Data Source information in the database
        data_source_request.set_job_status(JobStatus.IN_PROGRESS)
        # data_source_saved = self.data_source_service.save(data_source_request)

        # Step 2: Fetch all the links to content dictionary for the given website
        link_to_page_content_dict = LINK_TO_PAGE_CONTENT_DICT  # self.web_scraper_service.scrape_website(url, is_auth_enabled, is_recursive, rules)

        # Step 3: Train the model with the content extracted
        content_list: List[ContentModel] = self.gpt_service.extract_content_list('dae2f265-9ed6-42f1-a72d-1b9ee4fc816b',
                                                                                 link_to_page_content_dict)

        # Step 4: Save contents in the database
        save_status = self.content_service.save_all(content_list)
        log.info('Saved all the contents with status: %s', save_status)

        return save_status
