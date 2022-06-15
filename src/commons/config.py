"""Config"""
from dotenv import dotenv_values  # type: ignore


class Config:
    """Class"""

    def __init__(self):
        envs = dotenv_values()
        self.stage = str(envs['STAGE'])
        self.log_level = str(envs['LOG_LEVEL'])
        self.source = str(envs['SOURCE'])
        self.currency_quote_api_url = str(envs['CURRENCY_QUOTE_API_URL'])
