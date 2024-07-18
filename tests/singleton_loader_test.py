import unittest
from data_loader import DataLoader



class TestSingletonDataLoader(unittest.TestCase):

    def test_singleton_data_loader(self):
        file_path = 'data\weather_classification_data.csv'

        # Action
        s1 = DataLoader(file_path)
        s2 = DataLoader(file_path)
        # Assert:
        self.assertEqual(s1,s2)

if __name__ == '__main__':
    unittest.main()
    
