from flask import Blueprint
from sqlalchemy.sql import text

from ..db import db_session


base_bp = Blueprint("base", __name__, "/")


@base_bp.route("/health")
def health():
    try:
        db_session.query(text("1")).from_statement(text("SELECT 1")).all()
        return {"health": "healthy"}, 200
    except:
        return {"health": "unhealthy"}, 500

