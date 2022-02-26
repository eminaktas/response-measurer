import requests
import logging
from response_measurer.methods import Methods


class Post(Methods):
    def __init__(self, host: str, data: str, timeout: float, loop_count: int):
        super(Post, self).__init__(host, data, timeout, loop_count)

    def send_request(self):
        try:
            logging.debug("POST request started")
            results = []
            all_results = []
            for i in range(self.loop_count):
                response = requests.post(
                    self.host,
                    data=self.data,
                    timeout=self.timeout
                )
                result = response.elapsed.total_seconds()
                all_results.append(
                    {
                        "time": self.time(),
                        "result": result
                    }
                )
                results.append(result)
            logging.debug("POST request finished")
            return Methods.calculate(results), all_results
        except Exception as e:
            logging.error(e)
            exit(1)
