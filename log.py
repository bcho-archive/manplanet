#coding: utf-8

import logging

import config


def handler_factory(handlers):
    #: TODO passing *args
    return [handler(**kwargs) for handler, kwargs in handlers]


def logger_factory(name, handlers, level, log_format):
    logger = logging.getLogger(name)

    formatter = logging.Formatter(log_format)
    logger.setLevel(level)

    for handler in handlers:
        handler.setFormatter(formatter)
        handler.setLevel(level)
        logger.addHandler(handler)

    return logger


handlers = [
    (logging.FileHandler, {'filename': config.log_path}),
    (logging.StreamHandler, {}),
]
logger = logger_factory(config.project_codename, handler_factory(handlers),
                        config.log_level, config.log_format)
