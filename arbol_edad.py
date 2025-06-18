# Definicion de la clase Nodo
class Nodo:
    def __init__(self, edad):
        self.edad = edad
        self.izquierda = None
        self.derecha = None

# Clase principal del arbol
class ArbolEdad:
    def __init__(self):
        self.raiz = None

    # Metodo para insertar una nueva edad en el arbol
    def insertar(self, edad):
        if self.raiz is None:
            self.raiz = Nodo(edad)
        else:
            self._insertar_recursivo(self.raiz, edad)

    # Insercion recursiva segun valor
    def _insertar_recursivo(self, nodo_actual, edad):
        if edad < nodo_actual.edad:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(edad)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, edad)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(edad)
            else:
                self._insertar_recursivo(nodo_actual.derecha, edad)

    # Recorrido del arbol e impresion con clasificacion
    def clasificar_y_mostrar(self, nodo):
        if nodo:
            self.clasificar_y_mostrar(nodo.izquierda)
            if nodo.edad < 18:
                categoria = "Menor de edad"
            elif nodo.edad <= 60:
                categoria = "Adulto"
            else:
                categoria = "Adulto mayor"
            print(f"{nodo.edad} años -> {categoria}")
            self.clasificar_y_mostrar(nodo.derecha)

# Programa principal
if __name__ == "__main__":
    arbol = ArbolEdad()
    edades = [15, 34, 72, 10, 55, 80, 25]
    for edad in edades:
        arbol.insertar(edad)

    print("Clasificacion de personas por edad:")
    arbol.clasificar_y_mostrar(arbol.raiz)
