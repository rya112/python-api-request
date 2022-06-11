"""Currency Quote Service"""
import requests
from src.commons.context import Context


class CurrencyQuoteService:
    """Class"""

    def __init__(self, context: Context):
        self.context = context
        self.url = context.config.currency_quote_api_url

    def get_updated_currency(self, code: str):
        """Get the currency conversion between two currencies

        Args:
            code (str): Currency code separated by '-' (ex.: USD-BRL)

        Returns:
            dict: Last currency conversion
        """
        response = requests.get(f'{self.url}/json/last/{code}')
        json = response.json()
        return json[code.replace('-', '')]

    def get_last_days_currency(self, code: str, days: int):
        """Get currency conversion of the last days

        Args:
            code (str): Currency code separated by '-' (ex.: USD-BRL)
            days (int): last days

        Returns:
            dict: Currency conversion of the last days
        """
        response = requests.get(f'{self.url}/json/daily/{code}/{days}')
        return response.json()

    def get_period_currency(self, code: str, start_date: str, end_date: str):
        """Get period currency conversion

        Args:
            code (str): Currency code separated by '-' (ex.: USD-BRL)
            start_date (str): start date period
            end_date (str): end date period

        Returns:
            dict: Period currency conversion
        """
        response = requests.get(
            f'{self.url}/json/daily/{code}?start_date={start_date}\
                &end_date={end_date}')
        return response.json()

    def get_currency_quotes(self, code: str, number: int):
        """Get specific latest currency conversions

        Args:
            code (str): Currency code separated by '-' (ex.: USD-BRL)
            number (int): number of quotes

        Returns:
            dict: Specific latest currency conversions
        """
        response = requests.get(f'{self.url}/{code}/{number}')
        return response.json()

    def get_period_currency_quotes(
            self,
            code: str,
            number: int,
            start_date: str,
            end_date: str):
        """Get specific period latest currency conversions

        Args:
            code (str): Currency code separated by '-' (ex.: USD-BRL)
            number (int): number of quotes
            start_date (str): start date period
            end_date (str): end date period

        Returns:
            dict: Specific period latest currency conversions
        """
        response = requests.get(
            f'{self.url}/{code}/{number}?start_date={start_date}\
                &end_date={end_date}')
        return response.json()
