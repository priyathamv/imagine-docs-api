import os.path
import uuid

from src.configuration.supabase_client import SupabaseClient
from src.service.base_service import BaseService
from src.service.file_parser import FileParserService


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("Folder %s created!" % path)
    else:
        print("Folder %s already exists" % path)


class FileService(BaseService):

    def __init__(self, file_parser: FileParserService, supabase_client: SupabaseClient) -> None:
        super().__init__()
        self.file_parser = file_parser
        self._supabase = supabase_client.get_instance()

    def upload_file(self, folder_name, file_obj):
        filename = file_obj.filename
        mimetype = file_obj.mimetype
        file_path_local = '/tmp/' + filename
        file_obj.save(os.path.join(file_path_local))

        unique_filename = str(uuid.uuid4())

        with open(file_path_local, 'rb+') as file:
            res = self._supabase.storage.from_(folder_name).upload(unique_filename, file.read(), {'content-type': mimetype})
            file_url_remote = str(res.url).split('object')[0] + 'object/public' + str(res.url).split('object')[1]

        if os.path.exists(file_path_local):
            os.remove(file_path_local)
        return file_url_remote


    def get_documents_from_file(self, file_location):
        return self.file_parser.extract_documents_from_pdf(file_location)

    def upload_files(self, files):
        self.logger.debug('Uploading files...')

        output = []
        for file in files:
            filename = file.filename
            file_ext = os.path.splitext(filename)[1]
            file.save_project(filename)
            if file_ext == '.pdf':
                text = self.file_parser.extract_documents_from_pdf(filename)
            # elif file_ext == '.docx':
            #     text = self.file_parser.extract_text_from_docx(filename)
            # elif file_ext == '.txt':
            #     text = self.file_parser.extract_text_from_txt(filename)
            else:
                self.logger.debug('File type unknown: %s', file_ext)
                text = ''
            output.append(text)

            if os.path.exists(filename):
                os.remove(filename)
        return output
