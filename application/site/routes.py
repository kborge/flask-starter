from flask import Blueprint

site = Blueprint('site', __name__)


@site.route('/')
def index():
    return 'Hello World'