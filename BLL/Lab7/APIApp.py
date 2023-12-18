import requests
from colorama import Fore
from colorama import Style

class APIApp:
    def __init__(self, api_client, reader_writer, validator, history, error_handler, results_display, input_parser, data_saver):
        self.api_client = api_client
        self.reader_writer = reader_writer
        self.validator = validator
        self.history = history
        self.error_handler = error_handler
        self.results_display = results_display
        self.input_parser = input_parser
        self.data_saver = data_saver

    def get_data_from_api(self):
        return self.api_client.get_data()

    def get_user_input(self):
        user_input = self.reader_writer.read_input(f"Enter email: ")
        return user_input

    def run(self, data_type, user_input):
        try:
            # Task 1: Selecting the API provider
            data_from_api = self.api_client.get_data()

            # Checking the validity of the user's input
            if self.validator.validate_email(user_input):
                print("Email is valid.")
                response = requests.get("https://jsonplaceholder.typicode.com/users?email=" + user_input)
                self.history.add_to_history(user_input, response.json())

                # Task 5: Displaying the results
                self.results_display.display_data(response.json(), Fore.BLUE, Style.BRIGHT)
            else:
                print("Invalid email format. Please enter the email in the correct format.")
                self.data_saver.save_data(data_from_api, 'json')

        except Exception as e:
            print(f"Error: {e}")

