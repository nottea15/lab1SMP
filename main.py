# Task 10: User-friendly interface

import pyfiglet #Завдання 2: Бібліотека ASCII-арту
from colorama import Fore, Style

print(Fore.LIGHTMAGENTA_EX + "Welcome to ASCII ART program. Enjoy!" + Style.RESET_ALL)
def get_user_input():

# Task 1: User input
   user_input = input(Fore.LIGHTYELLOW_EX + "Enter a word or phrase to convert to ASCII art: ")

# Task 3: Choosing a font
   print("Available font styles:\n" + Fore.LIGHTWHITE_EX + "1. standard\n2. banner\n3. slant\n4. script"+ Fore.LIGHTYELLOW_EX)

   while True:
       try:
           font_choice = int(input("Choose a font style number" + Fore.LIGHTWHITE_EX + "(1-4):" + Fore.LIGHTYELLOW_EX))
           if 1 <= font_choice <= 5:
               break
           else:
               print("Please enter a number between 1 and 4.")
       except ValueError:
           print("Please enter the correct font style number.")

# Task 4: Text color
   print("Available text colors:\n" + Fore.LIGHTRED_EX + "1. Red\n" + Fore.LIGHTBLUE_EX + "2. Blue\n" + Fore.LIGHTGREEN_EX + "3. Green")

   while True:
       try:
           color_choice = int(input(Fore.LIGHTYELLOW_EX + "Choose a text color number " + Fore.LIGHTWHITE_EX + "(1-3):" + Fore.LIGHTYELLOW_EX))
           if 1 <= color_choice <= 3:
               break
           else:
               print("Please enter a number between 1 and 3.")
       except ValueError:
           print("Please enter the correct text color number.")

   while True:
       try:
           width = int(input("Enter the width of the ASCII art " + Fore.LIGHTWHITE_EX +  "(number of characters in a line):" + Fore.LIGHTYELLOW_EX))
           if width > 0:
               break
           else:
               print("Please enter a number greater than zero.")
       except ValueError:
           print("Please enter the correct width.")

   while True:
       try:
           height = int(input("Enter the height of the ASCII art " + Fore.LIGHTWHITE_EX +  "(number of lines):" + Fore.LIGHTYELLOW_EX))
           if height > 0:
               break
           else:
               print("Please enter a number greater than zero.")
       except ValueError:
           print("Please enter the correct height.")

# Task 8: Selection of symbols
   use_custom_chars = input("Do you want to choose a special character to create ASCII art? " + Fore.LIGHTWHITE_EX +  "(y/n):" + Fore.LIGHTYELLOW_EX).strip().lower()
   if use_custom_chars == 'y':
       char_set = input("Enter the characters you want to use for ASCII art " + Fore.LIGHTWHITE_EX + "(eg '@#*'):" + Fore.LIGHTYELLOW_EX)
   else:
       char_set = None

   preview_enabled = input("Want to preview your ASCII art before saving?" + Fore.LIGHTWHITE_EX + " (y/n):"+ Fore.LIGHTYELLOW_EX).strip().lower()

   return user_input, font_choice, color_choice, width, height, char_set, preview_enabled


# Task 9: Preview function
def preview_ascii_art(ascii_text, selected_color):
   print(selected_color + ascii_text + Style.RESET_ALL)


def generate_ascii_art(text, font_choice, color_choice, width, height, char_set=None):
   fonts = ['standard', 'banner', 'slant', 'script']
   selected_font = fonts[font_choice - 1]
   ascii_art = pyfiglet.Figlet(font=selected_font)

   colors = [Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX]
   selected_color = colors[color_choice - 1]

   ascii_text = ascii_art.renderText(text)
   ascii_lines = ascii_text.split('\n')

# Task 7: The size of ART
   scaled_ascii_lines = []
   char_set_length = len(char_set) if char_set else 0
   for line in ascii_lines:
       scaled_line = ""
       for char in line:
           if char == ' ':
               scaled_line += ' '
           else:
               if char_set:
                   scaled_line += char_set[hash(char) % char_set_length]
               else:
                   scaled_line += char
       scaled_ascii_lines.append(scaled_line.center(width)[:width])

   scaled_ascii_text = '\n'.join(scaled_ascii_lines[:height])

   colored_text = selected_color + scaled_ascii_text + Style.RESET_ALL
   return colored_text


def main():
   user_input, font_choice, color_choice, width, height, char_set, preview_enabled = get_user_input()
   ascii_text = generate_ascii_art(user_input, font_choice, color_choice, width, height, char_set)

   if preview_enabled == 'y':
       selected_color = [Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX][color_choice - 1]
       preview_ascii_art(ascii_text, selected_color)

# Task 6: Saving to a file
   save_confirmation = input(Fore.LIGHTYELLOW_EX + "Want to save ASCII art to a file?" + Fore.LIGHTWHITE_EX + " (y/n):").strip().lower()
   if save_confirmation == 'y':
       file_name = input(Fore.LIGHTYELLOW_EX + "Enter a file name to save the ASCII art " + Fore.LIGHTWHITE_EX + "(without extension):")
       with open(f"{file_name}.txt", "w") as file:
           file.write(ascii_text)
       print(Fore.LIGHTYELLOW_EX + f"ASCII art is saved in a file {file_name}.txt\n" + Fore.LIGHTMAGENTA_EX + "Thank you for using my program!")


if __name__ == "__main__":
   main()