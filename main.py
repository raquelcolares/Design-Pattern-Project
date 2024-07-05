from src.data_loader import DataLoader
from src.data_processor import DataProcessor
from src.data_analyzer import DataAnalyzer
from src.data_types import DataType

if __name__ == "__main__":
    
    loader=DataLoader("data\weather_classification_data.csv")
    data = loader.load_data()
    print(data)