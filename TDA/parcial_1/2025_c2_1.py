"""1. Sea A una matríz de n × n (con n ≥ 3) con todos valores diferentes. Definimos la vecindad de una celda como las 8 celdas vecinas
(arriba, abajo, derecha, izquierda, y las 4 diagonales), siempre que existan (en los bordes algunas no existirán). Un elemento A [i, j] es
un máximo local si su valor es estrictamente mayor que el valor de todas las celdas vecinas. Implementar un algoritmo de división y
conquista que encuentre un máximo local en tiempo O(n). Justificar adecuadamente la complejidad del algoritmo implementado.
"""


def max_local(matriz, izq, der):
    mid = (izq + der) // 2
    num = 0
    pos = []
    for f in range(len(matriz)):
        if matriz[f][mid] > num:
            num = matriz[f][mid]
            pos = [f, mid]

    cand, posicion = es_max_local(matriz, num, pos)

    if cand == num:
        return num
    if posicion[1] > mid:
        return max_local(matriz, mid + 1, der)
    return max_local(matriz, izq, mid)


def es_max_local(matriz, num, pos):
    fila = pos[0]
    col = pos[1]
    cand = num
    posicion = pos

    for f in range(fila - 1, fila + 2):
        for c in range(col - 1, col + 2):
            if 0 <= f < len(matriz) and 0 <= c < len(matriz[0]):
                if matriz[f][c] > num:
                    cand = matriz[f][c]
                    posicion = [f, c]
    return cand, posicion


"""2. Implementar un algoritmo greedy que dada una lista de intervalos de formato [a, b] (con a <= b) determine el menor conjunto
de intervalos que incluyan el mismo rango que los intervalos originales. Indicar y justificar la complejidad del algoritmo. Justificar
por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo."""


def juntar_intervalos(intervalos):
    intervalos.sort(lambda x: x[0])
    inicio = intervalos[0][0]
    final = intervalos[0][1]
    respuesta = []
    for ini, fin in intervalos:
        if final >= ini:
            if fin > final:
                final = fin
        else:
            respuesta.append([inicio, final])
            inicio = ini
            final = fin
    respuesta.append([inicio, final])
    return respuesta


# * La complejidad del algoritmo es O(n log n) porque se ordena el intervalo y cualquier algoritmo de ordenamiento que se aplique sin contexto no puede ser menor a O(n log n). El algoritmo es Greedy porque en cada paso busca un optimo local buscando minimizar la cantidad de intervalos totales devuelto observando si el inicio del arreglo siguiente al visto se encuentra contenido en el actual teniendo en cuenta previamente se ordeno por el primer numero de cada intervalo teniendo en cuenta que a<= b dentro de los intervalos. El algoritmo es optimo porque no hay una manera mas eficiente de construir los intervalos.

"""3. El problema conocido como Feedback Vertex Set (FVS) indica: Dado un grafo (por simplificación, no dirigido), indicar vértices a
eliminar de dicho grafo de tal manera que el grafo quede acíclico.
En nuestro grafo cada vértice i tiene un valor positivo vi

. Implementar un algoritmo que, por backtracking, encuentre el mínimo
FVS (es decir, el conjunto de vértices que sea un FVS, y sea de suma mínima). Si bien es obvio, el grafo no cuenta con una primitiva
tiene_ciclos (e, incluso, si la tuviera, sería poco conveniente usarla, recomendamos pensar por qué)."""


def fvs(grafo):
    min_sum = [float("inf")]
    eliminados = []
    vertices = grafo.obtener_vertices()
    bt_fvs(grafo, vertices, min_sum, eliminados, [], 0, 0)
    return eliminados


def bt_fvs(grafo, vertices, min_sum, eliminados, actual, sum_actual, idx):
    if idx == len(vertices):
        if sum_actual < min_sum[0] and es_aciclico(grafo[:], actual):
            min_sum[0] = sum_actual
            eliminados.clear()
            eliminados.extend(actual)
        return

    actual.append(vertices[idx])
    sum_actual += vertices[idx].valor
    bt_fvs(grafo, vertices, min_sum, eliminados, actual, sum_actual, idx + 1)

    sum_actual -= vertices[idx].valor
    actual.pop()
    bt_fvs(grafo, vertices, min_sum, eliminados, actual, sum_actual, idx)


def es_aciclico(grafo, actual):
    for v in actual:
        grafo.eliminar_vertice(v)

    visitados = set()
    padre = {}

    for inicio in grafo.obtener_vertices():
        if inicio in visitados:
            continue
        cola = Cola_enlazada()  # type: ignore
        cola.encolar(inicio)
        padre[inicio] = None
        while cola.notEmpty():
            v = cola.desencolar()
            visitados.add(v)
            for w in grafo.adyacentes(v):
                if w not in padre:
                    padre[w] = v
                    cola.encolar(w)
                elif padre[v] != w:
                    return False
    return True


"""4. En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. Ahora planteamos un problema similar: Implementar un algoritmo que dado una lista (ordenada) de monedas posibles y una cantidad de cambio a dar, devuelva la cantidad de formas diferentes que hay para dar dicho cambio. El algoritmo a implementar debe ser también por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado."""

# * La ecuacion de recurrencia es: opt[i]= opt[i-j] siendo j todos los billetes


def cambio(billetes, cambio):
    opt = [0] * len(cambio)
    opt[0] = 1
    for i in range(len(opt)):
        for j in billetes:
            if j > i:
                break
            opt[i] += opt[i - j]

    return opt


# * La complejidad es O(C*B) siendo B los billetes y c el cambio
