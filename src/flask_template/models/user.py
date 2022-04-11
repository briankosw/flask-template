from typing import Optional
from sqlalchemy import Column, Integer, String
from flask_template.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String)

    def __init__(self, name: Optional[str] = None, email: Optional[str] = None) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"<User {self.name!r} {self.email!r}>"
