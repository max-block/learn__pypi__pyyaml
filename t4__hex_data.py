import yaml

data_str = """
f1: 0x123 # it's not a string! 
f2: "0x123"
"""

res = yaml.full_load(data_str)
print(res)
# {'f1': 291, 'f2': '0x123'}
