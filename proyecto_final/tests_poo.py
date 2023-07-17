# Importamos la librerías necesarias
import unittest

# Importamos la clase principal del proyecto para realizar los tests
from proyecto_poo import Matriz

# Usamos POO para los tests
class TestPrograma(unittest.TestCase):
    def test_generar_matriz(self):
        # Test para verificar si la matriz generada tiene el tamaño correcto
        matriz_obj = Matriz(3)
        matriz_obj.generar_matriz()
        matriz = matriz_obj.matriz
        self.assertEqual(len(matriz), 3)
        self.assertEqual(len(matriz[0]), 3)
        self.assertEqual(len(matriz[1]), 3)
        self.assertEqual(len(matriz[2]), 3)
    
    def test_calcular_sumas(self):
        # Test para verificar si las sumas de filas y columnas son correctas
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matriz_obj = Matriz(len(matriz))
        matriz_obj.matriz = matriz
        filas_suma, columnas_suma = matriz_obj.calcular_sumas()
        self.assertEqual(filas_suma, [6, 15, 24])
        self.assertEqual(columnas_suma, [12, 15, 18])
        
        matriz = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        matriz_obj = Matriz(len(matriz))
        matriz_obj.matriz = matriz
        filas_suma, columnas_suma = matriz_obj.calcular_sumas()
        self.assertEqual(filas_suma, [0, 3, 6])
        self.assertEqual(columnas_suma, [3, 3, 3])
        
        matriz = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
        matriz_obj = Matriz(len(matriz))
        matriz_obj.matriz = matriz
        filas_suma, columnas_suma = matriz_obj.calcular_sumas()
        self.assertEqual(filas_suma, [27, 27, 27])
        self.assertEqual(columnas_suma, [27, 27, 27])
    
    def test_tamanio_matriz_invalido(self):
        # Test para verificar si se lanza una excepción al ingresar un tamaño de matriz no válido
        with self.assertRaises(ValueError):
            matriz_obj = Matriz(0)
            matriz_obj.generar_matriz()
            
        with self.assertRaises(ValueError):
            matriz_obj = Matriz(100)
            matriz_obj.generar_matriz()

    def test_tipo_invalido(self):
        # Test para verificar si se lanza una excepción al ingresar un tipo de dato no válido
        with self.assertRaises(ValueError):
            matriz_obj = Matriz("abc")
            matriz_obj.generar_matriz()
        
        with self.assertRaises(ValueError):
            matriz_obj = Matriz([1, 2, 3])
            matriz_obj.generar_matriz()

# Ejecutar los test unitarios
if __name__ == "__main__":
    unittest.main()
