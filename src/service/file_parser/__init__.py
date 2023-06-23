import requests
import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import NLTKTextSplitter

from src.service.base_service import BaseService


class FileParserService(BaseService):

    def __init__(self) -> None:
        super().__init__()
        self.text_splitter = NLTKTextSplitter(chunk_size=1000)

    def extract_documents_from_pdf(self, remote_file_location):
        response = requests.get(remote_file_location, stream=True)

        # if response.status_code != 200:
        #     raise EntitySaveException('DataSource saving failed' + str(save_response))
        file_path = '/tmp/' + remote_file_location.split('/')[-1]

        with open(file_path, 'wb') as pdf:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)
            pdf.close()

            loader = PyMuPDFLoader(file_path)
            documents = loader.load()
            os.remove(file_path)

            texts = self.text_splitter.split_documents(documents)
            return texts

    # def extract_text_from_docx(self, filename):
    #     full_text = []
    #     doc = docx.Document(filename)
    #     for cur_para in doc.paragraphs:
    #         full_text.append(cur_para.text)
    #
    #     return ''.join(full_text)
    #
    # def extract_text_from_txt(self, filename):
    #     with open(filename) as file:
    #         lines = file.readlines()
    #         return ''.join(lines)
