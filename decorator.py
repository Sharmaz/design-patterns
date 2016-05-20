# -*-coding:utf-8-*-

from abc import ABCMeta

class Shape:
    # Component Interfaz para objetos que pueden tener responsabilidades añadidas dinámicamente.
    __metaclass__ = ABCMeta
    def draw(self):
        pass

class Circle(Shape):
    # Concrete Component, Define un objeto al cual se le puede añadir responsabilidades adicionales.
    def draw(self):
        print "Soy un Circulo"

class Rectangle(Shape):
    # Concrete Component, Define un objeto al cual se le puede añadir responsabilidades adicionales.
    def draw(self):
        print "Soy un Rectangulo"

class ShapeDecorator(Shape):
    # Decorator, Mantiene una referencia al objeto Component y define una interfaz que cumple con la interfaz de Component.
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape

    def draw(self):
        self.decoratedShape.draw()

    def doSomethingElse(self):
        pass

class ColorRedShapeDecorator(ShapeDecorator):
    # Concrete Decorator, Extienden la funcionalidad del Component al añadirle estado o comportamiento.
    def draw(self):
        self.decoratedShape.draw()
        self.doSomethingElse()

    def doSomethingElse(self):
        print "Pintando de Rojo"

if __name__ == "__main__":
    circle = Circle()
    rectangle = Rectangle()
    redRectangle = ColorRedShapeDecorator( rectangle )
    redCircle = ColorRedShapeDecorator( circle )

    print "######"
    circle.draw()
    redCircle.draw()
    print "######"
    rectangle.draw()
    redRectangle.draw()
