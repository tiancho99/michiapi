from flask import Flask
from flask_bootstrap import Bootstrap5

from .api import michi_api, limiter
from .db_manager.models import db
from .config import Config

def create_app():
    app = Flask(__name__, template_folder="app/templates", static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(michi_api, url_prefix="/api")

    limiter.init_app(app)
    bootstrap = Bootstrap5(app)

    return app
