import abc
import requests
import logging
from response_measurer.calculaters import *


class Methods:
    def __init__(self):
        """
        TODO: fill here
        """

    @staticmethod
    @abc.abstractmethod
    def send_request(parameters: dict):
        """
        Implements the HTTP request based on the type
        :return: numerical list
        """

    @staticmethod
    def calculate(values):
        # For now, we are just calculating values for one row.
        # values_list = []
        values_dict = {}
        # Calculate mean
        mean = calculate_mean(values)
        values_dict.update(
            {
                "mean": mean
            }
        )
        # Percentile %50
        p50 = calculate_percentile(values, 0.5)
        values_dict.update(
            {
                "P50": p50
            }
        )
        # Percentile %99
        p99 = calculate_percentile(values, 0.99)
        values_dict.update(
            {
                "P99": p99
            }
        )
        return values_dict
