from flask import Blueprint, request

from flask_template.db import db_session
from flask_template.models import User


user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("", methods=("POST",))
def create_user() -> str:
    data = request.get_json()
    new_user = User(data["name"], data["email"])
    try:
        db_session.add(new_user)
    except Exception:
        print("Failed to create new user")
        db_session.rollback()
    else:
        db_session.commit()
    return "Created user!\n"


@user_bp.route("/<string:email>", methods=("GET",))
def get_user(email: str) -> str:
    query = db_session.query(User).filter(User.email == email).first()
    return str(query)
