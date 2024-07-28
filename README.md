# Design Patterns Project

#### Raquel Colares Santos
#### Joao Vitor Peluzo Cardoso

---------------------------------------------------------------

This project was designed to load, process, analyze multiple types of data
from a single CSV file, and create a classification Neural Network Model, utilizing different classes and different design patterns.

*   Github repository - https://github.com/raquelcolares/Design-Pattern-Project



**Project Phase 1:**

Create a logging system where the log output can be easily redirected to specific output formats (console, file, etc.) and ensure that the logging configuration and handling are managed via a single instance (singleton).

**Project Phase 2:**

Extend the system where the output of the logger can be adapted to various formats (like console output, file output, or even a hypothetical network output).

**Project Phase 3:**

Extend the logging system to notify subscribed observers whenever a logging event occurs. This will allow multiple parts of the application to react to logs dynamically.
 


### Libraries required for this project:

*   ABC
*   Pathlib
*   Pandas
*   Numpy
*   Matplotlib
*   Seaborn
*   Sklearn
*   Streamlit
*   Pickle
*   Unittest


### Diagrams before applying Design Patterns

The classes of the project scope below, is illustrating the system prior to implementing Design Patterns.
The project has four classes, that together are responsable to open, analyze, process the data and implement a classification Neural Networks Model, which predicts four types of weather; cloudy, rainy, snowy and sunny.

<p align="center">
    <img width="900" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Project-Scope.png">
</p>



### Diagrams after applying Design Patterns

On this project, it implements the designs Singleton, Adaptor, Factory and Observer. The purpose of implementing Design Pattern is, to solve a problem that occurs many times in a way that the solution can be reused, saving time and money. 

* Singleton, Adaptor and Factory Patterns

The class DataLoader is responsable for loading the dataset that will be used by other classes for the classification of the weather. However, the DataLoader previously implemented on the project scope was recognizing only a csv format.

On a context that the dataset could be provided in many formats, and to allow the DataLoader class to work with it, the use of the Adaptor design pattern make it feasible. 

For this project it will be considered two formats, csv and json. The system was already created for the csv format, then an interface was created to give the same access for opening both formats. 

Complementary to the Adaptor, it was created the Factory design which will be responsable for deciding which object to initiate (or the csv or json) based on the file format. 

As the AdaptorFactory class is responsible for the creation of the object, the Singleton pattern is then applied to this class for ensuring only one instance of this object could exist, and also to avoid the creation of multiple objects and for control resources. 


<p align="center">
    <img width="800" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Singleton-Adaptor-Factory.png">
</p>


* Observer Pattern

The purpose of the Observer design pattern applied to this project, is to notify the registered subscribers (observers), to receive updates of the temperature statistics, like minimum, maximum and average temperature. 

The class WeatherStatisticsStream implements the publisher aspect of the observer pattern. It is composed of four methods: set_stats, register_subscriber, remove_subscriber and notify_subscriber. 

The set_stats is reponsible for initializing the temperature datas to be published. The register_subscriber is used for adding the subscriber to the list of subscribers that will be notified, by the notify_subscriber method. In additon, the remove_subscriber method can be used for removing an especific subscriber from the list.  

The ConsoleSubscriber class implements the subscriber aspect of the pattern. It has the method update, which keeps the subscribers aware of each notificiation made. 


<p align="center">
    <img width="650" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Observer.png">
</p>


* Logger

The MyLogger class is implementing a logger functionality, which records messages in a console or a file, using the adaptor attribute. There is many types of level messages; as info, debug, warning, error, fatal, and trace. 

Morever, the MyLogger class, has the capability of managing a list of subscribers to notify them of error or warning messages. 

The class FileSubscriber implements the subscriber to the list of WarningSubscribers or ErrorSubscribers. It has an update method that records the messages to a file. 


<p align="center">
    <img width="900" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Logger.png">
</p>


### Unit testing

It was implemented six unit test on this project that can be found on the file tests. 
The unit tests are separating in three classes: the class TestSingletonDataLoader to test the singleton pattern, the class TestAdapters for the adaptor and factory, and the class TestLogger to verify functions to write messages on a console, a file and the subscribers functionalities. 



### References: 

Dataset - https://www.kaggle.com/datasets/nikhil7280/weather-type-classification/data

The Catalog of Design Patterns - https://refactoring.guru/design-patterns/catalog

Design Patterns course material - LaSalle College

