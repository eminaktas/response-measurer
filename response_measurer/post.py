import requests
import logging
from response_measurer.calculaters import *


class Post:
    def __init__(self, parameters: dict):
        self.parameters = parameters

    def send_post_request(self):
        try:
            values_list = []
            for i in range(self.parameters["loop_count"]):
                response = requests.post(
                    self.parameters["host"],
                    data=self.parameters["data"],
                    timeout=self.parameters["timeout"]
                )
                values_list.append(response.elapsed.total_seconds())
            return values_list
        except Exception as e:
            logging.error(e)
            exit(1)

    def run(self):
        values = self.send_post_request()
        # Calculate mean
        mean = calculate_mean(values)
        logging.info(f"Mean of the POST requests: {mean:.5f}")
        # Percentile %50
        p50 = calculate_percentile(values, 0.5)
        logging.info(f"Percentile %50 of the POST requests: {p50:.5f}")
        p99 = calculate_percentile(values, 0.99)
        logging.info(f"Percentile %99 of the POST requests: {p99:.5f}")
