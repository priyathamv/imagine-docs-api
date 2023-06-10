import os.path

from src.service.base_service import BaseService
from src.service.file_parser import FileParserService


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("Folder %s created!" % path)
    else:
        print("Folder %s already exists" % path)


class FileService(BaseService):

    def __init__(self, file_parser: FileParserService) -> None:
        self.file_parser = file_parser
        super().__init__()

    def upload_file(self, file):
        pass

    def upload_files(self, files):
        self.logger.debug('Uploading files...')

        output = []
        for file in files:
            filename = file.filename
            file_ext = os.path.splitext(filename)[1]
            file.save_project(filename)
            if file_ext == '.pdf':
                text = self.file_parser.extract_text_from_pdf(filename)
            elif file_ext == '.docx':
                text = self.file_parser.extract_text_from_docx(filename)
            elif file_ext == '.txt':
                text = self.file_parser.extract_text_from_txt(filename)
            else:
                self.logger.debug('File type unknown: %s', file_ext)
                text = ''
            output.append(text)

            if os.path.exists(filename):
                os.remove(filename)
        return output
