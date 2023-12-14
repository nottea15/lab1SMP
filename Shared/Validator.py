import re

# Utility class for validating user input against predefined choices
class Validator:

    def validate_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input not in valid_options:
                print("Invalid input. Please try again.")
            else:
                return user_input



