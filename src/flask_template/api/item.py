from flask import Blueprint, request

from flask_template.db import db_session
from flask_template.models import Item


item_bp = Blueprint("item", __name__, url_prefix="/item")


@item_bp.route("", methods=("POST",))
def create_item() -> str:
    data = request.get_json()
    new_item = Item(data["sku"], data["name"], data["item_type"])
    try:
        db_session.add(new_item)
    except Exception:
        print("Failed to create new item")
        db_session.rollback()
    else:
        db_session.commit()
    return "Created item!\n"


@item_bp.route("/<string:sku>", methods=("GET",))
def get_item(sku: str) -> str:
    query = db_session.query(Item).filter(Item.sku == sku).first()
    return str(query)
