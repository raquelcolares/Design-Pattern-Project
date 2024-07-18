import json


class JsonReader:
    def read_json_data(self, file_path: str):
        with open(file_path, mode="r") as file:
            data = json.load(file)
        return data
