from config import Config
from context import Context
from services.currencyQuoteService import CurrencyQuoteService


def main() -> None:
    config = Config()
    context = Context(config)
    api_service = CurrencyQuoteService(context)
    json_response = api_service.get_updated_currency('USD-BRL')
    print(json_response)


if __name__ == '__main__':
    main()
