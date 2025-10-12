from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


    def __repr__(self):
        return f"Thing: {self.__dict__}"



@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    lst: list = field(default_factory=list)


t = Thing('name',20,300)
td = ThingData('name',20,300)

print(td)