class expense:
    def __init__(self,desc,catog,price):
        self.desc = desc
        self.catog = catog
        self.price = price

class expenses:
    def __init__(self):
        self.all = []

    def add(self,desc,catog,price):
        self.all.append(expense(desc,catog,price))

    def delete(self,x):
        del self.all[x]
        
    def total(self):
        t = 0
        for item in self.all:
            t += item.price
        return t

    def items(self):
        t = []
        for item in self.all:
            t += [[item.desc,item.catog,item.price]]
        return t


    
        
