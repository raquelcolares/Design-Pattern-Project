from src.data_loader import DataAdapter
import pandas as pd


class DataReader:
    def __init__(self, adapter: DataAdapter):
        self.adapter = adapter

    def display_data(self, file_path):
        data = self.adapter.load_data(file_path)
        if isinstance(data, pd.DataFrame):
            print(data.head())
        else:
            for row in data:
                print(row)
        return data
