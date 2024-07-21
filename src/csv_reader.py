import pandas as pd
#from logger import MyLogger, ConsoleAdapter


class CsvReader:
    def read_csv_data(self, file_path):
        #self.logger.info("Trying to load data")
        data = pd.read_csv(file_path)
        #self.logger.info("File loaded")
        return data
