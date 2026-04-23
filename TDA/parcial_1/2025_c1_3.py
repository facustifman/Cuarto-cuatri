"""1. Implementar una función que, dado un arreglo ordenado y sin repetidos de valores enteros no negativos, obtenga el mínimo
valor que no se encuentre en el arreglo. Indicar y justificar adecuadamente la complejidad del algoritmo.
Por ejemplo:
minimoExcluido([0, 1, 5]) --> 2
minimoExcluido([1, 3, 5]) --> 0
minimoExcluido([0, 1, 2, 3, 4, 5]) --> 6
minimoExcluido([0, 1, 2, 3, 4, 5, 1234567]) --> 6"""


def minimoExcluido(arr):
    if arr[0] != 0:
        return 0
    candidato = minExcluido(arr, 0, len(arr) - 1)
    return candidato


def minExcluido(arr, ini, fin):
    if ini > fin:
        return ini
    mid = (ini + fin) // 2
    if arr[mid] == mid:
        return minExcluido(arr, mid + 1, fin)
    else:
        return minExcluido(arr, ini, mid - 1)


"""2. Dado un grafo sin ciclos (un bosque, el cual es necesariamente bipartito), implementar un algoritmo greedy que obtenga el
matching máximo. Es decir, el subconjunto máximo de aristas tal que ninguna arista comparta vértice entre sí.
Indicar y justificar la complejidad del algoritmo. El análisis de la complejidad debe estar completo. Justificar por qué es un
algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo."""


def matching_maximo(grafo):
    matching = []
    visitados = set()
    for vertice in grafo:
        if vertice not in visitados:
            for vecino in grafo.adyacentes(vertice):
                if vecino not in visitados:
                    matching.append((vertice, vecino))
                    visitados.add(vertice)
                    visitados.add(vecino)
                    break
    return matching


# *La complejidad del algoritmo es O(V+E) debido a que se recorre cada vertice y sus adyacentes una sola vez. El algoritmo es Greedy porque basado en una decision local de fijarse si el vertice a emparejar no ha sido visitado, y si es asi, se empareja con el primer vecino disponible. El algoritmo da siempre la solucion optima en un bosque, ya que al ser un grafo sin ciclos, no hay posibilidad de que una decision local incorrecta afecte a futuras decisiones, garantizando asi que se obtiene el matching máximo.

"""3. Un P athSelection de un grafo dirigido G y un conjunto de caminos P1, P2, ..., Pc, es un subconjunto de dichos caminos tal que
ninguno de ellos compartan ningún nodo entre sí. Implementar un algoritmo que dado obtenga el P athSelection más grande
posible de un Grafo y un conjunto de caminos dado. Obviamente, implementarlo con un algoritmo por bactracking (si te sale
hacerlo polinomial con otra técnica, te aseguramos el 10 en la materia, pero no te prometemos darte nada del millón de dólares)."""


def path_selection(grafo, caminos):
    mejor_seleccion = []
    mejor_cantidad = [0]
    bt_path_selection(grafo, caminos, mejor_seleccion, mejor_cantidad, [], 0)
    return mejor_seleccion


def bt_path_selection(grafo, caminos, mejor_seleccion, mejor_cantidad, actual, idx):
    if idx == len(caminos):
        if len(actual) > mejor_cantidad[0]:
            mejor_seleccion.clear()
            mejor_seleccion.append(list(actual))
            mejor_cantidad[0] = len(actual)
        return

    if no_se_solapan(actual, caminos[idx]):
        actual.append(caminos[idx])
        bt_path_selection(
            grafo, caminos, mejor_seleccion, mejor_cantidad, actual, idx + 1
        )
        actual.pop()
    bt_path_selection(grafo, caminos, mejor_seleccion, mejor_cantidad, actual, idx + 1)


def no_se_solapan(seleccion, camino):
    for i in seleccion:
        for nodo in i:
            if nodo in camino:
                return False
    return True


"""4. Dado un arreglo de números positivos, donde cada elemento representa el máximo número de pasos que podemos dar desde esa
posición, implementar un algoritmo que, utilizando programación dinámica determine la menor cantidad de saltos a realizar
para llegar al final del arreglo (comenzamos en la posición 0). También escribir el algoritmo que permita reconstruir la solución.
Indicar y justificar la complejidad del algoritmo implementado.
Por ejemplo, si el arreglo es [2, 3, 1, 1, 4], la solución óptima es ir desde la posición 0 a la posición 1 (saltando 1 lugar,
teniendo máximo 2 desde el inicio), y de allí a la posición 4 (saltando 3 lugares, que es el máximo desde dicha posición), logrando
llegar al final en 2 saltos."""

# * La ecuacion de recurrencia es: opt[i] = 1 + min(opt[j]) para todo j que permite llegar a i


def min_pasos(pasos):
    n = len(pasos)
    opt = [float("inf")] * n
    for i in range(n):
        for j in range(i):
            if pasos[j] + j >= i:
                opt[i] = min(opt[i], 1 + opt[j])
    return opt[-1]
