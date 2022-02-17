import requests
import logging
from response_measurer.methods import Methods


class Post(Methods):
    def __init__(self):
        super(Post, self).__init__()

    @staticmethod
    def send_request(parameters: dict):
        try:
            logging.debug("POST request started")
            values_list = []
            for i in range(parameters["loop_count"]):
                response = requests.post(
                    parameters["host"],
                    data=parameters["data"],
                    timeout=parameters["timeout"]
                )
                values_list.append(response.elapsed.total_seconds())
            logging.debug("POST request finished")
            return Methods.calculate(values_list)
        except Exception as e:
            logging.error(e)
            exit(1)
