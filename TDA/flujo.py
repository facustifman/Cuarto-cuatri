class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self._ady = {}
        self._cap = {}

    def agregar_vertice(self, v):
        if v not in self._ady:
            self._ady[v] = set()

    def añadir_vertice(self, v):
        self.agregar_vertice(v)

    def agregar_arista(self, v, w, capacidad=1):
        self.agregar_vertice(v)
        self.agregar_vertice(w)
        self._ady[v].add(w)
        self._cap[(v, w)] = capacidad
        if not self.dirigido:
            self._ady[w].add(v)
            self._cap[(w, v)] = capacidad

    def añadir_arista(self, v, w, capacidad=1):
        self.agregar_arista(v, w, capacidad)

    def obtener_vertices(self):
        return list(self._ady.keys())

    def adyacentes(self, v):
        return list(self._ady.get(v, ()))

    def capacidad(self, v, w):
        return self._cap.get((v, w), 0)


def flujo(grafo, s, t):
    from collections import deque

    def construir_predecesores():
        pred = {v: [] for v in grafo.obtener_vertices()}
        for v in grafo.obtener_vertices():
            for w in grafo.adyacentes(v):
                pred[w].append(v)
        return pred

    pred = construir_predecesores()
    flujos = {(v, w): 0 for v in grafo.obtener_vertices() for w in grafo.adyacentes(v)}

    while True:
        padre = {s: None}
        cola = deque([s])

        while cola and t not in padre:
            v = cola.popleft()

            for w in grafo.adyacentes(v):
                if w not in padre and grafo.capacidad(v, w) - flujos.get((v, w), 0) > 0:
                    padre[w] = (v, True)
                    cola.append(w)

            for w in pred.get(v, []):
                if w not in padre and flujos.get((w, v), 0) > 0:
                    padre[w] = (v, False)
                    cola.append(w)

        if t not in padre:
            break

        incremento = float("inf")
        v = t
        while v != s:
            p, forward = padre[v]
            if forward:
                incremento = min(
                    incremento, grafo.capacidad(p, v) - flujos.get((p, v), 0)
                )
            else:
                incremento = min(incremento, flujos.get((v, p), 0))
            v = p

        v = t
        while v != s:
            p, forward = padre[v]
            if forward:
                flujos[(p, v)] = flujos.get((p, v), 0) + incremento
            else:
                flujos[(v, p)] = flujos.get((v, p), 0) - incremento
            v = p

    return {arista: flujo for arista, flujo in flujos.items() if flujo > 0}


def disjuntos(grafo, s, t):
    # devolver una lista en la cual cada elemento es una lista, con el camino
    # entre s y t. Todos esos caminos deben incluir inicio (s) y fin (t).
    red = Grafo(dirigido=True)
    for v in grafo.obtener_vertices():
        red.agregar_vertice(v)
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            red.agregar_arista(v, w, 1)

    flujos = flujo(red, s, t)

    activo = {arista: f for arista, f in flujos.items() if f > 0}
    caminos = []

    while True:
        camino = _bfs_camino(activo, s, t, red)
        if camino is None:
            break
        caminos.append(camino)
        for i in range(len(camino) - 1):
            arista = (camino[i], camino[i + 1])
            activo[arista] -= 1
            if activo[arista] == 0:
                del activo[arista]

    return caminos


def _bfs_camino(activo, s, t, red):
    cola = [[s]]
    visitados = {s}
    while cola:
        camino = cola.pop(0)
        v = camino[-1]
        if v == t:
            return camino
        for w in red.adyacentes(v):
            if w not in visitados and activo.get((v, w), 0) > 0:
                visitados.add(w)
                cola.append(camino + [w])
    return None


def representantes(miembros):
    # devolver un diccionario NombreRepresentante -> NombreClubRepresentado
    # si no se puede resolver dadas las características del problema, devolver None
    # miembros: lista de objetos Miembro con atributos .nombre, .partido, .clubes
    clubes = {}
    for m in miembros:
        for club in m.clubes:
            if club not in clubes:
                clubes[club] = []
            clubes[club].append(m.nombre)

    n = len(clubes)
    if n == 0:
        return {}
    limite = n // 2

    s = "__s__"
    t = "__t__"
    red = Grafo(dirigido=True)
    red.agregar_vertice(s)
    red.agregar_vertice(t)

    for club in clubes:
        red.agregar_vertice("club_" + club)
        red.agregar_arista(s, "club_" + club, 1)

    partidos_vistos = set()
    for m in miembros:
        red.agregar_vertice("persona_" + m.nombre)
        if m.partido not in partidos_vistos:
            red.agregar_vertice("partido_" + m.partido)
            red.agregar_arista("partido_" + m.partido, t, limite)
            partidos_vistos.add(m.partido)
        red.agregar_arista("persona_" + m.nombre, "partido_" + m.partido, 1)

    for club, integrantes in clubes.items():
        for persona in integrantes:
            red.agregar_arista("club_" + club, "persona_" + persona, 1)

    flujos = flujo(red, s, t)

    resultado = {}
    for club, integrantes in clubes.items():
        for persona in integrantes:
            if flujos.get(("club_" + club, "persona_" + persona), 0) == 1:
                resultado[persona] = club
                break

    if len(resultado) < n:
        return None

    return resultado


"""5- Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una artista (por ejemplo, a una arista de capacidad 3 se le aumenta a 4), permita obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo implementado."""

# ---------------------------------------------------------------------------
# Helpers compartidos por obtener_nuevo_flujo
# ---------------------------------------------------------------------------


def _construir_predecesores(red):
    pred = {v: [] for v in red.obtener_vertices()}
    for v in red.obtener_vertices():
        for w in red.adyacentes(v):
            pred[w].append(v)
    return pred


def _bfs_camino_residual(red, flujos, pred, s, t):
    from collections import deque

    visitado = {s: None}
    cola = deque([s])

    while cola:
        v = cola.popleft()
        if v == t:
            break
        # Aristas forward: (v, w) con capacidad residual > 0
        for w in red.adyacentes(v):
            if w not in visitado and red.capacidad(v, w) - flujos.get((v, w), 0) > 0:
                visitado[w] = (v, True)
                cola.append(w)
        # Aristas backward: existe (w, v) con flujo > 0, se puede cancelar
        for w in pred.get(v, []):
            if w not in visitado and flujos.get((w, v), 0) > 0:
                visitado[w] = (v, False)
                cola.append(w)

    if t not in visitado:
        return None

    camino = []
    v = t
    while v != s:
        padre, forward = visitado[v]
        camino.append((padre, v, forward))
        v = padre
    camino.reverse()
    return camino


def _valor_flujo(flujos, s, red):
    return sum(flujos.get((s, w), 0) for w in red.adyacentes(s))


# ---------------------------------------------------------------------------


def obtener_nuevo_flujo(red, flujos, arista_aumentada, s, t):
    """
    Actualiza el flujo máximo al incrementar en 1 la capacidad de arista_aumentada.

    Parámetros:
        red              -- grafo con la capacidad de arista_aumentada ya incrementada
        flujos           -- dict (a,b)->flujo del flujo máximo previo (se modifica in-place)
        arista_aumentada -- tupla (u, v) cuya capacidad aumentó en 1
        s, t             -- fuente y sumidero

    Retorna: nuevo valor del flujo máximo.

    Justificación O(V + E):
        Si (u,v) no estaba saturada, el grafo residual no cambia → O(1).
        Si estaba saturada, el nuevo residual es el anterior más la arista (u,v) cap. 1.
        Cualquier nuevo camino aumentante DEBE usar esa arista (si hubiera otro, ya
        existía en el residual anterior y contradiría el flujo máximo previo).
        Un único BFS sobre el grafo residual encuentra ese camino (o confirma que no
        existe): O(V + E). La augmentación recorre el camino: O(V). Total: O(V + E).
    """
    u, v = arista_aumentada
    cap_nueva = red.capacidad(u, v)  # ya incrementada en 1
    f_uv = flujos.get((u, v), 0)

    # Si la arista no estaba saturada antes (f < cap_vieja = cap_nueva - 1),
    # el grafo residual no cambia y el flujo máximo tampoco.
    if f_uv < cap_nueva - 1:
        return _valor_flujo(flujos, s, red)

    # La arista estaba saturada: buscar camino aumentante en el nuevo residual.
    pred = _construir_predecesores(red)
    camino = _bfs_camino_residual(red, flujos, pred, s, t)

    if camino is None:
        return _valor_flujo(flujos, s, red)

    for a, b, forward in camino:
        if forward:
            flujos[(a, b)] = flujos.get((a, b), 0) + 1
        else:
            # Arista residual inversa: reducir flujo en la arista original (b, a)
            flujos[(b, a)] = flujos.get((b, a), 0) - 1

    return _valor_flujo(flujos, s, red)


"""9-Dado un grafo bipartito no dirigido, un match es un subconjunto de las aristas en el cual para todo vértice 
v
v a lo sumo una arista del match incide en 
v
v (en el match, tienen grado a lo sumo 1). Decimos que el vértice 
v
v está matcheado si hay alguna arista que incida en él (sino, está unmatcheado). El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad posible). Dar una metodología para encontrar el matching máximo de un grafo, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el matching máximo. ¿Cuál es el orden temporal de la solución implementada?"""


def matching_maximo(grafo):
    def _obtener_particion_bipartita(g):
        particion_1 = getattr(g, "particion_1", None)
        if particion_1 is not None:
            return set(particion_1), set(g.obtener_vertices()) - set(particion_1)

        from collections import deque

        color = {}
        for inicio in g.obtener_vertices():
            if inicio in color:
                continue
            color[inicio] = 0
            cola = deque([inicio])
            while cola:
                v = cola.popleft()
                for w in g.adyacentes(v):
                    if w not in color:
                        color[w] = 1 - color[v]
                        cola.append(w)
                    elif color[w] == color[v]:
                        raise ValueError("El grafo no es bipartito")

        u = {v for v, c in color.items() if c == 0}
        v = set(color) - u
        return u, v

    particion_1, particion_2 = _obtener_particion_bipartita(grafo)

    red = Grafo(dirigido=True)
    red.agregar_vertice("s")
    red.agregar_vertice("t")

    for v in grafo.obtener_vertices():
        red.agregar_vertice(v)

    for v in particion_1:
        red.agregar_arista("s", v, 1)
    for v in particion_2:
        red.agregar_arista(v, "t", 1)

    for v in particion_1:
        for w in grafo.adyacentes(v):
            if w in particion_2:
                red.agregar_arista(v, w, 1)

    flujos = flujo(red, "s", "t")

    matching = []
    for v in particion_1:
        for w in grafo.adyacentes(v):
            if w in particion_2 and flujos.get((v, w), 0) == 1:
                matching.append((v, w))

    return matching


"""10- Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). Dado un grafo dirigido y dos vértices 
s
s y 
t
t, encontrar el máximo número de caminos disjuntos s-t en G. Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. ¿Cuál es el orden temporal de la solución implementada? ¿Cómo resolverías el problema si el grafo fuera no dirigido?"""


def caminos_disjuntos(grafo, s, t):
    # Máximo número de caminos s-t disjuntos en aristas:
    # 1) poner capacidad 1 en cada arista
    # 2) calcular flujo máximo
    # 3) descomponer el flujo en caminos s-t
    red = Grafo(dirigido=True)
    for v in grafo.obtener_vertices():
        red.agregar_vertice(v)
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            red.agregar_arista(v, w, 1)

    flujos = flujo(red, s, t)
    activo = {}
    for arista, f in flujos.items():
        if f > 0:
            activo[arista] = f
    caminos = []

    while True:
        camino = _bfs_camino(activo, s, t, red)
        if camino is None:
            break
        caminos.append(camino)
        for i in range(len(camino) - 1):
            arista = (camino[i], camino[i + 1])
            activo[arista] -= 1
            if activo[arista] == 0:
                del activo[arista]

    return caminos


"""11 - Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de préstamos. ¿Cuál es el orden temporal de la solución implementada?"""


def asignar_libros(alumnos, libros):
    red = Grafo(dirigido=True)
    s = "s"
    t = "t"
    red.agregar_vertice(s)
    red.agregar_vertice(t)
    for alumno in alumnos:
        red.agregar_vertice(alumno)
        red.agregar_arista(s, alumno, 10)
    for libro in libros:
        red.agregar_vertice(libro)
        red.agregar_arista(libro, t, 3)
    for alumno in alumnos:
        for libro in alumno.libros_deseados:
            red.agregar_arista(alumno, libro, 1)
    flujos = flujo(red, s, t)
    asignacion = {}
    for alumno in alumnos:
        asignacion[alumno] = []
        for libro in alumno.libros_deseados:
            if flujos.get((alumno, libro), 0) == 1:
                asignacion[alumno].append(libro)
    return asignacion


"""12- Suponer que queremos schedulear cómo los aviones van de un aeropuerto a otro para cumplir sus horarios. Podemos decir que podemos usar un avión para un segmento/vuelo 
i
i y luego para otro 
j
j si se cumple alguna de las siguientes condiciones: a. El destino de 
i
i y el origen de 
j
j son el mismo. o b. Podemos agregar un vuelo desde el destino de 
i
i al origen de 
j
j con tiempo suficiente.

Decimos que el vuelo 
j
j es alcanzable desde el vuelo 
i
i si es posible usar el avión del vuelo 
i
i y después para el vuelo 
j
j.
Dados todos los vuelos con origen y destino, y el tiempo que tarda un avión entre cada par de ciudades queremos decidir: ¿Podemos cumplir con los m vuelos usando a lo sumo 
k
k aviones? Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se decide si es posible cumplir con la premisa. ¿Cuál es el orden temporal de la solución implementada?"""


def schedulear_vuelos(vuelos, tiempos, m, k):
    red = Grafo(dirigido=True)
    s = "s"
    t = "t"
    red.agregar_vertice(s)
    red.agregar_vertice(t)
    for i in range(m):
        red.agregar_vertice(i)
        red.agregar_arista(s, i, 1)
        red.agregar_arista(i, t, 1)
    for i in range(m):
        for j in range(m):
            if i != j and (
                vuelos[i].destino == vuelos[j].origen
                or tiempos[vuelos[i].destino][vuelos[j].origen]
                <= vuelos[j].hora_salida - vuelos[i].hora_llegada
            ):
                red.agregar_arista(i, j, 1)
    flujos = flujo(red, s, t)
    return sum(flujos.get((s, i), 0) for i in range(m)) <= k


"""13 - arlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. No se puede asumir que la ciudad tenga alguna forma en específico, por ejemplo, no hay que asumir que todas las calles sean cuadradas. Utilizando lo visto en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo."""


def enviar_hijos(ciudad, casa, escuela, hijos=5):
    red = Grafo(dirigido=True)
    s = casa
    t = escuela
    red.agregar_vertice(s)
    red.agregar_vertice(t)
    for esquina in ciudad.obtener_esquinas():
        red.agregar_vertice(esquina)
    for ady in ciudad.adyacentes(s):
        red.agregar_arista(s, ady, hijos)
    for ady in ciudad.adyacentes(t):
        red.agregar_arista(ady, t, hijos)
    for esquina in ciudad.obtener_esquinas():
        for adyacente in ciudad.adyacentes(esquina):
            red.agregar_arista(esquina, adyacente, 1)
    flujos = flujo(red, s, t)
    return (
        sum(flujos.get((s, esquina), 0) for esquina in ciudad.obtener_esquinas())
        >= hijos
    )
