from flask import Flask
from application.api.routes import api
from application.site.routes import site

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(site)