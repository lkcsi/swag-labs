import json

def params_from_file(file):
    with open(file, 'r') as fh:
        json_res = json.loads(fh.read())
        res = []
        for user in json_res:
            res.append([user['user'], user['pwd']])
        return res