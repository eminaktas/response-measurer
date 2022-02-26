import abc

from datetime import datetime
from response_measurer.calculaters import calculate_mean, calculate_percentile


class Methods:
    def __init__(self, host: str, timeout: float, loop_count: int):
        self.host = host
        self.timeout = timeout
        self.loop_count = loop_count

    @abc.abstractmethod
    def send_request(self):
        """
        Implements the HTTP request based on the type
        :return: numerical list
        """

    @staticmethod
    def time():
        return datetime.now().isoformat()

    @staticmethod
    def calculate(values):
        values_list = []
        values_dict = {}
        # Calculate mean
        mean = calculate_mean(values)
        values_dict.update({"mean": mean})
        # Percentile %50
        p50 = calculate_percentile(values, 0.5)
        values_dict.update({"P50": p50})
        # Percentile %99
        p99 = calculate_percentile(values, 0.99)
        values_dict.update({"P99": p99})
        values_list.append(values_dict)
        return values_list
