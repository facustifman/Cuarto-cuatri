from ff import flujo
from grafo import Grafo

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
