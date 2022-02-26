import random

import requests
import logging
from response_measurer.methods import Methods


class Post(Methods):
    def __init__(
        self,
        host: str,
        timeout: float,
        loop_count: int,
        _bytes: int = None,
        seed: int = None,
    ):
        super(Post, self).__init__(host, timeout, loop_count)
        self.bytes = _bytes
        self.seed = seed

    def generate_random_bytes(self):
        # Ref: https://github.com/postmanlabs/httpbin/blob/master/httpbin/core.py#L1423
        n = min(self.bytes, 1000 * 1024)  # set 100KB limit

        if self.seed:
            random.seed(self.seed)

        return bytearray(random.randint(0, 255) for i in range(n))

    def send_request(self):
        try:
            logging.debug("POST request started")
            results = []
            all_results = []
            for i in range(self.loop_count):
                response = requests.post(
                    self.host,
                    data=self.generate_random_bytes() if self.bytes else None,
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
