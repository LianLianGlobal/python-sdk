import json
import time


def timestamp():
    return str(round(time.time() * 1000))


def object_to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=False)
