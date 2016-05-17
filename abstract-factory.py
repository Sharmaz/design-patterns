from abc import ABCMeta, abstractmethod

class Car:
    # Abstract Product, declara interfaz para el tipo de objeto product.
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = None
        self.maxSpeed = None
    def __str__(self):
        return "Name is %s, maxSpeed is %s" % (self.name, self.maxSpeed)

class SportsCar(Car):
    # Product, define el producto a ser creado por concrete factory.
    def __init__(self):
        self.name = "Deportivo"
        self.maxSpeed = "250 km/h"

class DeluxeCar(Car):
    # Product, define el producto a ser creado por concrete factory.
    def __init__(self):
        self.name = "Deluxe"
        self.maxSpeed = "200 km/h"

class AbstractFactory:
    # AbstractFactory, declara una interfaz para un tipo de objetos product.
    __metaclass__ = ABCMeta

    def __init__(self):
        self.manufacture = None

    def __str__(self):
        return "Manufacture is %s" % (self.manufacture)

    @abstractmethod # referencia a un metodo abstracto
    def createCar(self, carType): pass

    @staticmethod # referencia al tipo de metodo
    def get_factory(factoryName):
        if factoryName == "Tesla":
            return TeslaFactory()
        elif factoryName == "Audi":
            return AudiFactory()
        raise TypeError("Unknow Factory")

class TeslaFactory(AbstractFactory):
    # Concrete Factory, implementa operaciones para generar concrete products.
    def __init__(self):
        self.manufacture = "Tesla"

    def createCar(self, carType):
        self.car = None
        if carType == "sports":
            self.car = SportsCar();
        elif carType == "deluxe":
            self.car = DeluxeCar();
        else:
            print "El tipo de carro %s no esta definido" % (carType)
        return self.car

    def doSomething(self):
        print "%s" % self.car

class AudiFactory(AbstractFactory):
    # Concrete Factory, implementa operaciones para generar concrete products.
    def __init__(self):
        self.manufacture = "Audi"

    def createCar(self, carType):
        self.car = None
        if carType == "sports":
            self.car = SportsCar();
        elif carType == "deluxe":
            self.car = DeluxeCar();
        else:
            print "El tipo de carro %s no esta definido" % (carType)
        return self.car

    def doSomething(self):
        print "%s" % self.car


if __name__ == "__main__":
    t = AbstractFactory.get_factory("Tesla")
    a = AbstractFactory.get_factory("Audi")

    s = t.createCar("sports")
    f = a.createCar("deluxe")

    print t
    print s

    print a
    print f
