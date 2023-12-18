class Lab4UI:
    # Constructor for the Menu class
    def __init__(self, generator, reader_writer, validator):
        self.generator = generator
        self.reader_writer = reader_writer
        self.validator = validator
        self.ascii_art_created = False
        self.menu_options = ["Enter text for ASCII art", "Create ASCII art", "Save ASCII art to file", "Exit"]

    # Method to display the menu options
    def display_options(self):
        for i, option in enumerate(self.menu_options):
            print(f"{i + 1}. {option}")

    # Method to run the menu loop
    def run(self):
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4): ", ['1', '2', '3', '4'])
            if choice == '1':
                self.generator.get_user_input()
            elif choice == '2':
                if not self.generator.text:
                    print("Error: Enter text first (option 1).")
                else:
                    self.ascii_art_created = True
                    self.generator.create_ascii_art()
            elif choice == '3':
                if not self.ascii_art_created:
                    print("Error: Create ASCII art first (option 2).")
                else:
                    filename = self.reader_writer.read_input("Enter a filename to save the ASCII art: ")
                    ascii_art_no_color = self.generator.remove_color_codes(self.generator.ascii_art)
                    self.reader_writer.write_output(filename, ascii_art_no_color)
                    print(f"ASCII art saved in file {filename}")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
