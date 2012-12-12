#coding: utf-8

import sys

import db
import server


def _main():
    command = 'server'
    if len(sys.argv) > 1:
        command = sys.argv[1]

    if command == 'server':
        server.app.run()
    elif command == 'rating':
        if sys.argv[2] == 'init':
            db.init_rating()
        elif sys.argv[2] == 'update':
            db.rating()
    elif command == 'db':
        if sys.argv[2] == 'drop':
            db.drop_all()
        elif sys.argv[2] == 'create':
            db.create_all()


if __name__ == '__main__':
    _main()
