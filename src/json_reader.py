import pandas as pd


class JsonReader:
    def read_json_data(self, file_path):
        data = pd.read_json(file_path)
        return data
