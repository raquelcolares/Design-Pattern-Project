import json
from .logger import MyLogger, LoggerAdapter, FileAdapter


class JsonReader:
    def read_json_data(self, file_path):
        self.logger = LoggerAdapter(
            MyLogger("CsvAdapter"), FileAdapter("csv_adapter.log")
        )
        """Read JSON data from file path"""
        with open(file_path, mode="r", encoding="utf-8") as file:
            data = json.load(file)
        return data
