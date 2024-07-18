import pandas as pd
import logging


# Singleton
class DataLoader:
    _instance = None
    # logger 
    logger = logging.getLogger('DataLoader')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    def __new__(cls, file_path=None):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
        else:
            DataLoader.logger.warning("The instance of DataLoader already exists")

        return cls._instance

    def __init__(self, file_path):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.file_path = file_path
        else:
            DataLoader.logger.warning("Instance not created: DataLoader class is singleton")

    def load_data(self):
        DataLoader.logger.info("Trying to load data")
        data = pd.read_csv(self.file_path)
        DataLoader.logger.info("File loaded ")
        return data
    
