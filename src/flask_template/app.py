from typing import Optional

from flask import Flask

from flask_template.api import init_api
# import flask_template.config  # noqa: F401
from flask_template.db import init_db


def create_app(testing: Optional[bool] = False) -> Flask:
    app = Flask(__name__)
    app.config.from_object("flask_template.config.configs")
    init_api(app)
    init_db(app)
    return app
