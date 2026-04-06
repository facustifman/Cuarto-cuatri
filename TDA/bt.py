"""1- Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si."""


def no_adyacentes(grafo, n):
    conjunto = []
    return backtracking(grafo, n, conjunto)


def backtracking(grafo, n, conjunto):
    if len(conjunto) == n:
        return True

    for vertice in grafo.obtener_vertices():
        if vertice not in conjunto and no_es_adyc(grafo, vertice, conjunto):
            conjunto.append(vertice)
            if backtracking(grafo, n, conjunto):
                return True
            conjunto.pop()

    return False


def no_es_adyc(grafo, vertice, conjunto):
    for nodo in conjunto:
        if vertice in grafo.adyacentes(nodo):
            return False
    return True


"""2- Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color."""


def colorear(grafo, n):
    colores = {}
    vertices = grafo.obtener_vertices()
    return colorear_bt(grafo, n, colores, 0, vertices)


def colorear_bt(grafo, n, colores, idx, vertices):
    if idx == len(vertices):
        return True

    vertice = vertices[idx]
    for color in range(1, n + 1):
        if color_valido(grafo, vertice, color, colores):
            colores[vertice] = color
            if colorear_bt(grafo, n, colores, idx + 1, vertices):
                return True
            del colores[vertice]
    return False


def color_valido(grafo, vertice, color, colores):
    for nodo in grafo.adyacentes(vertice):
        if nodo in colores and colores[nodo] == color:
            return False
    return True


"""13- Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo."""


def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    aristas = obtener_aristas(grafo)
    min_cover = [len(vertices)]
    mejor_cover = []
    bt_vertex_cover(grafo, vertices, 0, min_cover, mejor_cover, [], aristas)
    return mejor_cover


def bt_vertex_cover(
    grafo, vertices, idx, min_cover, mejor_cover, actual_cover, aristas
):
    if len(actual_cover) >= min_cover[0]:
        return
    if idx == len(vertices):
        if es_vc(actual_cover, aristas):
            min_cover[0] = len(actual_cover)
            mejor_cover.clear()
            mejor_cover.extend(actual_cover)
        return

    vertice = vertices[idx]
    actual_cover.append(vertice)
    bt_vertex_cover(
        grafo, vertices, idx + 1, min_cover, mejor_cover, actual_cover, aristas
    )
    actual_cover.pop()
    bt_vertex_cover(
        grafo, vertices, idx + 1, min_cover, mejor_cover, actual_cover, aristas
    )


def obtener_aristas(grafo):
    aristas = set()
    for vertice in grafo.obtener_vertices():
        for adyacente in grafo.adyacentes(vertice):
            aristas.add(tuple(sorted((vertice, adyacente))))
    return aristas


def es_vc(cover, aristas):
    for a1, a2 in aristas:
        if a1 not in cover and a2 not in cover:
            return False
    return True
