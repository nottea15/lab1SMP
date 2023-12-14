import pandas as pd
from tabulate import tabulate
from colorama import Style
import numpy as np


# Class for displaying results
class ResultsDisplay:
    def display_data(self, data, headers_color, font_style):
        if np.isscalar(data):
            df = pd.DataFrame([data])  # if data is a scalar value, create DataFrame from list
        elif isinstance(data, dict):
            df = pd.DataFrame([data])  # if data is a dictionary, create DataFrame from list of dictionaries
        else:
            df = pd.DataFrame(data)  # otherwise, create DataFrame as usual
        formatted_table = tabulate(df, headers='keys', tablefmt='psql')
        print(self.apply_styles(formatted_table, headers_color, font_style))

    def apply_styles(self, text, color, style):
        return f"{color}{style}{text}{Style.RESET_ALL}"
