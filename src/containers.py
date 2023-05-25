from dependency_injector import containers, providers

from src.services.gpt_service import GPTService
from src.services.file_parser_service import FileParserService
from src.services.web_scraper.web_scraper_service import WebScraperService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['.blueprints'])

    # Services
    file_parser_service = providers.Factory(FileParserService)

    gpt_service = providers.Factory(GPTService, file_parser = file_parser_service)

    web_scraper_service = providers.Factory(WebScraperService)
