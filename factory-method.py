from abc import ABCMeta



class Car:
    # Product, definimos los objetos que va a crear Factory Method.
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = None
        self.maxSpeed = None
    def __str__(self):
        return "Name is %s, maxSpeed is %s" % (self.name, self.maxSpeed)

class SportsCar(Car):
    # Concrete Product, Implementa la interfaz de product.
    def __init__(self):
        self.name = "Deportivo"
        self.maxSpeed = "250 km/h"

class FamilyCar(Car):
    # Concrete Product, Implementa la interfaz de product.
    def __init__(self):
        self.name = "Familiar"
        self.maxSpeed = "150 km/h"

class MyFactory:
    # Creator (o Factory) devuelve un objeto product.
    def createCar(self, carType):
        self.car = None
        if carType == "sports":
            self.car = SportsCar();
        elif carType == "family":
            self.car = FamilyCar();
        else:
            print "El tipo de carro %s no esta definido" % (carType)
        return self.car

    def doSomething(self):
        print "%s" % self.car

if __name__ == "__main__":
    myFactory = MyFactory()
    s = myFactory.createCar("sports")
    f = myFactory.createCar("family")

    print s
    print f
