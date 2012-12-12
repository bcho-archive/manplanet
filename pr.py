#coding: utf-8

'''
    pr.py
    ~~~~~

    A simple PageRank algorithm implement.
'''

from log import logger


RANK = {}
dampling = 0.85


def init_rank(items):
    logger.info('PR init rank.')
    init_ranking = 1.0 / len(items)

    for item in items:
        RANK[item.id] = [init_ranking, item]


def setup(items):
    logger.info('PR setup.')
    for item in items:
        RANK[item.id] = [item.rating, item]


def finish():
    logger.info('PR finish.')
    for rating, item in RANK.values():
        item.rating = rating


def pr(item, prev):
    rank = 0.0
    for outbound in item.fromme:
        rank += prev[outbound.id][0] / len(outbound.tome)
    rank = (1 - dampling) + rank * dampling
    return rank


def iterate(times=None):
    times = times or 100

    prev = RANK.copy()
    for _ in range(0, times):
        logger.info('PR iterating %d times.' % (_ + 1))
        for id, (rating, item) in prev.items():
            RANK[id][0] = pr(item, prev)
        prev = RANK.copy()
