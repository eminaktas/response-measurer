import requests
import logging
from response_measurer.methods import Methods


class Get(Methods):
    def __init__(self, host: str, timeout: float, loop_count: int):
        super(Get, self).__init__(host, timeout, loop_count)

    def send_request(self):
        try:
            logging.debug("GET request started")
            results = []
            all_results = []
            for i in range(self.loop_count):
                response = requests.get(
                    self.host,
                    timeout=self.timeout,
                )
                result = response.elapsed.total_seconds()
                all_results.append({"time": self.time(), "result": result})
                results.append(result)
            logging.debug("POST request finished")
            return self.calculate(results), all_results
        except Exception as e:
            logging.error(e)
            exit(1)
