function AdapteeShipping() {
  // Adaptee, Define una interfaz existente que necesita adaptarse.
  this.request = function(origen, destino, peso) {
    this.origen = origen
    this.destino = destino
    this.peso = peso
    this.total = peso * 100; // Math.round(Math.random()*12345)
    return this.total;
  }
}

function TargetShipping() {
  // Target, Define la interfaz de dominio especifico que utiliza Client.
  this.login = function(credenciales){
    // To Do
  }
  this.setOrigen = function(origen) {
    this.origen = origen
  }
  this.setDestino = function(destino) {
    this.destino = destino
  }
  this.calcular = function(peso) {
    this.peso = peso
    this.total = peso * 100; //Math.round(Math.random()*4321)
    return this.total;
  }

}

function ShippingAdapter(credenciales) {
  // Adapter, Adapta la interfaz Adaptee para la interfaz de destino.
  var targetShipping = new TargetShipping()

  targetShipping.login()
  return {
    request: function(origen, destino, peso) {
      targetShipping.setOrigen(origen)
      targetShipping.setDestino(destino)
      return targetShipping.calcular(peso)
    }
  }

}
function Client() {
  // Cliente, Colabora con objetos de acuerdo con la interfaz Target.
  this.run = function() {
    var oldInterface = new AdapteeShipping()
    var cost = oldInterface.request("1234","321",232.34)
    console.log(cost)

    var mycreeds = "user/pass"
    var adapter = new ShippingAdapter(mycreeds)
    var newCost = adapter.request("1234", "321", 232.34)

    console.log(newCost)
  }
}

cliente = new Client()
cliente.run();
