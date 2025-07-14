from flask import Flask
from app.config import Config   # type: ignore
from app.api import users, errors, tokens # type: ignore
from flask import Blueprint

bp = Blueprint('api', __name__)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.api import bp as api_bp # type: ignore
    app.register_blueprint(api_bp, url_prefix='/api')
  

    return app


    