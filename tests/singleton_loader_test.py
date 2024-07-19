import unittest
from src.data_loader import DataLoader, CsvAdapter, JsonAdapter, DataAdapter
import pandas as pd
import json


class TestSingletonDataLoader(unittest.TestCase):

    def test_singleton_data_loader(self):
        file_path = "data\weather_classification_data.csv"

        # Action
        s1 = DataLoader(file_path)
        s2 = DataLoader(file_path)
        # Assert:
        self.assertEqual(s1, s2)


class TestAdapters(unittest.TestCase):
    def test_csv_adapter(self):
        adapter = CsvAdapter()
        df = adapter.load_data("data/weather_classification_data.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)  # Check if data was loaded

    def test_json_adapter(self):
        adapter = JsonAdapter()

        # Create a sample JSON file for testing
        data = [{"key1": "value1"}, {"key2": "value2"}]
        with open("test.json", "w") as f:
            json.dump(data, f)

        df = adapter.load_data("test.json")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

    def test_data_adapter_abstract(self):
        with self.assertRaises(TypeError):
            DataAdapter()


if __name__ == "__main__":
    unittest.main()
