"""Test Currency Quote Service"""
import sys
import unittest
from unittest import mock
from unittest.mock import Mock

from src.services.currency_quote_service import CurrencyQuoteService
from test.mocks.context_mock import MockContext

sys.path.append('..')


class CurrencyQuoteServiceTest(unittest.TestCase):
    """Class"""

    def setUp(self):
        self.context = MockContext()
        self.currency_quote_service = CurrencyQuoteService(self.context)

    def test_get_updated_currency(self):
        """Should return last currency conversion from USD-BRL
        """

        currency_code = 'USD-BRL'

        with mock.patch('requests.get') as requests_get_mock:
            mock_data = Mock(return_value={
                'USDBRL': {
                    'code': 'USD',
                    'codein': 'BRL',
                    'high': '5.0000',
                    'create_date': '2022-01-01 00:00:00'}})
            requests_get_mock.return_value.json = mock_data
            currency = self.currency_quote_service.get_updated_currency(
                currency_code)
            self.assertEqual(currency['code'], 'USD')
            self.assertEqual(currency['codein'], 'BRL')
            self.assertEqual(currency['high'], '5.0000')
            self.assertEqual(currency['create_date'], '2022-01-01 00:00:00')


if __name__ == '__main__':
    unittest.main()
