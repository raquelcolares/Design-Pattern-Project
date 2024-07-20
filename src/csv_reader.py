import pandas as pd
from .logger import MyLogger, ConsoleAdapter


class CsvReader:
    def __init__(self):
        self.logger = MyLogger(
            "CsvReader", "INFO", ConsoleAdapter()
        )  # Ensure a valid adapter is set

    def read_csv_data(self, file_path):
        self.logger.info(f"Reading CSV data from {file_path}")
        try:
            data = pd.read_csv(file_path).values.tolist()
            return data
        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            self.logger.error(f"Error reading CSV data: {e}")
            raise
