from abc import ABC, abstractmethod
from csv_reader import CsvReader
from json_reader import JsonReader
import pathlib
from logger import LoggerOutputAdapter, ConsoleAdapter, MyLogger


# Adaptor Design

class DataLoader(ABC):
    logger = MyLogger("DataLoader")
    
    @abstractmethod
    def load_data(self):
        pass

class CsvAdapter(DataLoader):
    def __init__(self):
        self.csv_reader = CsvReader()
        
    def load_data(self, file_path):
        DataLoader.logger.info("Importing the CSV")
        data = self.csv_reader.read_csv_data(file_path)
        DataLoader.logger.debug("CSV loaded")
        return data


class JsonAdapter(DataLoader):
    def __init__(self):
        self.json_reader = JsonReader()
        
    def load_data(self, file_path):
        DataLoader.logger.info("Importing the JSON")
        data = self.json_reader.read_json_data(file_path)
        DataLoader.logger.debug("JSON loaded")
        return data
    

# Singleton and Factory Designs

class AdaptorFactory:
    _instance = None
    logger = MyLogger("AdaptorFactory")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AdaptorFactory, cls).__new__(cls)
        else:
            cls.logger.warning("The instance of DataLoader already exists")
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.adapters = {
            '.csv': CsvAdapter(),
            '.json': JsonAdapter()
        }
        else:
            self.logger.warning("Instance not created: DataLoader class is singleton")

    def get_adapter(self, file_path):
        file_type = pathlib.Path(file_path).suffix
        adapter = self.adapters.get(file_type)
        if not adapter:
            raise ValueError("File is not in an available format!")
        return adapter