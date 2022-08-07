import os

from dotenv import load_dotenv

load_dotenv()

# REVIEW: things like port and local host should be saved as ENV variables
PORT = int(os.environ.get("PORT"))
HOST = os.environ.get("HOST")

## ROUTES
STATIC_ROUTE = "/static"
ROOT = "/"
WEBSOCKET_ROUTE = "/ws"

# REVIEW: all constants should be in all caps.
# REVIEW: filepaths should be relative unless set a the environment level
STATIC_DIR = "static"
LOGGING_DIR = "./logs/logs.log"
TEMPLATES_DIR = "templates"
BYTES_IN_GB = 1073741824
