import os
from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.service.document import DocumentService
from src.service.data_source import DataSourceService
from src.service.gpt_service import GPTService
from src.service.gpt_stream_service import GPTStreamService
from src.service.project import ProjectService
from src.service.file_service import FileService
from src.service.file_parser import FileParserService
from src.service.scheduler.file_upload_scheduler import FileUploadScheduler
from src.service.web_scraper import WebScraperService
from src.service.training_service import TrainingService
from src.repository.project_repository import ProjectRepository
from src.repository.data_source_repository import DataSourceRepository
from src.repository.document_repository import DocumentRepository
from src.configuration.supabase_client import SupabaseClient
from src.configuration.gpt_client import GPTClient
from src.constant import SUPABASE_URL, SUPABASE_KEY, OPENAI_API_TYPE, OPENAI_API_KEY, OPENAI_ENDPOINT, \
    OPENAI_API_VERSION


class Container(containers.DeclarativeContainer):
    load_dotenv()

    wiring_config = containers.WiringConfiguration(packages=['.blueprint'])

    # Configurations
    supabase_client: SupabaseClient = providers.Singleton(SupabaseClient,
                                                          os.environ.get(SUPABASE_URL),
                                                          os.environ.get(SUPABASE_KEY))
    gpt_client: GPTClient = providers.Singleton(GPTClient,
                                                os.environ.get(OPENAI_API_TYPE),
                                                os.environ.get(OPENAI_API_KEY),
                                                os.environ.get(OPENAI_ENDPOINT),
                                                os.environ.get(OPENAI_API_VERSION))

    # Repositories
    project_repository = providers.Factory(ProjectRepository, supabase_client, 'project')
    data_source_repository = providers.Factory(DataSourceRepository, supabase_client, 'data_source')
    content_repository = providers.Factory(DocumentRepository, supabase_client, 'document')

    # Services
    file_parser_service = providers.Factory(FileParserService)
    file_service = providers.Factory(FileService, file_parser_service, supabase_client)
    project_service = providers.Factory(ProjectService, project_repository)
    data_source_service = providers.Factory(DataSourceService, data_source_repository, file_service)
    document_service = providers.Factory(DocumentService, content_repository)
    web_scraper_service = providers.Factory(WebScraperService)
    gpt_service = providers.Factory(GPTService, gpt_client)
    gpt_stream_service = providers.Factory(GPTStreamService, gpt_service, supabase_client)
    file_upload_scheduler = providers.Factory(FileUploadScheduler, supabase_client, data_source_service)
    training_service = providers.Factory(TrainingService, file_service, web_scraper_service, gpt_service, supabase_client, data_source_service, document_service, file_upload_scheduler)
