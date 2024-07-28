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

The classes below illustrate the project scope before the use of Design Patterns.

<p align="center">
    <img width="900" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Project-Scope.png">
</p>


### Diagrams after applying Design Patterns


<p align="center">
    <img width="800" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Singleton-Adaptor-Factory.png">
</p>


<p align="center">
    <img width="700" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Observer.png">
</p>


<p align="center">
    <img width="900" src="https://github.com/raquelcolares/Design-Pattern-Project/blob/main/pictures-diagrams-project/Logger.png">
</p>


### References: 

Dataset - https://www.kaggle.com/datasets/nikhil7280/weather-type-classification/data

The Catalog of Design Patterns - https://refactoring.guru/design-patterns/catalog

Design Patterns course material - LaSalle College

