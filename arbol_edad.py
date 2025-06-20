# Definicion de la clase Nodo
class Nodo:
    def __init__(self, edad):
        self.edad = edad            # Guarda la edad de la persona
        self.izquierda = None       # Puntero al hijo izquierdo (menores)
        self.derecha = None         # Puntero al hijo derecho (mayores)

# Clase principal del arbol
class ArbolEdad:
    def __init__(self):
        self.raiz = None            # Al inicio, el arbol no tiene nodos

    # Metodo para insertar una nueva edad en el arbol
    def insertar(self, edad):
        if self.raiz is None:
            self.raiz = Nodo(edad)  # Si no hay raiz, se crea el primer nodo
        else:
            self._insertar_recursivo(self.raiz, edad)  # Llama al metodo recursivo

    # Insercion recursiva segun valor
    def _insertar_recursivo(self, nodo_actual, edad):
        if edad < nodo_actual.edad:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(edad)  # Inserta en izquierda si es menor
            else:
                self._insertar_recursivo(nodo_actual.izquierda, edad)  # Sigue por la izquierda
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(edad)  # Inserta en derecha si es mayor o igual
            else:
                self._insertar_recursivo(nodo_actual.derecha, edad)  # Sigue por la derecha

    # Recorrido del arbol e impresion con clasificacion
    def clasificar_y_mostrar(self, nodo):
        if nodo:
            self.clasificar_y_mostrar(nodo.izquierda)  # Recorre izquierda
            if nodo.edad < 18:
                categoria = "Menor de edad"
            elif nodo.edad <= 60:
                categoria = "Adulto"
            else:
                categoria = "Adulto mayor"
            print(f"{nodo.edad} años -> {categoria}")  # Muestra clasificacion
            self.clasificar_y_mostrar(nodo.derecha)  # Recorre derecha


# Programa principal
if __name__ == "__main__":
    arbol = ArbolEdad()                                # Crea el arbol
    edades = [15, 34, 72, 10, 55, 80, 25]              # Lista de edades a insertar
    for edad in edades:
        arbol.insertar(edad)                           # Inserta cada edad en el arbol

    print("Clasificacion de personas por edad:")
    arbol.clasificar_y_mostrar(arbol.raiz)            # Muestra edades clasificadas
