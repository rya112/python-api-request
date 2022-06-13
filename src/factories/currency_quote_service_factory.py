from src.commons.context import Context
from src.services.currency_quote_service import CurrencyQuoteService
from src.services.currency_quote_service_api import CurrencyQuoteServiceApi


class CurrencyQuoteFactory:
    """Class"""

    def __init__(self, context: Context):
        self.context = context

    def getService(self) -> CurrencyQuoteService:
        """ Create currency quote service
        Can return a spefic service

        Returns:
            CurrencyQuoteService: Abstract Class from Currency Quote Service
        """
        return CurrencyQuoteServiceApi(self.context)
