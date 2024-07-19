from src.data_loader import DataAdapter


class DataReader:
    def __init__(self, adapter: DataAdapter):
        self.adapter = adapter

    def display_data(self, file_path):
        data = self.adapter.load_data(file_path)
        print(data)
