"""Test Currency Quote Service"""
import sys
import unittest
from test.mocks.context_mock import MockContext
from unittest import mock
from unittest.mock import Mock

from src.factories.currency_quote_service_factory import CurrencyQuoteFactory

sys.path.append('..')


class CurrencyQuoteServiceTest(unittest.TestCase):
    """Class"""

    def setUp(self):
        self.context = MockContext()

    def test_get_updated_currency(self):
        """Should return last currency conversion from USD-BRL
        """

        currency_code = 'USD-BRL'

        with mock.patch('requests.get') as requests_get_mock:
            mock_data = Mock(return_value={
                'USDBRL': {
                    'code': 'USD',
                    'codein': 'BRL',
                    'name': 'Dólar Americano/Real Brasileiro',
                    'high': '5.0000',
                    'low': '4.9875',
                    'varBid': '0.1231',
                    'pctChange': '2.47',
                    'bid': '5.1091',
                    'ask': '5.1102',
                    'timestamp': '1655146763',
                    'create_date': '2022-01-01 00:00:00'}})
            requests_get_mock.return_value.json = mock_data
            service_factory = CurrencyQuoteFactory(self.context)
            service = service_factory.getService()
            currency = service.get_updated_currency(
                currency_code)
            self.assertEqual(currency.code, 'USD')
            self.assertEqual(currency.codein, 'BRL')
            self.assertEqual(currency.high, '5.0000')
            self.assertEqual(currency.create_date, '2022-01-01 00:00:00')


if __name__ == '__main__':
    unittest.main()
