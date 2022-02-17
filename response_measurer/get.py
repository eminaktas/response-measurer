import requests
import logging
from response_measurer.methods import Methods


class Get(Methods):
    def __init__(self):
        super(Get, self).__init__()

    @staticmethod
    def send_request(parameters: dict):
        logging.warning("GET method is not implemented")
        exit(1)
        try:
            logging.debug("GET request started")
            values_list = []
            for i in range(parameters["loop_count"]):
                # TODO: To be done
                print("TODO")
            logging.debug("GET request finished")
            return Methods.calculate(values_list)
        except Exception as e:
            logging.error(e)
            exit(1)
