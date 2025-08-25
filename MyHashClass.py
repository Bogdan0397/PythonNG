class Hashlist:
    def __init__(self,data: list[int]):
        self.data = data

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data

        return False

    def __hash__(self):
        return hash(sum(self.data))

    def __str__(self):
        return str(self.data)


l1 = Hashlist([1,2,3])
l2 = Hashlist([5,1,0])
print(dir(l1))

