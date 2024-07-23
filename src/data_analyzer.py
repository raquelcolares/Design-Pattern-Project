import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
    
    def get_summary_statistics(self):
        return self.data.describe()
    
    def temperature_stats(self):
        temp_stats = self.data["Temperature"].describe()
        return temp_stats["min"], temp_stats["max"], temp_stats["mean"]
    
    def dataset_shape(self):
        return self.data.shape
    
    def missing_values(self):
        return self.data.isna().sum()
    
    def plot_data(self):
        plt.figure(figsize=(20, 15))
        for i, col in enumerate(self.data.columns,1):
            plt.subplot(4, 3, i)
            sns.histplot(x=self.data[col], bins=10, kde=True, color='green')
            plt.title(col)
        plt.show()