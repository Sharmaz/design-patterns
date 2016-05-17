var mySingleton = (function() {
  // Instacia almacena una referencia a el Singleton
  var instance;

  function init() {
    // Singleton, construlle el objeto que vamos a generar
    // Metodos privados y variables
    function privateMethod() {
      console.log("Soy un metodo privado")
    }
    var privateNumber = Math.round(Math.random()*1000);

    return {
      // Metodos publicos y variables
      publicMethod: function() {
        console.log("Entrando al metodo publico")
        privateMethod();
        console.log("Saliendo del metodo publico")
      },
      getRandomNumber: function() {
        return privateNumber;
      }
    }
  }

  return {
    // Obtenemos la instancia de Singleton si esta existe
    // o creamos una en el caso que no exista
    getInstance: function() {
      if ( !instance ) {
        instance = init();
      }
      return instance;
    }
  }
})();

var testOne = mySingleton.getInstance();
testOne.publicMethod();
var testTwo = mySingleton.getInstance();
testTwo.publicMethod();

console.log("testOne " + testOne.getRandomNumber())
console.log("testTwo " + testOne.getRandomNumber())

console.log(testOne.getRandomNumber() === testTwo.getRandomNumber())
