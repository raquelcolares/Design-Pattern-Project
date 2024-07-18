from src.data_loader import DataAdapter


class DataReader:
    def __init__(self, adapter: DataAdapter):
        self.adapter = adapter

    def display_data(self, file_path: str):
        data = self.adapter.read_data(file_path)
        for key, value in data.items():
            print(f"{key}: {value}")
