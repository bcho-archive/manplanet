#coding: utf-8

from random import randint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import and_

from config import database_url, pr_iterate_times
from models import Base, Page
import pr

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


def pages_count():
    return session.query(Page).count()


def get_page_by_id(id):
    return _get_one(Page, (Page.id == id))


def get_page(name, section):
    return _get_one(Page, and_(Page.name == name, Page.section == section))


def get_random_page():
    return get_page_by_id(randint(1, pages_count()))


def add_page(name, section, relatives=None):
    #: replace the empty section with 3
    section = section or '3'
    page = get_page(name, section)
    if not page:
        page = Page(name, section)
        found = False
    else:
        found = True

    relatives = relatives or []
    for n, s in relatives:
        page.fromme.append(add_page(n, s))

    if not found:
        session.add(page)

    return page


def init_rating():
    pages = session.query(Page).all()
    pr.init_rank(pages)
    pr.finish()
    session.commit()


def rating():
    pages = session.query(Page).all()
    pr.setup(pages)
    pr.iterate(pr_iterate_times)
    pr.finish()
    session.commit()
