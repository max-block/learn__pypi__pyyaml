import yaml

str_data = """ 
line 1

line 2

...
"""

str_data2 = """
key: |
    line 1
    line 2
...
"""


res = yaml.full_load(str_data)
print(res, type(res))


res = yaml.full_load(str_data2)
print(res, type(res))
