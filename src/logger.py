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


class LoggerAdapter:
    def __init__(self, logger, adapter: LoggerOutputAdapter = ConsoleAdapter()):
        self.logger = logger
        self.adapter = adapter

    def log(self, message, level="INFO"):
        formatted_message = f"{level} - {message}"
        self.adapter.write(formatted_message)


class MyLogger:
    def __init__(self, name, level="INFO"):
        self.name = name
        self.level = level

    def _format_message(self, message, level):
        return f"[{level}] {self.name}: {message}"

    def debug(self, message):
        if self.level in ["DEBUG"]:
            self.adapter.write(self._format_message(message, "DEBUG"))

    def info(self, message):
        if self.level in ["DEBUG", "INFO"]:
            self.adapter.write(self._format_message(message, "INFO"))

    def warning(self, message):
        if self.level in ["DEBUG", "INFO", "WARNING"]:
            self.adapter.write(self._format_message(message, "WARNING"))

    def error(self, message):
        self.adapter.write(self._format_message(message, "ERROR"))

    def critical(self, message):
        self.adapter.write(self._format_message(message, "CRITICAL"))

    def set_level(self, level):
        self.level = level.upper()

    def set_adapter(self, adapter):
        self.adapter = adapter
