import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt



class DataModel:
    
    X_train= pd.DataFrame()
    X_test= pd.DataFrame()
    y_train= pd.DataFrame()
    y_test= pd.DataFrame()

    def __init__(self, data, logger):
        self.data = data
        self.logger = logger
  
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def scaler(self):
        columns_to_scale = ["Temperature", "Humidity", "Wind Speed", "Precipitation (%)", 
                            "Atmospheric Pressure", "UV Index", "Visibility (km)"]
        scaler = StandardScaler()
        self.data[columns_to_scale] = scaler.fit_transform(self.data[columns_to_scale])
        return self.data

    def train_test_split(self):
        X = self.data.drop(columns=["Weather Type", "target_name"])
        y = self.data["target_name"]
        DataModel.X_train, DataModel.X_test, DataModel.y_train, DataModel.y_test = train_test_split(X,y, test_size=0.20, random_state=42)
        print(DataModel.X_train.shape, DataModel.X_test.shape) 
        return DataModel.X_train, DataModel.X_test, DataModel.y_train, DataModel.y_test

    def neural_network_model():
        model = MLPClassifier(
            random_state=42,
            max_iter=1000,
            hidden_layer_sizes=(100, 50, 30,),
            n_iter_no_change=100,
            early_stopping=True, 
            verbose=False)
        model.fit(DataModel.X_train, DataModel.y_train)
        return model

    def evaluation_metrics(self):
        self.logger.warning("Evaluation of the Neural Network Model in progress...")
        model_fit = DataModel.neural_network_model()
        print(f"Test accuracy: {model_fit.score(DataModel.X_test, DataModel.y_test)}")
        print(f"Train accuracy: {model_fit.score(DataModel.X_train, DataModel.y_train)}")

    def loss_curve(self):
        self.logger.warning("Calculation of the loss function in progress...")
        loss_curve = DataModel.neural_network_model().loss_curve_
        plt.plot(loss_curve)
        plt.show()