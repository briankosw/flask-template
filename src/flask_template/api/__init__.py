from flask import Flask

from .base import base_bp
from .item import item_bp
from .user import user_bp


def init_api(app: Flask) -> None:
    app.register_blueprint(base_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(user_bp)
