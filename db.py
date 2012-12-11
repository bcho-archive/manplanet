#coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import and_

from config import database_url
from models import Base, Page

engine = create_engine(database_url, encoding='utf-8')
session = scoped_session(sessionmaker(bind=engine, autoflush=True,
                                      expire_on_commit=False))


def create_all():
    Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)


def commit():
    session.commit()


def _get_all(model, cond):
    ret = session.query(model).filter(cond)
    return ret.all() if ret.count() else None


def _get_one(model, cond):
    ret = _get_all(model, cond)
    return ret[0] if ret else None


def get_page(name, section):
    return _get_one(Page, and_(Page.name == name, Page.section == section))


def add_page(name, section, relatives=None):
    page, found = get_page(name, section), True
    if not page:
        page = Page(name, section)
        found = False

    relatives = relatives or []
    for n, s in relatives:
        page.fromme.append(add_page(n, s))

    if not found:
        session.add(page)

    return page