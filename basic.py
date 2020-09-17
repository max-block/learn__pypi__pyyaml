from datetime import datetime

import yaml


def parse_yaml():
    data = """
    a: 1
    b: bla bla
    c: 2019-12-23 09:33:25.943138
    d:
    - 1
    - 2
    - 3
    - 4
    e: true
    f: null
    """
    res = yaml.full_load(data)
    print(res)
    # {'a': 1, 'b': 'bla bla', 'c': datetime.datetime(2019, 12, 23, 9, 33, 25, 943138), 'd': [1, 2, 3, 4], 'e': True, 'f': None} # noqa


def dump_yaml():
    data = {
        "a": 1,
        "b": "bla bla",
        "c": datetime.now(),
        "d": [1, 2, 3, 4],
        "e": True,
        "f": None,
    }
    res = yaml.dump(data)
    print(res)
    # a: 1
    # b: bla
    # bla
    # c: 2019 - 12 - 23
    # 0
    # 9: 34:50.598645
    # d:
    # - 1
    # - 2
    # - 3
    # - 4
    # e: true
    # f: null


if __name__ == "__main__":
    parse_yaml()
    dump_yaml()
