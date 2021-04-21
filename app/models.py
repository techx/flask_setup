from sqlalchemy.dialects.postgresql import JSONB
from flask import Flask
from app import db

class Item(db.Model):
    #table name
    __tablename__ = "items"

    #col names, primary key auto increments
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    active = db.Column(db.Boolean)

    def populate(self, name, active):
        '''
        creates item object with specified fields
        '''
        self.name = name
        self.active = active

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}