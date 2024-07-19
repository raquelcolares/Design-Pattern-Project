import csv
from .logger import MyLogger, LoggerAdapter, FileAdapter


class CsvReader:
    def __init__(self):
        self.logger = LoggerAdapter(
            MyLogger("CsvReader"), FileAdapter("csv_reader.log")
        )

    def read_csv_data(self, file_path):
        """Read CSV data from file path"""
        data = []
        self.logger.info(f"Reading CSV data from {file_path}")
        try:
            with open(file_path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
                self.logger.info(f"Successfully read {len(data)} rows from CSV file.")
            return data
        except FileNotFoundError as e:
            self.logger.error(f"Error: CSV file not found - {e}")
            return None  # Or raise an exception if appropriate
