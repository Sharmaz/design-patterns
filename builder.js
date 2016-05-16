function testBuilderPattern() {
  var shop = new Director()
  var carBuilder = new CarBuilder()
  var car = shop.construct(carBuilder)

  car.doSomething()
}

function Director() {
  /* clase que identifica el metodo construct y recibe
  como parametro el builder */
  this.construct = function(builder) {
    builder.step1()
    builder.step2()
    return builder.getResult()
  }
  // Builder contiende las partes del objeto a construir
}

function CarBuilder() {
  /* CarBuilder es el ConcreteBuilder que construye
  y junta las partes del producto implementando la interface del builder */
  this.car = null
  this.step1 = function() {
    this.car = new Car()
  }
  this.step2 = function() {
    this.car.addParts()
  }
  this.getResult = function() {
    return this.car
  }
}

function Car() {
  // Car es el producto
  this.doors = 0
  this.addParts = function() {
    this.doors = 4
  }

  this.doSomething = function() {
    console.log("Tengo " + this.doors + " puertas")
  }
}

testBuilderPattern()
