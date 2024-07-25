
class ConsoleSubscriber:
    def update(self, temperatureMin, temperatureMax, temperatureMean):
        print(f"Minimum Temperature: {temperatureMin}F,\
              Maximum Temperature:{temperatureMax}F,\
              Average Temperature: {temperatureMean}F")


class FileSubscriber:
    def update(self, message):
        with open("logger_subscriber.txt", "a") as f:
            f.write(f"{message}\n")
