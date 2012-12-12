#coding: utf-8

from flask import Flask, request, jsonify

import builder

#: init app
app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/pages.json')
def get():
    limit = int(request.args.get('limit', 20))
    start_id = request.args.get('start_id', None)
    start_id = int(start_id) if start_id else None
    return jsonify(builder.build(limit, start_id))
