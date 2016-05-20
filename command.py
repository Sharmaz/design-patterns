# -*-coding:utf-8-*-

from abc import ABCMeta

class Command:
    # Command, Declara una interfaz para ejecutar una operación.
    __metaclass__ = ABCMeta
    def execute(self):
        pass

class Light:
    # Receiver, Sabe como ejecutar las operaciones.
    def turnOn(self):
        print "Foco Encendido"

    def turnOff(self):
        print "Foco Apagado"

class Switch:
    # Invoker, Le pide a Command que ejecute la petición.
    def __init__(self, onCommand, offCommand):
        self._onCommand = onCommand
        self._offCommand = offCommand

    def on(self):
        self._onCommand.execute()
    def off(self):
        self._offCommand.execute()

class OnCommand(Command):
    # Concrete Command, Extiende Command, implementando el metodo execute al invocar las operaciones correspondientes en el Receiver.
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turnOn()

class OffCommand(Command):
    # Concrete Command, Extiende Command, implementando el metodo execute al invocar las operaciones correspondientes en el Receiver.
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turnOff()

class LightSwitch:
    # Cliente, Crea un objeto ConcreteCommand y le asigna su receiver.
    def __init__(self):
        self._foco = Light()
        self._switchUpp = OnCommand(self._foco)
        self._switchDown = OffCommand(self._foco)
        self._switch = Switch(self._switchUpp, self._switchDown)

    def operation(self, cmd):
        if cmd == "ON":
            self._switch.on()
        elif cmd == "OFF":
            self._switch.off()
        else:
            print "Operación Invalida"

if __name__ == "__main__":
    client = LightSwitch()
    print "Testing on command"
    client.operation("ON")
    print "Testing off command"
    client.operation("OFF")
