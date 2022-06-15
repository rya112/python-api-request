"""Context"""
from logging import Logger

from src.commons.config import Config
from src.commons.log import getLogger


class Context:
    """Class"""

    logger: Logger

    def __init__(self, config: Config):
        self.config = config
        self.logger = getLogger(
            config.log_level,
            str.format('{}-{}', config.source, config.stage))
