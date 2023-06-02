import os
from dependency_injector import containers, providers
from dotenv import load_dotenv
from supabase import Client

from src.service.project_service import ProjectService
from src.service.gpt_service import GPTService
from src.service.file_parser_service import FileParserService
from src.service.web_scraper.web_scraper_service import WebScraperService
from src.service.training_service import TrainingService
from src.repository.project_repository import ProjectRepository
from src.repository.document_repository import DocumentRepository
from src.repository.section_repository import SectionRepository
from src.configuration.supabase_client import SupabaseClient
from src.constants import SUPABASE_URL, SUPABASE_KEY


class Container(containers.DeclarativeContainer):
    load_dotenv()

    wiring_config = containers.WiringConfiguration(packages=['.blueprints'])

    # Configurations
    supabase_client: SupabaseClient = providers.Singleton(SupabaseClient,
                                                          os.environ.get(SUPABASE_URL),
                                                          os.environ.get(SUPABASE_KEY))

    # Repositories
    project_repository = providers.Factory(ProjectRepository, supabase_client, 'project')
    document_repository = providers.Factory(DocumentRepository, supabase_client, 'document')
    section_repository = providers.Factory(SectionRepository, supabase_client, 'section')

    # Services
    project_service = providers.Factory(ProjectService, project_repository)
    file_parser_service = providers.Factory(FileParserService)
    gpt_service = providers.Factory(GPTService, file_parser_service)
    web_scraper_service = providers.Factory(WebScraperService)
    training_service = providers.Factory(TrainingService, gpt_service, web_scraper_service)
