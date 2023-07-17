# Importamos la librerías necesarias
import random

# Creamos la clase principal del programa
class Matriz:
    # Constructor
    def __init__(self, n):
        self.n = n
        self.matriz = []

    # Generamos una matriz cuadrada de n x n elementos de manera aleatoria
    def generar_matriz(self):
        # En los test unitarios me daba error el lanzamiento de las excepciones
        # Comprobamos que es un entero y que es mayor que cero y menor que 100
        if not isinstance(self.n, int) or self.n <= 0 or self.n >= 100:
            raise ValueError("El tamaño de la matriz debe ser un número entero positivo mayor que cero.")
        
        # Creamos la matriz
        # Usamos números aleatorios entre 0 y 9
        for _ in range(self.n):
            fila = []
            for _ in range(self.n):
                fila.append(random.randint(0, 9))
            self.matriz.append(fila)

    # Recorremos los elementos de la matriz que le pasamos por parámetro
    # Los imprimimos por pantalla
    def imprimir_matriz(self):
        for fila in self.matriz:
            for elemento in fila:
                print(elemento, end=" ")
            print()

    # Función que calcula las sumas, tanto de filas como de columnas
    def calcular_sumas(self):
        filas_suma = [sum(fila) for fila in self.matriz]
        columnas_suma = [sum(columna) for columna in zip(*self.matriz)]
        return filas_suma, columnas_suma

    # Mostramos por pantalla el valor de las sumas
    def imprimir_sumas(self, filas_suma, columnas_suma):
        print("\nSuma de las filas:\n")
        for i, suma in enumerate(filas_suma):
            print(f"Fila {i+1}: {suma}")
        
        print("\nSuma de las columnas:\n")
        for i, suma in enumerate(columnas_suma):
            print(f"Columna {i+1}: {suma}")

# Función principal en donde se introduce el número de filas y columnas 
# Se ejecuta el flujo lógico del programa
# Manejamos las excepciones
def main():
    try:
        n = input("\nIngrese el tamaño de la matriz (N): ")
        
        # No se aceptan caracteres que no sean números
        if not n.isdigit():
            raise ValueError("El tamaño de la matriz debe ser un número entero positivo mayor que cero.")
        
        # El número debe ser mayor a cero y menor a cien
        n = int(n)
        if n <= 0 or n >= 100:
            raise ValueError("El tamaño de la matriz debe ser un número entero positivo mayor que cero y menor que 100.")
        
        matriz = Matriz(n)
        matriz.generar_matriz()
        
        print("\nMatriz generada:\n")
        matriz.imprimir_matriz()
        
        filas_suma, columnas_suma = matriz.calcular_sumas()
        
        print("\nSuma de elementos:")
        matriz.imprimir_sumas(filas_suma, columnas_suma)
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    
    except Exception as e:
        print(f"Ha ocurrido un error: {str(e)}")

if __name__ == "__main__":
    main()
