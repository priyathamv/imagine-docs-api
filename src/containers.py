import os
from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.service.project_service import ProjectService
from src.service.file_service import FileService
from src.service.file_parser_service import FileParserService
from src.service.web_scraper.web_scraper_service import WebScraperService
from src.service.training_service import TrainingService
from src.repository.project_repository import ProjectRepository
from src.repository.data_source_repository import DataSourceRepository
from src.repository.content_repository import ContentRepository
from src.configuration.supabase_client import SupabaseClient
from src.constant import SUPABASE_URL, SUPABASE_KEY


class Container(containers.DeclarativeContainer):
    load_dotenv()

    wiring_config = containers.WiringConfiguration(packages=['.blueprint'])

    # Configurations
    supabase_client: SupabaseClient = providers.Singleton(SupabaseClient,
                                                          os.environ.get(SUPABASE_URL),
                                                          os.environ.get(SUPABASE_KEY))

    # Repositories
    project_repository = providers.Factory(ProjectRepository, supabase_client, 'project')
    data_source_repository = providers.Factory(DataSourceRepository, supabase_client, 'data_source')
    content_repository = providers.Factory(ContentRepository, supabase_client, 'content')

    # Services
    project_service = providers.Factory(ProjectService, project_repository)
    file_parser_service = providers.Factory(FileParserService)
    file_service = providers.Factory(FileService, file_parser_service)
    web_scraper_service = providers.Factory(WebScraperService)
    training_service = providers.Factory(TrainingService, file_service, web_scraper_service)
