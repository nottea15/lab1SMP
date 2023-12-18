import json
import pandas as pd


# Class for saving data
class DataSaver:
    def save_data(self, data, format):
        if format == 'json':
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
        elif format == 'csv':
            if isinstance(data, dict):
                data = [data]  # convert dictionary to list of dictionaries
            df = pd.DataFrame(data)  # create DataFrame
            df.to_csv('data.csv')
        elif format == 'txt':
            with open('data.txt', 'w') as f:
                for item in data:
                    f.write("%s\n" % item)
