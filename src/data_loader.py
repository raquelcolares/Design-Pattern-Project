import pandas as pd
import logging
import pickle
from abc import ABC, abstractmethod
from .csv_reader import CsvReader
from .json_reader import JsonReader


# Adapter
## interface
class DataAdapter(ABC):
    @abstractmethod
    def load_data(self, file_path):
        pass


# Logger Adapter
class LoggerOutputAdapter(ABC):
    @abstractmethod
    def write(self, message):
        pass


class ConsoleAdapter(LoggerOutputAdapter):
    def write(self, message):
        print(message)


class FileAdapter(LoggerOutputAdapter):
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        with open(self.filename, "a") as f:
            f.write(message + "\n")


class LoggerAdapter:
    def __init__(self, logger, adapter: LoggerOutputAdapter = ConsoleAdapter()):
        self.logger = logger
        self.adapter = adapter

    def log(self, message, level=logging.INFO):
        formatted_message = f"{level} - {message}"
        self.adapter.write(formatted_message)


class CsvAdapter(DataAdapter):
    def __init__(self):
        self.csv_reader = CsvReader()
        self.logger = LoggerAdapter(
            logging.getLogger("CsvAdapter")
        )  # Logger do Adapter

    def load_data(self, file_path: str) -> pd.DataFrame:
        self.logger.log(f"Loading CSV data from {file_path}")  # Log
        try:
            data = self.csv_reader.read_csv_data(file_path)
            df = pd.DataFrame(data[1:], columns=data[0])
            self.logger.log("CSV data uploaded successfully!")
            return df
        except Exception as e:
            self.logger.log(f"Error loading CSV data: {e}", level=logging.ERROR)
            raise e


class JsonAdapter(DataAdapter):
    def __init__(self):
        self.json_reader = JsonReader()
        self.logger = LoggerAdapter(logging.getLogger("JsonAdapter"))

    def load_data(self, file_path: str) -> pd.DataFrame:
        self.logger.log(f"Loading JSON data from {file_path}")
        try:
            data = self.json_reader.read_json_data(file_path)
            self.logger.log("JSON data loaded successfully!")
            return pd.DataFrame(data)
        except Exception as e:
            self.logger.log(f"Error loading JSON data: {e}", level=logging.ERROR)
            raise e


# Singleton
class DataLoader:
    _instance = None
    # logger
    logger = logging.getLogger("DataLoader")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    def __new__(cls, file_path=None):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        else:
            DataLoader.logger.warning("The instance of DataLoader already exists")

        return cls._instance

    def __init__(self, file_path):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.file_path = file_path
        else:
            DataLoader.logger.warning(
                "Instance not created: DataLoader class is singleton"
            )

    def load_data(self):
        DataLoader.logger.info("Trying to load data")
        data = pd.read_csv(self.file_path)
        DataLoader.logger.info("File loaded ")
        return data
