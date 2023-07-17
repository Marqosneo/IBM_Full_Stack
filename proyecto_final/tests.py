# Importamos la librerías necesarias
import unittest

# Importamos las funciones a las que haremos los tests
from proyecto import generar_matriz, calcular_sumas

class TestPrograma(unittest.TestCase):
    def test_generar_matriz(self):
        # Test para verificar si la matriz generada tiene el tamaño correcto
        matriz = generar_matriz(3)
        self.assertEqual(len(matriz), 3)
        self.assertEqual(len(matriz[0]), 3)
        self.assertEqual(len(matriz[1]), 3)
        self.assertEqual(len(matriz[2]), 3)
    
    def test_calcular_sumas(self):
        # Test para verificar si las sumas de filas y columnas son correctas
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        filas_suma, columnas_suma = calcular_sumas(matriz)
        self.assertEqual(filas_suma, [6, 15, 24])
        self.assertEqual(columnas_suma, [12, 15, 18])
        
        matriz = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        filas_suma, columnas_suma = calcular_sumas(matriz)
        self.assertEqual(filas_suma, [0, 3, 6])
        self.assertEqual(columnas_suma, [3, 3, 3])
        
        matriz = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
        filas_suma, columnas_suma = calcular_sumas(matriz)
        self.assertEqual(filas_suma, [27, 27, 27])
        self.assertEqual(columnas_suma, [27, 27, 27])
    
    def test_tamanio_matriz_invalido(self):
        # Test para verificar si se lanza una excepción al ingresar un tamaño de matriz no válido
        with self.assertRaises(ValueError):
            generar_matriz(0)
        
        with self.assertRaises(ValueError):
            generar_matriz(100)
    
    def test_tipo_invalido(self):
        # Test para verificar si se lanza una excepción al ingresar un tipo de dato no válido
        with self.assertRaises(ValueError):
            generar_matriz("abc")
        
        with self.assertRaises(ValueError):
            generar_matriz([1, 2, 3])

# Ejecutar los test unitarios
if __name__ == "__main__":
    unittest.main()
