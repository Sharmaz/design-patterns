# -*-coding:utf-8-*-
from abc import ABCMeta, abstractmethod
class Publisher:
    # Observable, Declara una interfaz para añadir o remover observers del cliente.
    __metaclass__ = ABCMeta
    def __init__(self):
        pass

    def addObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyAll(self):
        pass

class Forum(Publisher):
    # Concrete Observable, Extiende Observable. Mantiene el estado del objeto y cuando cambia, notifica a los Observers ligados.

    def __init__(self):
        self.usersList = []
        self.post = None

    def addObserver(self, observer):
        if observer not in self.usersList:
            self.usersList.append(observer)

    def removeObserver(self, observer):
        self.usersList.remove(observer)

    def notifyAll(self):
        for observer in self.usersList:
            observer.notify(self.post)

    def writePost(self, text):
        self.post = text
        self.notifyAll()

class Suscriber:
    # Observer, Interfaz que define las operaciones a ser usadas para notificar a este objeto.
    def __init__(self):
        pass
    def notify(self, post):
        pass

class UserA(Suscriber):
    # Concrete Observer, Implementaciones concretas de Observer.

    def __init__(self):
        pass
    def notify(self, post):
        print "User A ha sido notificado %s" % post

class UserB(Suscriber):
    # Concrete Observer, Implementaciones concretas de Observer.

    def __init__(self):
        pass
    def notify(self, post):
        print "User B ha sido notificado %s" % post

if __name__ == "__main__":
    foro = Forum()
    user1 = UserA()
    user2 = UserB()

    foro.addObserver(user1)
    foro.addObserver(user2)

    foro.writePost("Mi primer post")

    foro.removeObserver(user2)
    foro.writePost("Mi segundo post")
