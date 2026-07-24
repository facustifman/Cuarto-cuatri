"""4. Implementar un algoritmo que, por programación dinámica, dado un grafo no dirigido y pesado, dos vértices s y t, y un número
k, determine el costo del camino mínimo entre s y t que utilice exactamente k aristas. El camino puede repetir vértices (es decir,
el camino puede no ser simple). También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad
del algoritmo implementado (el de programación dinámica, y también el de la reconstrucción)."""

#* C[i][v] = min( C[i-1][u] + peso(u, v) ) para todo i > 0 y para toda arista (u, v) (se plantea que el grafo sea no dirigido para que a nivel código esto sea más sencillo).
def camino(grafo, K):

    opt[i][w]=[] 