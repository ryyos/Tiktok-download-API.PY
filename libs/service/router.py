from flask import Blueprint, request
from libs.service.scraping import Scrapper

blueprint = Blueprint('main', __name__)

@blueprint.route(rule='/', methods=['GET'])
def heloo():
    args = request.args
    scraping = Scrapper()
    
    return scraping.ex(tiktok_url=args.get('url'))

