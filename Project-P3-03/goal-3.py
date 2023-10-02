import json
from collections import ChainMap

dev = json.load(open('dev.json'))
prod = json.load(open('prod.json'))
common = json.load(open('common.json'))


def combine(env):
    return ChainMap(env, common)


print(combine(prod).get("logs")['level'])