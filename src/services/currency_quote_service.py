from abc import ABC, abstractmethod

from src.models.currency_quote_model import CurrencyQuoteModel


class CurrencyQuoteService(ABC):

    @abstractmethod
    def get_updated_currency(self, code: str) -> CurrencyQuoteModel:
        pass

    @abstractmethod
    def get_last_days_currency(self, code: str, days: int):
        pass

    @abstractmethod
    def get_period_currency(self, code: str, start_date: str, end_date: str):
        pass

    @abstractmethod
    def get_currency_quotes(self, code: str, number: int):
        pass

    @abstractmethod
    def get_period_currency_quotes(
            self,
            code: str,
            number: int,
            start_date: str,
            end_date: str):
        pass
