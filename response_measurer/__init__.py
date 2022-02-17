import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

version = "0.2.0"
