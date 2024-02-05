from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List

db = SQLAlchemy()

michi_tag_m2m = db.Table(
    "michi_tags",
    Column("michi_id", ForeignKey("michis.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

doggo_tag_m2m = db.Table(
    "doggo_tag",
    Column("doggo_id", ForeignKey("doggos.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class Michis(db.Model):
    __tablename__ = "michis"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, )
    gif_url: Mapped[str] = mapped_column(String, )
    tags: Mapped[List["Tags"]] = relationship(secondary="michi_tags")

    def __init__(self, id, name, description, gif_url, tags):
        self.id = id
        self.name = name
        self.description = description
        self.gif_url = gif_url
        self.tags = tags or []
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "gif_url": self.gif_url,
            "tags": [tag.serialize() for tag in self.tags],
        }


class Doggos(db.Model):
    __tablename__ = "doggos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, )
    gif_url: Mapped[str] = mapped_column(String, )
    tags: Mapped[List["Tags"]] = relationship(secondary="doggo_tag")

    def __init__(self, id, name, description, gif_url, tags):
        self.id = id
        self.name = name
        self.description = description
        self.gif_url = gif_url
        self.tags = tags or []

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "gif_url": self.gif_url,
            "tags": [tag.serialize() for tag in self.tags],
        }

    
class Tags(db.Model):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


