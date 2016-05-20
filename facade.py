# -*-coding:utf-8-*-

class Scanner:
    # Clases del subsistema, Implementan una funcionalidad del subsistema.
    def __init__(self):
        self.nombre = "Scanner"

class Parser:
    # Clases del subsistma, Llevan acabo el trabajo asignado por el objeto Facade.
    def __init__(self):
        self.nombre = "Parser"

class Compiler:
    # Facade, Conoce cuales clases del subsistema son responsables por una petición.
    def __init__(self):
        self.nombre = "Compiler"
        self.scanner = Scanner()
        self.parser = Parser()

    # Facade, Delegan peticiones del cliente a los objetos del subsistema apropiado.
    def compile(self):
        print "Compilando ..."
        print "Escaneando %s" % self.scanner.nombre
        print "Parseando %s" % self.parser.nombre


if __name__ == "__main__":
    compiler = Compiler()
    compiler.compile()
