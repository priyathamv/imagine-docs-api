from src.service.base_service import BaseService
from src.service.gpt_service import GPTService
from src.service.web_scraper.web_scraper_service import WebScraperService
from src.models.website_training_request import WebsiteTrainingRequest


class TrainingService(BaseService):

    def __init__(self, gpt_service: GPTService, web_scraper_service: WebScraperService):
        self.gpt_service = gpt_service
        self.web_scraper_service = web_scraper_service
        super().__init__()

    def train_files_data(self, files):
        self.logger.debug('Uploading files...')

        return self.gpt_service.upload_files(files)

    def train_website_data(self, training_request: WebsiteTrainingRequest):
        self.logger.debug('Training website data...')

        application_id = training_request.application_id
        url = training_request.url
        is_auth_enabled = training_request.is_auth_enabled
        is_recursive = training_request.is_recursive
        rules = training_request.rules

        return self.web_scraper_service.scrape_website(url, is_auth_enabled, is_recursive, rules)
