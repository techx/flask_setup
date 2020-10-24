from sqlalchemy.dialects.postgresql import JSONB
from flask import Flask
from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    active = db.Column(db.Boolean)

    def populate(self, data, **kwargs):
        for key, val in data.items():
            if hasattr(self, key): setattr(self, key, val)

        for key, val in kwargs.items():
            if hasattr(self, key): setattr(self, key, val)

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}