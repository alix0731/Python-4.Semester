

postfix = "from property"

class Car:
    def __init__(self, *args):
        self.__make = args[0]
        self.__model = args[1]
        self.__bhp = args[2]
        self.__mph = args[3]


    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def bhp(self):
        return self.__bhp

    @property
    def mph(self):
        return self.__mph
        
    @make.setter
    def make(self, make):
        self.__make = make

    @model.setter
    def model(self, model):
        self.__model = model

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @mph.setter 
    def mph(self, mph):
        self.__mph = map


car = Car('Burger', 2020, 100, 275)
print(car.mph)
print(car.model)


