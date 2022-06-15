"""Logger"""
import logging
import logging.config


def getLogger(level: str, source: str):
    logging.config.fileConfig(
        'logging.config',
        defaults=None,
        disable_existing_loggers=True,
        encoding=None)
    logger = logging.getLogger(source)
    logger.setLevel(level)
    return logger
