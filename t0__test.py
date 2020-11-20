import yaml

data_str = """
private_key: 0x123 # it
"""

res = yaml.full_load(data_str)
print(res, type(res))
