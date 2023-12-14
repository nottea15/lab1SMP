import json
import os
import re


# Class for handling user input and parsing
class InputParser:

    def __init__(self):
        patterns = {
            "date": "\\b(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/((?:19|20)\\d\\d)\\b",
            "phone": "\\+\\d{2}[-. (]*\\d{3}[-. )]*\\d{3}[-. ]*\\d{2}[-. ]*\\d{2}",
            "email": "\\S+@\\S+\\.\\S+",
            "credit_card": "\\b\\d{4}[-.\\s]?\\d{4}[-.\\s]?\\d{4}[-.\\s]?\\d{4}\\b"
        }
        self.date_pattern = patterns['date']
        self.phone_pattern = patterns['phone']
        self.email_pattern = patterns['email']
        self.credit_card_pattern = patterns['credit_card']

    def parse_user_input(self, user_input):
        date_tuples = re.findall(self.date_pattern, user_input)
        dates = ['/'.join(date_tuple) for date_tuple in date_tuples]
        phones = re.findall(self.phone_pattern, user_input)
        emails = [email.rstrip(',') for email in re.findall(self.email_pattern, user_input)]
        credit_cards = re.findall(self.credit_card_pattern, user_input)

        return dates, phones, emails, credit_cards

