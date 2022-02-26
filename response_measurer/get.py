import requests
import logging
from response_measurer.methods import Methods


class Get(Methods):
    def __init__(self, host: str, data: str, timeout: float, loop_count: int):
        super(Get, self).__init__(host, data, timeout, loop_count)

    def send_request(self):
        logging.warning("GET method is not implemented")
        exit(1)
