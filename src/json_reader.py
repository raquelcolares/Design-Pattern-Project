import pandas as pd


class JsonReader:
    def read_json_data(self, file_path):
        #self.logger.info("Trying to load data")
        data = pd.read_json(file_path)
        #self.logger.info("File loaded")
        return data
