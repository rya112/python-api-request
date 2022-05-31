import requests
from context import Context


class CurrencyQuoteService:
    """API Client"""

    def __init__(self, context: Context):
        self.context = context
        self.url = context.config.currency_quote_api_url

    def get_updated_currency(self, code: str):
        '''
        Returns the currency conversion between two currencies
                Parameters:
                        code (string): Currency code separated by '-' (ex.: USD-BRL)
                Returns:
                        response (dict): Data the last conversion
        '''
        response = requests.get(f'{self.url}/json/last/{code}')
        return response.json()

    def get_last_days_currency(self, code: str, days: int):
        response = requests.get(f'{self.url}/json/daily/{code}/{days}')
        return response.json()

    def get_period_currency(self, code: str, start_date: str, end_date: str):
        response = requests.get(
            f'{self.url}/json/daily/{code}?start_date={start_date}&end_date={end_date}')
        return response.json()

    def get_currency_quotes(self, code: str, number: int):
        response = requests.get(f'{self.url}/{code}/{number}')
        return response.json()

    def get_period_currency_quotes(self, code: str, number: int, start_date: str, end_date: str):
        response = requests.get(
            f'{self.url}/{code}/{number}?start_date={start_date}&end_date={end_date}')
        return response.json()
