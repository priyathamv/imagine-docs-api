from flask import request, Blueprint
from flask.json import jsonify
from dependency_injector.wiring import Provide, inject

from src.containers import Container
from src.services.gpt_service import GPTService
from src.services.web_scraper.web_scraper_service import WebScraperService

gpt_bp = Blueprint('gpt_blueprint', __name__)


@gpt_bp.route('/upload-files', methods=['POST'])
@inject
def upload_files(gpt_service: GPTService = Provide[Container.gpt_service]):
    files = request.files.getlist('files')

    output = gpt_service.upload_files(files)

    return jsonify({'result': output})


@gpt_bp.route('/scrape-website', methods=['GET'])
@inject
def scrape_website(web_scraper_service: WebScraperService = Provide[Container.web_scraper_service]):
    url = request.args.get("url")
    output = web_scraper_service.scrape_website(url, True)

    return jsonify({'result': output})
