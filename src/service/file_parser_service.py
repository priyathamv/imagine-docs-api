from src.service.base_service import BaseService
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import docx


class FileParserService(BaseService):

    def __init__(self) -> None:
        super().__init__()

    def extract_text_from_pdf(self, filename):
        full_text = []
        for page_layout in extract_pages(filename):
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    full_text.append(element.get_text())

        return ''.join(full_text)

    def extract_text_from_docx(self, filename):
        full_text = []
        doc = docx.Document(filename)
        for cur_para in doc.paragraphs:
            full_text.append(cur_para.text)

        return ''.join(full_text)

    def extract_text_from_txt(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            return ''.join(lines)
