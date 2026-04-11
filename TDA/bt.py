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


"""4-Independent set"""


def independent_set(grafo):
    conjunto = []
    max_conjunto = [0]
    return bt_independent_set(
        grafo, conjunto, [], 0, grafo.obtener_vertices(), max_conjunto
    )


def bt_independent_set(grafo, conjunto, actual, idx, vertices, max_conjunto):
    if idx == len(vertices):
        if len(actual) > max_conjunto[0]:
            max_conjunto[0] = len(actual)
            conjunto.clear()
            conjunto.extend(actual)
        return

    vertice = vertices[idx]
    if no_es_adyc(grafo, vertice, actual):
        actual.append(vertice)
        bt_independent_set(grafo, conjunto, actual, idx + 1, vertices, max_conjunto)
        actual.pop()
    bt_independent_set(grafo, conjunto, actual, idx + 1, vertices, max_conjunto)


def no_es_adyc(grafo, vertice, conjunto):
    for nodo in conjunto:
        if vertice in grafo.adyacentes(nodo):
            return False
    return True


"""8- Isomorfismo de grafos"""


def hay_isomorfismo(grafo1, grafo2):
    if len(grafo1.obtener_vertices()) != len(grafo2.obtener_vertices()):
        return False
    vertices1 = grafo1.obtener_vertices()
    vertices2 = grafo2.obtener_vertices()
    return backtracking_isomorfismo(grafo1, grafo2, vertices1, vertices2, {}, 0)


def backtracking_isomorfismo(grafo1, grafo2, vertices1, vertices2, mapeo, idx):
    if idx == len(vertices1):
        return True

    vertice1 = vertices1[idx]
    for vertice2 in vertices2:
        if vertice2 not in mapeo.values() and es_adyacente_equivalente(
            grafo1, grafo2, vertice1, vertice2, mapeo
        ):
            mapeo[vertice1] = vertice2
            if backtracking_isomorfismo(
                grafo1, grafo2, vertices1, vertices2, mapeo, idx + 1
            ):
                return True
            del mapeo[vertice1]

    return False


def es_adyacente_equivalente(grafo1, grafo2, vertice1, vertice2, mapeo):
    adyacentes1 = set(grafo1.adyacentes(vertice1))
    adyacentes2 = set(grafo2.adyacentes(vertice2))

    for v1 in adyacentes1:
        if v1 in mapeo:
            if mapeo[v1] not in adyacentes2:
                return False
        else:
            if not any(v2 for v2 in adyacentes2 if v2 not in mapeo.values()):
                return False

    for v2 in adyacentes2:
        if v2 in mapeo.values():
            if list(mapeo.keys())[list(mapeo.values()).index(v2)] not in adyacentes1:
                return False
        else:
            if not any(v1 for v1 in adyacentes1 if v1 not in mapeo):
                return False

    return True


"""9- Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo."""


def obtener_combinaciones(materias):
    # codigo de muestra
    combinaciones = []
    backtracking_combinaciones(materias, 0, [], combinaciones)
    return combinaciones


def backtracking_combinaciones(materias, idx, actual, combinaciones):
    if idx == len(materias):
        combinaciones.append(actual.copy())
        return
    for curso in materias[idx]:
        for c in actual:
            if not son_compatibles(curso, c):
                break
        else:
            actual.append(curso)
            backtracking_combinaciones(materias, idx + 1, actual, combinaciones)
            actual.pop()


"""10- Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. ¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?

"""


def sumatoria_dados(n, s):
    resultados = []
    backtracking_dados(n, s, [], resultados, 0)
    return resultados


def backtracking_dados(n, s, actual, resultados, tirados):
    if len(actual) == n:
        if sum(actual) == s:
            resultados.append(actual.copy())
        return

    if sum(actual) > s:
        return
    if tirados + sum(range(1, 7)) * (n - len(actual)) < s:
        return
    for dado in range(1, 7):
        actual.append(dado)
        backtracking_dados(n, s, actual, resultados, tirados + 1)
        actual.pop()


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


"""14- Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien

(i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices."""


def dominating_set_min(grafo):
    mejor = []
    min_ds = [len(grafo.obtener_vertices())]
    vertices = grafo.obtener_vertices()
    bt_dominating_set(grafo, vertices, mejor, min_ds, [], 0)
    return mejor


def bt_dominating_set(grafo, vertices, mejor, min_ds, actual, idx):
    if len(actual) > min_ds[0]:
        return
    if idx == len(vertices):
        if es_dominante(grafo, actual, vertices):
            min_ds[0] = len(actual)
            mejor.clear()
            mejor.extend(actual)
        return
    vertice = vertices[idx]
    actual.append(vertice)
    bt_dominating_set(grafo, vertices, mejor, min_ds, actual, idx + 1)
    actual.pop()
    bt_dominating_set(grafo, vertices, mejor, min_ds, actual, idx + 1)


def es_dominante(grafo, conjunto, vertices):

    for v in vertices:
        if v in conjunto:
            continue
        for ady in grafo.adyacentes(v):
            if ady in conjunto:
                break
        else:
            return False
    return True


"""
15- Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos)."""


def max_grupos_bodegon(P, W):
    grupos = []
    max_ocupacion = [0]
    backtracking_bodegon(P, W, grupos, max_ocupacion, [], 0)
    return grupos


def backtracking_bodegon(P, W, grupos, max_ocupacion, actual, idx):
    ocupacion_actual = sum(actual)
    if ocupacion_actual > max_ocupacion[0] and ocupacion_actual <= W:
        max_ocupacion[0] = ocupacion_actual
        grupos.clear()
        grupos.extend(actual)
    if idx == len(P):
        return
    grupo = P[idx]
    if ocupacion_actual + grupo <= W:
        actual.append(grupo)
        backtracking_bodegon(P, W, grupos, max_ocupacion, actual, idx + 1)
        actual.pop()
    backtracking_bodegon(P, W, grupos, max_ocupacion, actual, idx + 1)


"""16- Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber cuál es ese mínimovalor para cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema. Indicar la complejidad del algoritmo implementado."""


def pintar_colectivos(colectivos, paradas):
    pintados = {}
    min_valor = [len(colectivos)]
    backtracking_pintar(colectivos, paradas, pintados, min_valor, 0)
    return pintados


def backtracking_pintar(colectivos, paradas, pintados, min_valor, idx):
    if idx == len(colectivos):
        colores_usados = max(pintados.values()) if pintados else 0
        if colores_usados < min_valor[0]:
            min_valor[0] = colores_usados
        return
    colectivo = colectivos[idx]
    for color in range(1, min_valor[0]):
        if color_valido_paradas(colectivo, color, pintados, paradas):
            pintados[colectivo] = color
            backtracking_pintar(colectivos, paradas, pintados, min_valor, idx + 1)
            del pintados[colectivo]


def color_valido_paradas(colectivo, color, pintados, paradas):
    for parada in paradas:
        if colectivo in parada:
            for otro in parada:
                if otro != colectivo and otro in pintados and pintados[otro] == color:
                    return False
    return True
