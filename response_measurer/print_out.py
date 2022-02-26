import csv
import logging
import os

from datetime import datetime


class PrintOut:
    def __init__(self, method):
        self.method = method
        self.time = datetime.now().isoformat()

    def extract_headers(self, datas: dict):
        return list(datas.keys())

    def get_metadata(self, no_time: bool = False):
        return {
            "time": self.time if not no_time else None,
            "name": self.generate_name(),
            "method": self.method,
        }

    def generate_name(self):
        return f"random-string-{self.method}"

    def merge_listed_dict_with_metadata(self, datas: list) -> list:
        merged_data = []

        # Check if data has time already.
        no_time = False
        if datas[0].get("time"):
            no_time = True
        metadata = self.get_metadata(no_time)

        for data in datas:
            _datas = metadata.copy()
            _datas.update(data)
            merged_data.append(_datas)
        return merged_data


class PrintCsv(PrintOut):
    def __init__(self, method):
        super(PrintCsv, self).__init__(method)

    def print(self, calculated_results: list, all_results: list):
        for result in (calculated_results, all_results):
            if result[0].get("time"):
                result_type = "all-results"
            else:
                result_type = "calculated-results"

            _datas = self.merge_listed_dict_with_metadata(result)

            field_names = self.extract_headers(_datas[0])

            file_name = (
                f"{os.getcwd()}/{self.method.lower()}-request-{self.time}-{result_type}"
            )

            with open(file_name, "w", encoding="UTF8") as f:
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                datas_list = _datas
                writer.writerows(datas_list)

            logging.info("Result is printed as CSV file")


class PrintTerminal(PrintOut):
    def __init__(self, method):
        super(PrintTerminal, self).__init__(method)

    def print(self, calculated_results: list, all_results: list):
        for result in (calculated_results, all_results):
            _datas = self.merge_listed_dict_with_metadata(result)
            print(f"{_datas}")
