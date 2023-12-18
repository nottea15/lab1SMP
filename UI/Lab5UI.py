import json
import os
from BLL.Lab5.Cube import Cube
from BLL.Lab5.Pyramid import Pyramid


class Lab5UI:
    def __init__(self, reader_writer, validator):
        self.reader_writer = reader_writer
        self.validator = validator
        self.figure = None
        self.menu_options = ["Choose figure", "Enter parameters for figure", "Show 3D figure", "Show 2D figure",
                             "Save 3D figure to file", "Exit"]

    def display_options(self):
        print("Dmytro's ART Generator")  # Red color for title
        for i, option in enumerate(self.menu_options):
            print(f"{i + 1}. {option}")

    def run(self):
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4/5/6): ", ['1', '2', '3', '4', '5', '6'])
            if choice == '1':
                figure_choice = self.validator.validate_input("Choose a figure (Cube/Pyramid): ", ['Cube', 'Pyramid'])
                if figure_choice == 'Cube':
                    self.figure = Cube()
                else:
                    self.figure = Pyramid()
            elif choice == '2':
                if self.figure is None:
                    print("Error: Choose a figure first (option 1).")
                else:
                    size = self.validator.validate_input("Enter size for figure (1 or 2): ", ['1', '2'])
                    color = self.validator.validate_input(
                        "Enter color for figure (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE): ",
                        ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE'])
                    symbol = self.reader_writer.read_input("Enter symbol for figure: ")
                    remove_shades = self.validator.validate_input(
                        "Do you want to remove shades? (yes/no): ", ['yes', 'no'])
                    self.figure = Cube(int(size), color, symbol, remove_shades.lower() == 'yes') if isinstance(
                        self.figure, Cube) else Pyramid(int(size), color, symbol, remove_shades.lower() == 'yes')
            elif choice == '3':
                if self.figure is None:
                    print("Error: Enter parameters for figure first (option 2).")
                else:
                    self.figure.draw_3D()
            elif choice == '4':
                if self.figure is None:
                    print("Error: Enter parameters for figure first (option 2).")
                else:
                    self.figure.draw_2D()
            elif choice == '5':
                if self.figure is None:
                    print("Error: Enter parameters for figure first (option 2).")
                else:
                    filename = self.reader_writer.read_input("Enter a filename to save the 3D figure: ")
                    if isinstance(self.figure, Cube):
                        self.figure.saveCube_3D(filename)
                    else:
                        self.figure.savePyramid_3D(filename)
                    print(f"3D figure saved in file {filename}")
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")