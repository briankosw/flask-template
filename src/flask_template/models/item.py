from sqlalchemy import Column, String
from flask_template.db import Base


class Item(Base):
    __tablename__ = "items"
    sku = Column(String, primary_key=True)
    name = Column(String)
    item_type = Column(String)

    def __init__(self, sku: str, name: str, item_type: str) -> None:
        self.sku = sku
        self.name = name
        self.item_type = item_type

    def __repr__(self) -> str:
        return f"<User {self.sku!r} {self.name!r}>"
