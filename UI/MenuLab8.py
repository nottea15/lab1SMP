import json
import os


class MenuLab8:
    # Constructor method for the MenuLab8 class
    def __init__(self, data_processor, validator, reader_writer):
        self.data_processor = data_processor
        self.validator = validator
        self.reader_writer = reader_writer
        self.menu_options = ["Explore Data", "Generate Visualizations", "Save Visualizations", "Exit"],

    def display_options(self):
        print("Data analysis")  # Red color for title
        for i, option in enumerate(self.menu_options):
            print(f"{i + 1}. {option}")

    # Method to run the menu
    def run(self):
        # Define the valid options
        valid_options = ['1', '2', '3', '4']

        # Loop until the user chooses to exit
        while True:
            # Display the menu options
            self.display_options()

            # Get the user's choice and validate it
            choice = self.validator.validate_input("Choose an option (1/2/3/4): ", valid_options)

            # Perform the action corresponding to the user's choice
            if choice == '1':
                # If the user chooses to explore data, ask for confirmation and then explore data
                if self.validator.validate_input("Explore data? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Exploring data...")
                    self.data_processor.explore_data()
            elif choice == '2':
                # If the user chooses to generate visualizations, ask for confirmation and then generate visualizations
                if self.validator.validate_input("Generate visualizations? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Generating visualizations...")
                    self.data_processor.visualize_data()
            elif choice == '3':
                # If the user chooses to save visualizations, ask for confirmation and then save visualizations
                if self.validator.validate_input("Save visualizations? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Saving visualizations...")
                    self.data_processor.visualize_data(save=True)
            elif choice == '4':
                # If the user chooses to exit, print a goodbye message and break the loop
                print("Goodbye!")
                break




