import unittest
from data_loader import AdaptorFactory, CsvAdapter, JsonAdapter
import pandas as pd



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
## Adaptor 

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


if __name__ == "__main__":
    unittest.main()
