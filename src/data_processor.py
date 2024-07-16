import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def clean_data(self):
        data = self.data.dropna()
        return data.isna().sum()

    def transform_data(self):
        # To transform categorical data into numerical values for the Neural Networks model
        ## Creating a column for the name of the targets
        self.data["target_name"] = self.data["Weather Type"]
        ## Transforming the label
        self.data["Weather Type"] = np.where(self.data["Weather Type"]=="Rainy",0, self.data["Weather Type"])
        self.data["Weather Type"] = np.where(self.data["Weather Type"]=="Cloudy",1, self.data["Weather Type"])
        self.data["Weather Type"] = np.where(self.data["Weather Type"]=="Sunny",2, self.data["Weather Type"])
        self.data["Weather Type"] = np.where(self.data["Weather Type"]=="Snowy",3, self.data["Weather Type"])
        self.data = self.data.astype({"Weather Type": int})
        ## One-hot-encoding for the other categorical features
        categorical_features = ["Cloud Cover", "Season", "Location"]
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        matrix = encoder.fit_transform(self.data[categorical_features])
        encoder_feature_names = encoder.get_feature_names_out()
        df_encoded = pd.DataFrame(data=matrix, columns=encoder_feature_names)
        self.data = pd.merge(self.data, df_encoded, left_index=True, right_index=True)
        self.data.drop(columns=categorical_features, inplace=True)

        return self.data

