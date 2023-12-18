import json
import os
from colorama import Fore
from colorama import Style

class MenuLab7:
    def __init__(self, api_app, validator, reader_writer):
        self.api_app = api_app
        self.validator = validator
        self.reader_writer = reader_writer
        self.menu_options = ["Find by email", "View history", "Display all data", "Save data", "Exit"]

    def display_options(self):
        print("Dmytro's JSONPlaceholder")  # Red color for title
        for i, option in enumerate(self.menu_options):
            print(f"{i + 1}. {option}")

    def run(self):
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4/5): ", ['1', '2', '3', '4', '5'])
            if choice == '1':
                valid_data = False
                data = None
                while not valid_data:
                    user_input = self.api_app.get_user_input()
                    if self.validator.validate_email(user_input):
                        valid_data = True
                if valid_data:
                    self.api_app.run('', user_input)
            elif choice == '2':
                self.api_app.history.view_history()
            elif choice == '3':
                display_choice = self.validator.validate_input("Choose a data display format (list/table): ",
                                                               ['list', 'table'])
                data_from_api = self.api_app.get_data_from_api()
                self.api_app.history.add_to_history('Display data', data_from_api)
                if display_choice == 'list':
                    print(data_from_api)
                else:
                    self.api_app.results_display.display_data(data_from_api, Fore.BLUE, Style.BRIGHT)
            elif choice == '4':
                save_choice = self.validator.validate_input("Do you want to save the data? (yes/no): ", ['yes', 'no'])
                if save_choice == 'yes':
                    format_choice = self.validator.validate_input(
                        "Choose a format to save the data (json/csv/txt): ", ['json', 'csv', 'txt'])
                    self.api_app.data_saver.save_data(self.api_app.get_data_from_api(), format_choice)
                    print(f"Data saved in {format_choice} format.")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
