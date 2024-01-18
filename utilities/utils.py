import inspect
import logging
import json
from base.element import Item


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
        result = []
        data = json.loads(fh.read())
        for item in data:
            values = item.values()
            if len(values) == 1:
                result.append(list(values)[0])
            else:
                result.append(tuple(values))
        return result


def convert_price_tag_to_float(text: str) -> float:
    text = text.split("$")[1]
    return float(text)


def sum_price_of_items(items: [Item]):
    return sum(i.price for i in items)
