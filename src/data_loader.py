from abc import ABC, abstractmethod
from src.csv_reader import CsvReader
from src.json_reader import JsonReader
import pathlib
#from .logger import MyLogger, FileAdapter, LoggerAdapter



"""
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
    def __init__(
        self, logger: MyLogger, adapter: LoggerOutputAdapter = ConsoleAdapter()
    ):
        self.logger = logger
        self.adapter = adapter

    def log(self, message, level="INFO"):
        levels = ["INFO", "WARNING", "ERROR"]
        if levels.index(level) >= levels.index(self.logger.level):
            formatted_message = f"[{level}] {self.logger.name}: {message}"
            self.adapter.write(formatted_message)


class CsvAdapter(DataAdapter):
    def __init__(self):
        self.csv_reader = CsvReader()
        self.logger = LoggerAdapter(
            MyLogger("CsvAdapter"), FileAdapter("csv_adapter.log")
        )

    def load_data(self, file_path: str) -> pd.DataFrame:
        self.logger.log(f"Loading CSV data from {file_path}", level="INFO")
        try:
            data = self.csv_reader.read_csv_data(file_path)
            df = pd.DataFrame(data)
            if df.empty or len(df) < 2:
                raise ValueError("Invalid CSV data: empty or missing header row.")
            self.logger.log("CSV data loaded successfully!", level="INFO")
            return df
        except FileNotFoundError as e:
            self.logger.log(f"File not found: {file_path}", level="ERROR")
            raise
        except ValueError as e:
            self.logger.log(str(e), level="ERROR")
            raise
        except Exception as e:
            self.logger.log(f"Error loading CSV data: {e}", level="ERROR")
            raise


class JsonAdapter(DataAdapter):
    def __init__(self):
        self.json_reader = JsonReader()
        self.logger = LoggerAdapter(
            MyLogger("JsonAdapter"), FileAdapter("json_adapter.log")
        )

    def load_data(self, file_path: str) -> pd.DataFrame:
        self.logger.log(f"Loading JSON data from {file_path}", level="INFO")
        try:
            data = self.json_reader.read_json_data(file_path)
            # Validate data (ensure it's not empty)
            if not data:
                raise ValueError("Invalid JSON data: empty.")
            self.logger.log("JSON data loaded successfully!", level="INFO")
            return pd.DataFrame(data)
        except FileNotFoundError as e:
            self.logger.log(f"File not found: {file_path}", level="ERROR")
            raise  # Re-raise the exception to signal failure
        except json.JSONDecodeError as e:
            self.logger.log(f"Error decoding JSON data: {e}", level="ERROR")
            raise  # Re-raise the exception
        except ValueError as e:
            self.logger.log(str(e), level="ERROR")
            raise  # Re-raise the exception to signal failure
        except Exception as e:
            self.logger.log(f"Error loading JSON data: {e}", level="ERROR")
            raise  # Re-raise the exception
"""

# Adaptor
class DataLoader(ABC):
    _instance = None
    #logger = MyLogger("DataLoader")

    #Singleton
    def __new__(cls, file_path=None):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        #else:
            #cls.logger.warning("The instance of DataLoader already exists")
        return cls._instance

    def __init__(self, file_path):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.file_path = file_path
        #else:
            #self.logger.warning("Instance not created: DataLoader class is singleton")

    @abstractmethod
    def load_data(self):
        pass

class CsvAdapter(DataLoader):
    def __init__(self):
        self.csv_reader = CsvReader()
        
    def load_data(self, file_path):
        data = self.csv_reader.read_csv_data(file_path)
        return data


class JsonAdapter(DataLoader):
    def __init__(self):
        self.json_reader = JsonReader()
        
    def load_data(self, file_path):
        data = self.json_reader.read_json_data(file_path)
        return data
    

# Factory
class AdaptorFactory:
    def __init__(self):
        self.adapters = {
            '.csv': CsvAdapter(),
            '.json': JsonAdapter()
        }

    def get_adapter(self, file_path):
        file_type = pathlib.Path(file_path).suffix
        adapter = self.adapters.get(file_type)
        if not adapter:
            raise ValueError('File is not in an available format!')
        return adapter