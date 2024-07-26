from data_loader import AdaptorFactory, CsvAdapter, JsonAdapter
from subscribers import FileSubscriber
from logger import *
import pandas as pd
import unittest
from unittest.mock import patch
from io import StringIO


# First Test:
## Singleton 
class TestSingletonDataLoader(unittest.TestCase):
    def test_singleton_data_loader(self):
        # Action
        s1_adapter = AdaptorFactory()
        s2_adapter = AdaptorFactory()
        # Assert:
        self.assertEqual(s1_adapter, s2_adapter)


# Second Test:
## Adaptor and Factory

class TestAdapters(unittest.TestCase):
    def test_csv_adapter(self):
        adapter = CsvAdapter()
        data_csv = adapter.load_data("data\weather_classification_data.csv")
        expected_shape = (13200, 11)
        self.assertEqual(data_csv.shape, expected_shape)

    def test_json_adapter(self):
        adapter = JsonAdapter()
        data_json = adapter.load_data("data\weather_classification_data.json")
        expected_shape = (13200, 11)
        self.assertEqual(data_json.shape, expected_shape)


# Third Test:
## Observer

class TestLogger(unittest.TestCase):
    # 1st
    def test_logger_consoleAdaptor(self):
        log_console = MyLogger("Test1")
        with patch("sys.stdout", new = StringIO()) as console_out:
            log_console.info("Message 1")
            self.assertEqual("[INFO] Test1: Message 1\n", console_out.getvalue())

    # 2nd    
    def test_logger_fileAdaptor(self):
        file_adapter = FileAdapter("Test_file.txt")
        log_file = MyLogger("Test2", "INFO", file_adapter)
        log_file.info("Message 2")
        with open("Test_file.txt", "r") as f:
            for line in f:
                written_string = line        
        self.assertEqual("[INFO] Test2: Message 2\n", line)

    # 3rd
    def test_logger_observer(self):
        logger = MyLogger("Test3")
        logger_subscriber = FileSubscriber()
        logger.register_WarningSubscriber(logger_subscriber)
        logger.warning("Warning message test")
        with open("logger_subscriber.txt", "r") as f:
            for line in f:
                written_string = line        
        self.assertEqual("[WARNING] Test3: Warning message test\n", line)

        

if __name__ == "__main__":
    unittest.main()



