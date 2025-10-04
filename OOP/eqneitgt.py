class Clock:
    __DAY = 86400

    def __init__(self,seconds: int):
        if not isinstance(seconds,int):
            raise ValueError('Not int')
        self.seconds = seconds% self.__DAY

    @classmethod
    def verify_data(cls,other):
        if not isinstance(other, (int,Clock)):
            raise ValueError('Not int or Clock')

        return other.seconds if isinstance(other,Clock) else other

    def __eq__(self, other):
        sc = self.verify_data(other)

        return self.seconds == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.verify_data(other)
        return self.seconds <= sc

    def __ge__(self, other):
        sc = self.verify_data(other)
        return self.seconds >= sc

cl = Clock(2000)
cl2 = Clock(3000)

print(cl >= cl2)