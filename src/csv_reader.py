import csv


class CsvReader:
    def read_csv_data(self, file_path):
        """Read CSV data from file path"""
        data = []

        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        return data
