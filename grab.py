#coding: utf-8

import os

from config import base_path
from parser import parse
from log import logger
import db


def grab(section):
    section = 'man%s' % (str(section))
    path = os.path.join(base_path, section)

    for fname in os.listdir(path):
        full_path = os.path.join(path, fname)
        if os.path.isfile(full_path):
            result = parse(fname, full_path)
            if result:
                logger.info('Parsing %s(%s)' % result[0:2])
                db.add_page(result[0], result[1], result[3])
    db.commit()


if __name__ == '__main__':
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 'n']:
        logger.info('Parsing %s' % str(i))
        grab(i)
