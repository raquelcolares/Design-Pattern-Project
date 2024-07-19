import csv
from .logger import MyLogger, LoggerAdapter, FileAdapter


class CsvReader:
    def read_csv_data(self, file_path):
        """Read CSV data from file path"""
        data = []
        self.logger = LoggerAdapter(
            MyLogger("CsvAdapter"), FileAdapter("csv_adapter.log")
        )
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        return data
