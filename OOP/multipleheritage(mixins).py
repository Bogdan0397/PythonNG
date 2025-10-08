class Goods:
    def __init__(self, name, weight,price):
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price


    def print_info(self):
        print(f'{self.name},{self.weight},{self.price}')





class MixinLog:
    ID = 0

    def __init__(self):
        print('Init MixinLog')
        self.ID +=1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: Sold at 00:00')

    def print_info(self):
        print('Print_info mixinlog')

class Notebook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)


nout = Notebook('Acer', 2,500)
nout.print_info()
nout.save_sell_log()