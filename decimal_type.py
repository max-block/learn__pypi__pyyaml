from decimal import Decimal

import yaml


def decimal_representer(dumper, data):
    return dumper.represent_scalar("!decimal", str(data))


def decimal_constructor(loader, node):
    return Decimal(node.value)


yaml.add_representer(Decimal, decimal_representer)
yaml.add_constructor("!decimal", decimal_constructor)

# dump decimal
data1 = Decimal("0.33")
res = yaml.dump(data1, default_style='"')
print(res)  # !decimal "0.33"

data2 = {"a": Decimal("0.33")}
res = yaml.dump(data2, default_style='"')
print(res)  # "a": !decimal "0.33"

data3 = {"a": [Decimal("0.31"), Decimal("0.32"), Decimal("0.33")]}
res = yaml.dump(data3, default_style='"')
print(res)
# "a":
# - !decimal "0.31"
# - !decimal "0.32"
# - !decimal "0.33"
