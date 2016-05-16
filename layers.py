
class PresentationLayer:
    def __init__(self):
        self.name = "PresentationLayer"

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def servicioCapa3(self, param):
        print "Ejecutando servicio %s" % self.name
        self.lowerLayer.servicioCapa2(param)
        print "Terminamos servicio %s" % self.name

class LogicLayer:
    def __init__(self):
        self.name = "LogicLayer"

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def servicioCapa2(self, param):
        print "Ejecutando servicio %s" % self.name
        self.lowerLayer.servicioCapa1(param)
        print "Terminamos servicio %s" % self.name

class DataLayer:
    def __init__(self):
        self.name = "DataLayer"

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def servicioCapa1(self, param):
        print "Dentro de %s" % self.name
        print "Ejecutando servicio capa 1 %s" % param

if __name__ == "__main__":
    ui = PresentationLayer()
    logic = LogicLayer()
    data = DataLayer()

    ui.setLowerLayer(logic)
    logic.setLowerLayer(data)

    ui.servicioCapa3("exampleParam")
