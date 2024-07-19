import json
from .logger import MyLogger, LoggerAdapter, FileAdapter


class JsonReader:
    def __init__(self):
        self.logger = LoggerAdapter(
            MyLogger("JsonReader"), FileAdapter("json_reader.log")
        )

    def read_json_data(self, file_path):
        """Read JSON data from file path"""
        self.logger.info(f"Reading JSON data from {file_path}")
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
                self.logger.info(
                    f"Successfully read {len(data)} records from JSON file."
                )
            return data
        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON: {e}")
            return None
