from colorama import init, Fore
import re

class Pyramid:
    def __init__(self, size=1, color='WHITE', symbol='#', remove_shadesPyramid=False):
        self.size = size
        self.color = color
        self.symbol = symbol
        self.remove_shadesPyramid = remove_shadesPyramid
        self.pyramid_3D = None
        self.pyramid_2D = None

    def remove_color_codes(self, string):
        # This regular expression matches all color codes
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', string)

    def remove_shades(self):
        # Pyramid shades
        if self.pyramid_3D is not None:
            self.pyramid_3D = [[cell.replace("=", "") for cell in row] for row in self.pyramid_3D]
        if self.pyramid_2D is not None:
            self.pyramid_2D = [[cell.replace("=", "") for cell in row] for row in self.pyramid_2D]

    def draw_3D(self):
        # Initialize colorama
        init()

        # Define colors
        colors = {
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'YELLOW': Fore.YELLOW,
            'BLUE': Fore.BLUE,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE
        }

        # Define matrix for pyramid representation
        self.pyramid_3D = [
            [colors[self.color] + " " * self.size * 11 + "/\\" + "*" * self.size + "."],
            [" " * self.size * 10 + "/" + self.symbol * self.size * 2 + "\\" + "*" * self.size * 2 + "."],
            [" " * self.size * 9 + "/" + self.symbol * self.size * 4 + "\\" + "*" * self.size * 3 + "."],
            [" " * self.size * 8 + "/" + self.symbol * self.size * 6 + "\\" + "*" * self.size * 4 + "."],
            [" " * self.size * 7 + "/" + self.symbol * self.size * 8 + "\\" + "*" * self.size * 4 + "|"],
            [" " * self.size * 6 + "/" + self.symbol * self.size * 10 + "\\" + "*" * self.size * 3 + "|"],
            [" " * self.size * 5 + "/" + self.symbol * self.size * 12 + "\\" + "*" * self.size * 2 + "|"],
            [" " * self.size * 4 + "/" + self.symbol * self.size * 14 + "\\" + "*" * self.size + "|"],
            [" " * self.size * 3 + "/" + "_" * self.size * 16 + "\\" + "|" + Fore.RESET],
            [" " * self.size * 2 + "=" * self.size * 15],
            [" " * self.size * 2 + "=" * self.size * 12],
            [" " * self.size * 2 + "=" * self.size * 9],
            [" " * self.size * 2 + "=" * self.size * 6],
            [" " * self.size * 2 + "=" * self.size * 3]
        ]

        # If remove_shadesPyramid is True, remove the shades
        if self.remove_shadesPyramid:
            self.remove_shades()

        # Print the pyramid
        for row in self.pyramid_3D:
            print(''.join(row))

    def draw_2D(self):
        # Initialize colorama
        init()

        # Define colors
        colors = {
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'YELLOW': Fore.YELLOW,
            'BLUE': Fore.BLUE,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE
        }

        # Define matrix for 2D representation
        self.pyramid_2D = [
            [colors[self.color] + " " * self.size * 11 + "/\\"],
            [" " * self.size * 10 + "/" + self.symbol * self.size * 2 + "\\"],
            [" " * self.size * 9 + "/" + self.symbol * self.size * 4 + "\\"],
            [" " * self.size * 8 + "/" + self.symbol * self.size * 6 + "\\"],
            [" " * self.size * 7 + "/" + self.symbol * self.size * 8 + "\\"],
            [" " * self.size * 6 + "/" + self.symbol * self.size * 10 + "\\"],
            [" " * self.size * 5 + "/" + self.symbol * self.size * 12 + "\\"],
            [" " * self.size * 4 + "/" + self.symbol * self.size * 14 + "\\"],
            [" " * self.size * 3 + "/" + "_" * self.size * 16 + "\\" + Fore.RESET]
        ]

        # If remove_shadesPyramid is True, remove the shades
        if self.remove_shadesPyramid:
            self.remove_shades()

        # Print the 2D representation
        for row in self.pyramid_2D:
            print(''.join(row))

    def set_size(self, size):
        if size in [1, 2]:
            self.size = size
        else:
            print("Invalid size. Please choose 1 or 2.")

    def savePyramid_3D(self, filename):
        # Check if pyramid_3D is not None
        if self.pyramid_3D is None:
            print("Error: Draw the 3D pyramid first.")
            return

        # Remove color codes from pyramid_3D
        pyramid_3D_no_color = [''.join([self.remove_color_codes(cell) for cell in row]) for row in self.pyramid_3D]

        # Save the pyramid to a file
        with open(filename, 'w') as f:
            for row in pyramid_3D_no_color:
                f.write(row + '\n')
