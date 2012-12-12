#coding: utf-8

'''
    builder.py
    ~~~~~~~~~~

    Build data.
'''

import db


def pick(size, start_id=None):
    if start_id:
        cur = db.get_page_by_id(start_id)
    else:
        cur = db.get_random_page()

    dataset = [cur]
    while len(dataset) < size:
        for i in cur.relatives:
            if i not in dataset:
                dataset.append(i)
        if dataset.index(cur) + 1 >= len(dataset):
            while cur in dataset:
                cur = db.get_random_page()
            dataset.append(cur)
        else:
            cur = dataset[dataset.index(cur) + 1]
    while len(dataset) > size:
        dataset.pop()

    return dataset


def build(size, start_id=None):
    raw = pick(size, start_id)

    dataset = {}
    for i in raw:
        dataset[i.id] = i.dict

    return dataset
