#coding: utf-8

import json

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


pages_and_pages = Table(
        'pages_pages', Base.metadata,
        Column('page1_id', Integer, ForeignKey('pages.id')),
        Column('page2_id', Integer, ForeignKey('pages.id')),
)


class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    section = Column(String(1), nullable=False)
    rating = Column(Float, default=0.0)

    #: self referential many-to-many relationship
    fromme = relationship('Page', secondary=pages_and_pages,
                          primaryjoin=id == pages_and_pages.c.page1_id,
                          secondaryjoin=id == pages_and_pages.c.page2_id,
                          backref="tome")

    def __init__(self, name, section):
        self.name = name
        self.section = section

    def __repr__(self):
        return '<Page %s(%s)>' % (self.name, self.section)

    @property
    def relatives(self):
        return list(set(self.fromme + self.tome))

    @property
    def dict(self):

        def _relatives(rel):
            return [i.id for i in rel]

        return {
            'fromme': _relatives(self.fromme),
            'tome': _relatives(self.tome),
            'name': self.name,
            'id': self.id,
            'rating': self.rating,
        }

    def to_json(self):
        return json.dumps(self.dict)
