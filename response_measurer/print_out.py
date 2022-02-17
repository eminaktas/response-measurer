import csv
import logging

# TODO: Define different output methods


class PrintOut:
    def __init__(self):
        """
        TODO: fill here
        """

    @staticmethod
    def extract_headers(datas):
        return list(datas.keys())


class PrintCsv(PrintOut):
    def __init__(self):
        super(PrintCsv, self).__init__()

    @staticmethod
    def print(datas):
        field_names = PrintOut.extract_headers(datas)
        with open('hede.csv', 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            datas_list = [datas]
            writer.writerows(datas_list)
        logging.info("Result is printed as CSV file")


class PrintTerminal(PrintOut):
    def __init__(self):
        super(PrintTerminal, self).__init__()

    @staticmethod
    def print(datas):
        logging.info(f"{datas}")
