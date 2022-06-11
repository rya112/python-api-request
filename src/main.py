"""Main"""
from src.commons.config import Config
from src.commons.context import Context
from src.services.currency_quote_service import CurrencyQuoteService


def main() -> None:
    """Function"""
    config = Config()
    context = Context(config)
    api_service = CurrencyQuoteService(context)
    currency_code = 'USD-BRL'
    currency = api_service.get_updated_currency(currency_code)
    print(str.format(
        "The last currency uptaded \"{0}\" from \"{1}\" was {2}",
        currency['create_date'],
        currency_code,
        currency['high']))


if __name__ == '__main__':
    main()
