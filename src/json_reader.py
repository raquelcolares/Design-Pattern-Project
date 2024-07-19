import json
import csv


class JsonReader:
    def read_json_data(self, file_path):
        """Read JSON data from file path"""
        with open(file_path, mode="r", encoding="utf-8") as file:
            data = json.load(file)
        return data
