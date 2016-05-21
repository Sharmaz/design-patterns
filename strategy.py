# -*-coding:utf-8-*-
from abc import ABCMeta, abstractmethod

class TextFinder:
    # Strategy, Declara una interfaz para soportar todos los algoritmos.

    __metaclass__ = ABCMeta
    def find(self, text):
        pass

class Finder(TextFinder):
    # Concrete Strategy, Extiende a Strategy. Cada ConcreteStrategy implementa un algoritmo.

    def find(self, text):
        return "%s Fue Encontrado" % text

class OtherFinder(TextFinder):
    # Concrete Strategy, Extiende a Strategy. Cada ConcreteStrategy implementa un algoritmo.

    def find(self, text):
        return "%s Was Found" % text

if __name__ == "__main__":
    # Context, Mantiene una referencia al objeto Strategy.
    # Context, Define una interfaz que deja a Strategy accesar a sus datos.
    
    finderOne = Finder()
    finderTwo = OtherFinder()

    print finderOne.find("abc")
    print finderTwo.find("abc")
