# in order to be recognized as a module must have a __init__.py file
# https://docs.python.org/3.8/library/__main__.html
import logging

from .constants import LOGGING_DIR

logging.basicConfig(filename=LOGGING_DIR, filemode="w", level=logging.DEBUG)
