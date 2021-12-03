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

    def cat(self,cato):
        t = 0
        for item in self.all:
            if item.catog == cato:
                t += item.price
        return t


e = expenses()

def menu():
    print('''
1. add expense
2. delete expense
3. output total
4. output all
5. output catagory total''')
    x = int(input('>>'))

    if x == 1:
        e.add(input('description>>'),input('catogory>>'),int(input('price>>')))
    elif x == 2:
        e.delete(int(input("x>>")))
    elif x == 3:
        print(e.total())
    elif x == 4:
        t = e.items()
        for line in t:
            print(t.index(line),' - ',line)
    elif x == 5:
        print(e.cat(input('catogory>>')))

while True:
    menu()
