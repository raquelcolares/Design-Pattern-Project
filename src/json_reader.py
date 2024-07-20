import json
from src.logger import MyLogger, ConsoleAdapter


class JsonReader:
    def __init__(self):
        self.logger = MyLogger("JsonReader", "INFO", ConsoleAdapter())

    def read_json_data(self, file_path):
        self.logger.info(f"Reading JSON data from {file_path}")
        # Add the actual logic to read JSON data
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
