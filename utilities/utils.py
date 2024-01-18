import inspect
import logging
import json



def file_logger(log_level=logging.INFO):

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    file_handler = logging.FileHandler("../test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

def params_from_json(filename):
    with open(filename, "r") as fh:
        data = json.loads(fh.read())
        return [tuple(item.values()) for item in data]
