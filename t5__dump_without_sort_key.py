import yaml

data = {"a": 1, "z": 2, "b": 3}

print(yaml.dump(data))
# a: 1
# b: 3
# z: 2


print(yaml.dump(data, sort_keys=False))
# a: 1
# z: 2
# b: 3
