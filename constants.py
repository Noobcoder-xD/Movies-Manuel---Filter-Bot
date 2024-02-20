
from os import environ
from constants import API_ID
from logging import basicConfig, INFO, StreamHandler, getLogger, WARNING, Logger
from logging.handlers import RotatingFileHandler
from script import StartTxT, HelpTxT, AboutTxT

basicConfig(
    level=INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler("filtersbot.txt", maxBytes=50000000, backupCount=10),
        StreamHandler()
    ]
)
