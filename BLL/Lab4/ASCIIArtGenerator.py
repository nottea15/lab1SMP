from Shared.Validator import Validator
from Shared.color_util import ColorUtil


# Constructor for the ASCIIArtGenerator class
class ASCIIArtGenerator:
    def __init__(self, ascii_art, reader_writer):
        self.ascii_art = ascii_art
        self.text = ''
        self.validator = Validator()
        self.reader_writer = reader_writer

    # Method to get user input for the text to be converted to ASCII art
    def get_user_input(self):
        self.text = self.reader_writer.read_input('Enter a word: ')

    # Method to get user input for the symbol to be used in the ASCII art
    def get_user_symbol(self):
        symbol_mapping = {
            '*': 'Star (*)',
            '#': 'Hash character (#)',
            '@': 'Special character (@)',
            '?': 'Question mark (?)',
            '=': 'Equal sign (=)',
            '-': 'Hyphen (-)'
        }

        print("Available symbols for ASCII art:")
        for symbol, description in symbol_mapping.items():
            print(f"{symbol}: {description}")

        user_choice = self.reader_writer.read_input('Choose a symbol for ASCII art: ')
        if user_choice in symbol_mapping:
            self.user_symbol = user_choice
        else:
            print("Invalid choice.")

    # Method to get user input for the size of the ASCII art
    def get_art_size(self):
        self.width = int(self.reader_writer.read_input('Enter the width of the ASCII art (2-40): '))
        self.height = int(self.reader_writer.read_input('Enter the height of the ASCII art (2-40): '))

    # Method to get user input for the alignment of the ASCII art
    def get_alignment(self):
        alignment_options = {
            'left': 'left',
            'center': 'center',
            'right': 'right',
        }
        choice = self.reader_writer.read_input('Choose text alignment (left/center/right): ')
        if choice in alignment_options:
            self.alignment = alignment_options[choice]
        else:
            print("Invalid choice.")

    # Method to get user input for the colors of the symbols in the ASCII art
    def get_colors(self):
        self.colors = []
        for i in range(len(self.user_symbol)):
            color_options = {
                'white': 'white',
                'grey': 'grey',
            }
            choice = self.reader_writer.read_input(f'Choose a color for symbol {self.user_symbol[i]}: ')
            while choice not in color_options:
                print("Invalid choice.")
                choice = self.reader_writer.read_input(f'Choose a color for symbol {self.user_symbol[i]}: ')
            self.colors.append(choice)

    # Method to generate ASCII art based on user input
    def generate_art(self):
        ascii_art = ''
        for char in self.text:
            if char.upper() in self.ascii_art:
                art = self.ascii_art[char.upper()]
                art = [line.replace('*', self.user_symbol) for line in art]
                art = art[:self.height]
                while len(art) < self.height:
                    art.append(' ' * self.width)
                ascii_art += '\n'.join(art) + '\n'
            else:
                ascii_art += f"ASCII art for the letter {char} is not available.\n"

        if self.alignment == 'center':
            lines = ascii_art.strip().split('\n')
            ascii_art = '\n'.join(line.center(self.width) for line in lines)
        elif self.alignment == 'right':
            lines = ascii_art.strip().split('\n')
            ascii_art = '\n'.join(line.rjust(self.width) for line in lines)

        colored_art = ''
        for symbol, color in zip(self.user_symbol, self.colors):
            colored_art += ColorUtil.colorize(symbol, color)

        ascii_art = ascii_art.replace(self.user_symbol, colored_art)
        return ascii_art

    # Method to create ASCII art based on user input
    def create_ascii_art(self):
        self.get_user_symbol()
        self.get_art_size()
        self.get_alignment()
        self.get_colors()
        self.ascii_art = self.generate_art()
        self.display_art(self.ascii_art)

    # Method to display the generated ASCII art
    def display_art(self, ascii_art):
        print("Created ASCII art:")
        print(ascii_art)

    # Method to save the generated ASCII art to a file
    def save_to_file(self):
        filename = self.reader_writer.read_input("Enter a filename to save the ASCII art: ")
        ascii_art_no_color = self.remove_color_codes(self.ascii_art)
        self.reader_writer.write_output(filename, ascii_art_no_color)
        print(f"ASCII art saved in file {filename}")

    # Method to remove color codes from the text
    def remove_color_codes(self, text):
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text
