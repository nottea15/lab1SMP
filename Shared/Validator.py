import re

from BLL.Lab7.InputParser import InputParser


# Utility class for validating user input against predefined choices
class Validator:

    def __init__(self):
        self.input_parser = InputParser()

    def validate_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input not in valid_options:
                print("Invalid input. Please try again.")
            else:
                return user_input

    def validate_date(self, date):
        # Перевірка, чи дата відповідає правильному формату
        if not re.match(self.input_parser.date_pattern, date):
            print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")
            return False
        return True

    def validate_phone(self, phone):
        # Перевірка, чи телефон відповідає правильному формату
        if not re.match(self.input_parser.phone_pattern, phone):
            print("Invalid phone format. Please enter the phone in the correct format.")
            return False
        return True

    def validate_email(self, email):
        # Перевірка, чи електронна пошта відповідає правильному формату
        if not re.match(self.input_parser.email_pattern, email):
            print("Invalid email format. Please enter the email in the correct format.")
            return False
        return True

    def validate_credit_card(self, credit_card):
        # Перевірка, чи кредитна картка відповідає правильному формату
        if not re.match(self.input_parser.credit_card_pattern, credit_card):
            print("Invalid credit card format. Please enter the credit card in the correct format.")
            return False
        return True

