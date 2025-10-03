class Cat:
    def __init__(self):
        self.name = 'Vasya'
        self.age = 1000


    def __repr__(self):
        return f'{self.__class__}:{self.name}'

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __abs__(self):
        return abs(self.age)


cat = Cat()
print(len(cat))
print(abs(cat))