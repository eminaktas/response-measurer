import logging
import argparse

from response_measurer.post import Post
from response_measurer.get import Get
from response_measurer.print_out import PrintCsv, PrintTerminal
from response_measurer import version


class Run:
    def __init__(self, _parameters):
        self.requests_type = _parameters["request_type"]
        self.host = _parameters["host"]
        self.output = _parameters["output"]
        self.timeout = _parameters["timeout"]
        self.loop_count = _parameters["loop_count"]

        self.post_method = Post(
            self.host,
            self.timeout,
            self.loop_count,
            _parameters.get("bytes", None),
            _parameters.get("seed", None),
        )
        self.get_method = Get(
            self.host,
            self.timeout,
            self.loop_count,
        )

        self.method_map = {
            "post": self.post_method,
            "get": self.get_method,
        }

        self.print_csv = PrintCsv(
            self.requests_type,
        )
        self.print_terminal = PrintTerminal(
            self.requests_type,
        )

        self.print_map = {"csv": self.print_csv, "print": self.print_terminal}

    def run(self):
        logging.info("response_measurer started")
        # Start the benchmark
        calculated_results, all_results = self.method_map[
            self.requests_type
        ].send_request()
        # Get the calculated results and print
        self.print_map[self.output].print(calculated_results, all_results)


def parse_args():
    # BASE PARSER
    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument("host", type=str, help="enter a host")
    base_parser.add_argument(
        "--loop-count",
        dest="loop_count",
        required=False,
        type=int,
        default=1,
        help="enter a loop count which repeats the requests given number "
        "(default: 1)",
    )
    base_parser.add_argument(
        "--timeout",
        dest="timeout",
        required=False,
        default=60,
        type=float,
        help="enter a timeout (default: 60 (secs))",
    )
    base_parser.add_argument(
        "--output",
        dest="output",
        required=False,
        type=str,
        default="print",
        help="enter an output method (supported methods: print, csv) (default: print)",
    )
    base_parser.add_argument(
        "--log-level",
        dest="log_level",
        required=False,
        default=None,
        type=str,
        help="define a log level (info,debug,warn,warning,critical,error,fatal)",
    )

    argument_parser = argparse.ArgumentParser(
        description="a HTTP request response measurer"
    )
    argument_parser.add_argument("--version", action="version", version=version)

    # SUB PARSER
    sub_argument_parsers = argument_parser.add_subparsers(
        help="enter a request method",
        dest="request_type",
        description="run one of the HTTP methods",
    )

    # POST PARSER
    post_parser = sub_argument_parsers.add_parser("post", parents=[base_parser])
    post_parser.description = "post method"
    post_parser.add_argument(
        "--bytes",
        dest="bytes",
        required=False,
        type=int,
        help="enter a integer value which sends n number of bytes generated w/o seed",
    )
    post_parser.add_argument(
        "--seed",
        dest="seed",
        required=False,
        type=int,
        help="enter a integer value which generates same data for the same seed value "
        "(default: generates random data each run)",
    )

    # GET PARSER
    get_parser = sub_argument_parsers.add_parser("get", parents=[base_parser])
    get_parser.description = "get method"

    args = vars(argument_parser.parse_args())
    return args


def set_log_settings(_log_level: str):
    def get_log_level():
        numeric_level = getattr(logging, _log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f"Invalid log level: {_log_level}")
        return numeric_level

    log_level = None
    if _log_level:
        log_level = get_log_level()
    if _log_level == "INFO":
        _format = "%(asctime)s: %(message)s"
    else:
        _format = "%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s"
    # Configure logging
    logging.basicConfig(level=log_level, format=_format, datefmt="%Y-%m-%d %H:%M:%S")


def main():
    _parameters = parse_args()
    set_log_settings(_parameters.get("log_level"))
    Run(_parameters).run()
