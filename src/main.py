"""Main"""
from src.commons.config import Config
from src.commons.context import Context
from src.factories.currency_quote_service_factory import CurrencyQuoteFactory


def main() -> None:
    """Function"""
    config = Config()
    context = Context(config)
    service_factory = CurrencyQuoteFactory(context)
    service = service_factory.getService()
    currency_code = 'USD-BRL'
    currency = service.get_updated_currency(currency_code)
    print(currency)
    print('>\n' +
          '>\n' +
          '>\n' +
          str.format(
              '> The last currency uptaded \"{0}\" from \"{1}\" was {2}',
              currency.create_date,
              currency_code,
              currency.high) +
          '\n>' +
          '\n>' +
          '\n>')


if __name__ == '__main__':
    main()
