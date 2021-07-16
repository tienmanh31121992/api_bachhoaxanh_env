from flask import Flask
from config import Config
from app.api import bp as api_bp

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
flask_app.register_blueprint(api_bp, url_prefix='/api/v1.0')
from app import routes, models
