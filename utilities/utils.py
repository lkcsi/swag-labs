import json
from pages.elements import Item


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
