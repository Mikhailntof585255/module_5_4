class House:
    house_history=[]
    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args)
        return super().__new__(cls)
    def __init__(self,name,number_of_floors:int):
        self.name=name
        self.number_of_floors=number_of_floors

    def __del__(self):
        return print(self.name, " снесён, но останется в истории")


h1 = House("ЖК Эльбрус", 10)
print(House.house_history)
h2 = House("ЖК Акация", 20)
print(House.house_history)
h3 = House('ЖК Матрёшки',20)
print(House.house_history)
del h2
del h3
print(House.house_history)

# print(h2)
# print(h3)