from src.data_loader import DataLoader, CsvAdapter, JsonAdapter, AdaptorFactory
from src.data_processor import DataProcessor
from src.data_analyzer import DataAnalyzer
from src.data_model import DataModel
from src.weather_statistics_stream import Publisher, WeatherStatisticsStream
from src.subscribers import ConsoleSubscriber, FileSubscriber
from src.logger import MyLogger
import pandas as pd


if __name__ == "__main__":

    # Initializing logger instance 
    log = MyLogger("Logger")
    warning_sub1 = FileSubscriber()
    log.register_WarningSubscriber(warning_sub1)


    # Loading and reading the dataset
    print("\n---------- Weather Dataset ----------")
    file_path = "data\weather_classification_data.csv"
    adapter = AdaptorFactory().get_adapter(file_path)
    data= adapter.load_data(file_path)
    print(data.head())  # shows the 5 first rows of the file 


    # DATA ANALYSIS
    ## Analysing the Descriptive statistics
    print("\n---------- Descriptive Statistics ----------")
    analyser = DataAnalyzer(data)
    stats = analyser.get_summary_statistics()
    print(stats)

    ## Analysing the amount of columns and rows
    print("\n---------- Dataset Shape ----------")
    shape = analyser.dataset_shape()
    print(shape)

    ## Analysing missing values for all features
    print("\n---------- Missing Values ----------")
    missing_values = analyser.missing_values()
    print(missing_values)

    ## Ploting the data distribution
    print("\n---------- Data Distribution Visualization ----------")
    analyser.plot_data()


    # DATA PREPROCESSING
    ## Treating missing values
    print("\n---------- Data Cleaning ----------")
    processor = DataProcessor(data)
    data_clean = processor.clean_data()
    print(data_clean)

    ## Transforming object type in numerical
    print("\n---------- Dataset Transformation ----------")
    data_transformed = processor.transform_data()
    print(data_transformed)


    # NEURAL NETWORK MODEL
    ## Creating the scaler
    print("\n---------- Scaler ----------")
    data_model_obj = DataModel(data_transformed, log)
    data_scaler = data_model_obj.scaler()
    print(data_scaler)

    ## Separating the dataset in train and test
    print("\n---------- Train Test Split ----------")
    train_test_split = data_model_obj.train_test_split()

    ## Analyzing the accuracy of the model
    print("\n---------- Evaluation ----------")
    data_model_obj.evaluation_metrics()

    ## Visualizing the Loss Curve
    print("\n---------- Loss Curve ----------")
    data_model_obj.loss_curve()


    # PUBLISHER / SUBSCRIBER
    ## Publisher
    pub = WeatherStatisticsStream()
    ## Subscriber
    sub1 = ConsoleSubscriber()
    sub2 = ConsoleSubscriber()
    ## Registering subscriber
    pub.register_subscriber(sub1)
    pub.register_subscriber(sub2)
    ## Getting the statistics to be publish
    print("\n---------- Weather Temperature Publisher ----------")
    tempMin, temMax, tempMean = analyser.temperature_stats()
    pub.set_stats(tempMin, temMax, tempMean)
    pub.notify_subscriber()

    
