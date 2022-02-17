import logging
import argparse

from response_measurer.post import Post
from response_measurer.get import Get
from response_measurer.print_out import *
from response_measurer import version


class Run:
    def __init__(self, _parameters):
        self.parameters = _parameters

        self.post_method = Post()
        self.get_method = Get()

        self.method_map = {
            "post": self.post_method,
            "get": self.get_method,
        }

        self.print_csv = PrintCsv
        self.print_terminal = PrintTerminal

        self.print_map = {
            "csv": self.print_csv,
            "print": self.print_terminal
        }

    def run(self):
        logging.info("response_measurer started")
        # Start the benchmark
        var = self.method_map[self.parameters["request_type"]].send_request(self.parameters)
        # Get the calculated results and print
        self.print_map[self.parameters["output"]].print(var)


def parse_args():
    # BASE PARSER
    argument_parser = argparse.ArgumentParser(description='A simple python HTTP request response measurer')
    argument_parser.add_argument('--version', action='version', version=version)
    argument_parser.add_argument('--host', dest='host', required=True, type=str,
                                 help='Enter a host')
    argument_parser.add_argument('--loop-count', dest='loop_count', required=False, type=int,
                                 default=1, help='Enter a loop count which repeats the requests given number'
                                                 'Default value is 1')
    argument_parser.add_argument('--timeout', dest='timeout', required=False, default=60,
                                 type=float, help='Enter a timeout. Default value is 60 seconds')
    argument_parser.add_argument('--output', dest='output', required=False, type=str, default='print',
                                 help='Output format. Supports: print|csv')
    argument_parser.add_argument('--log-level', dest='log_level', required=False, default='INFO', type=str,
                                 help='Define log level [INFO,DEBUG,WARN,WARNING,CRITICAL,ERROR,FATAL]. '
                                      'Default is INFO')

    # SUB PARSER
    sub_argument_parsers = argument_parser.add_subparsers(
        help='Enter request type. Supported requests: post', dest='request_type')

    # POST PARSER
    post_parser = sub_argument_parsers.add_parser('post')
    post_parser.add_argument('--data', dest='data', required=False, default='',
                             help='Define a data for POST request. Default is empty-string ""')

    # GET PARSER
    get_parser = sub_argument_parsers.add_parser('get')

    args = vars(argument_parser.parse_args())
    return args


def get_log_level(_log_level: str):
    numeric_level = getattr(logging, _log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {_log_level}")
    return numeric_level


if __name__ == '__main__':
    parameters = parse_args()
    log_level = get_log_level(parameters["log_level"])
    # Configure logging
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    Run(parameters).run()
