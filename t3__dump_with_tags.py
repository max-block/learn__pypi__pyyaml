import yaml

data = {"a": 1, "b": "bla", "c": True}

res = yaml.dump(data, default_style="'")
print(res)
# 'a': !!int '1'
# 'b': 'bla'
# 'c': !!bool 'true'
