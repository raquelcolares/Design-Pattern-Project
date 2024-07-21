from abc import ABC, abstractmethod


class LoggerOutputAdapter(ABC):
    @abstractmethod
    def write(self, message):
        pass


class ConsoleAdapter(LoggerOutputAdapter):
    def write(self, message):
        print(message)


class FileAdapter(LoggerOutputAdapter):
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        with open(self.filename, "a") as f:
            f.write(message + "\n")


class MyLogger:
    def __init__(self, name, level="INFO", adapter=None):
        self.name = name
        self.level = level.upper()
        if adapter:
            self.adapter = adapter
        else:
            self.adapter = ConsoleAdapter()

    def _format_message(self, message, level):
        return f"[{level}] {self.name}: {message}"

    def debug(self, message):
        self.adapter.write(self._format_message(message, "DEBUG"))

    def info(self, message):
        self.adapter.write(self._format_message(message, "INFO"))

    def warning(self, message):
        self.adapter.write(self._format_message(message, "WARNING"))

    def error(self, message):
        self.adapter.write(self._format_message(message, "ERROR"))

    def fatal(self, message):
        self.adapter.write(self._format_message(message, "FATAL"))
    
    def trace(self, message):
        self.adapter.write(self._format_message(message, "TRACE")) 

    def set_level(self, level):
        self.level = level.upper()

    def set_adapter(self, adapter):
        self.adapter = adapter

