from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def register_subscriber(self, subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber):
        pass

    @abstractmethod
    def notify_subscriber(self):
        pass


class WeatherStatisticsStream(Publisher):
    def __init__(self):
        self.subscribers = []
        self.temperatureMin = None
        self.temperatureMax = None
        self.temperatureMean = None

    def set_stats(self, temperatureMin, temperatureMax, temperatureMean):
        self.temperatureMin = temperatureMin
        self.temperatureMax = temperatureMax
        self.temperatureMean = temperatureMean

    def register_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
        else:
            print(f"Subscriber{subscriber} already exists")

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscriber(self):
        for subscriber in self.subscribers:
            subscriber.update(self.temperatureMin, self.temperatureMax, self.temperatureMean)




