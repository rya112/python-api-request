"""Mock Config"""
from src.commons.config import Config


class MockConfig(Config):
    """Class"""

    def __init__(self):
        super().__init__()
        self.currency_quote_api_url = 'url'
