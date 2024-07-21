import pandas as pd


class CsvReader:
    def read_csv_data(self, file_path):
        data = pd.read_csv(file_path)
        return data
