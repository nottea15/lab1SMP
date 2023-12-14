import unittest
from unittest.mock import patch, Mock

from BLL.Lab7.APIClient import APIClient
from BLL.Lab7.InputParser import InputParser
from Shared.Validator import Validator


# Unit tests for the API
class UnitTestsAPI(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient('https://jsonplaceholder.typicode.com/users')
        self.validator = Validator()

    @patch('requests.get')
    def test_get_data(self, mock_get):
        mock_response = Mock()
        expected_dict = {"title": "foo", "body": "bar", "userId": 1}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response
        self.assertEqual(self.api_client.get_data(), expected_dict)

    def test_validate_phone(self):
        self.assertTrue(self.validator.validate_phone('+380631234567'))
        self.assertFalse(self.validator.validate_phone('1234567'))

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email('test@example.com'))
        self.assertFalse(self.validator.validate_email('testexample.com'))

    def test_validate_credit_card(self):
        self.assertTrue(self.validator.validate_credit_card('1234-5678-9012-3456'))
        self.assertFalse(self.validator.validate_credit_card('1234-5678-9012'))

    def test_validate_date(self):
        self.assertTrue(self.validator.validate_date('31/12/2023'))
        self.assertFalse(self.validator.validate_date('31/13/2023'))

    def test_parse_user_input(self):
        dates, phones, emails, credit_cards = self.input_parser.parse_user_input('31/12/2023, +380631234567, test@example.com, 1234-5678-9012-3456')
        self.assertEqual(dates, ['31/12/2023'])
        self.assertEqual(phones, ['+380631234567'])
        self.assertEqual(emails, ['test@example.com'])
        self.assertEqual(credit_cards, ['1234-5678-9012-3456'])


if __name__ == '__main__':
    unittest.main()