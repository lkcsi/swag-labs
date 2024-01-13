import json
import os


def users():
    return _load_json('params/users.json')


def items():
    return _load_json('params/items.json')


def params_from_file(filename):
    res = []
    for item in _load_json(filename):
        res.append((item['username'], item['password']))
    return res


def _load_json(file):
    with open(file, 'r') as fh:
        return json.loads(fh.read())
