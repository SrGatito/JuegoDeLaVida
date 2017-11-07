'''
Función de actualizar
-Entrada:
	-Matriz de booleanos
-Funcionalidad:
	-Recibe una matriz de boleanos y devuelve otra
 con los estados actualizados.
-Salida:
	-Nueva matriz
'''
import cesar

def actualizar(matriz):
matrizActualizada = copy.deepcopy(matriz)

	for i in range(len(matriz)):
		for j in range (len(matriz)):
			matriz[i][j] = cesar.cesar(i,j,matriz)

	return matrizActualizada
