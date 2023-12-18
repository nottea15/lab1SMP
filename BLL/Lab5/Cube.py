from colorama import init, Fore
import re

class Cube:
    def __init__(self, size=1, color='WHITE', symbol='#', remove_shades=False):
        self.size = size
        self.color = color
        self.symbol = symbol
        self.remove_shades = remove_shades
        self.cube_3D = None
        self.cube_2D = None

    def remove_color_codes(self, string):
        # This regular expression matches all color codes
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', string)

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

        # Define matrix for cube representation
        self.cube_3D = [
            ["*" * (3 if self.size == 1 else 3) + colors[self.color] + "X" + "=" * self.size * 10 + "X" + Fore.RESET],
            ["*" * (1 if self.size == 1 else 1) + colors[self.color] + "/" + self.symbol * self.size * 11 + "/" + "|"],
            ["X" + "=" * self.size * 11 + "X" + self.symbol * self.size + "|"],
            ["|" + self.symbol * self.size * 11 + "|" + self.symbol * self.size + "X"],
            ["|" + self.symbol * self.size * 11 + "|" + self.symbol * self.size + "/"],
            ["|" + self.symbol * self.size * 11 + "|" + "/"],
            ["X" + "=" * self.size * 11 + "X" + Fore.RESET]
        ]

        # Cube shades
        if self.remove_shades:
            self.cube_3D[0][0] = self.cube_3D[0][0].replace("*", " ", 3 if self.size == 1 else 3)
            self.cube_3D[1][0] = self.cube_3D[1][0].replace("*", " ", 1)

        # Add spaces in place of removed "*"
        if self.size == 2 and self.remove_shades:
            self.cube_3D[0][0] = "  " + self.cube_3D[0][0]
            self.cube_3D[1][0] = " " + self.cube_3D[1][0]

        # Print the cube
        for row in self.cube_3D:
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
        self.cube_2D = [
            [colors[self.color] + "X" + "=" * self.size * 11 + "X"],
            ["|" + self.symbol * self.size * 11 + "|"],
            ["|" + self.symbol * self.size * 11 + "|"],
            ["|" + self.symbol * self.size * 11 + "|"],
            ["X" + "=" * self.size * 11 + "X" + Fore.RESET]
        ]

        # Print the 2D representation
        for row in self.cube_2D:
            print(''.join(row))

    def saveCube_3D(self, filename):
        # Check if cube_3D is not None
        if self.cube_3D is None:
            print("Error: Draw the 3D cube first.")
            return

        # Remove color codes from cube_3D
        cube_3D_no_color = [''.join([self.remove_color_codes(cell) for cell in row]) for row in self.cube_3D]

        # Save the cube to a file
        with open(filename, 'w') as f:
            for row in cube_3D_no_color:
                f.write(row + '\n')