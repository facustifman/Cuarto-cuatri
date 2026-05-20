import pulp

def juan_el_vago(trabajos):
    # devolver un arreglo de los índices de días a trabajar
    n = len(trabajos)
    if n == 0:
        return []

    prob = pulp.LpProblem("juan_el_vago", pulp.LpMaximize)

    # x[i] = 1 si Juan trabaja el día i, 0 si no
    x = [pulp.LpVariable(f"x_{i}", cat="Binary") for i in range(n)]

    # Maximizar ganancia total
    prob += pulp.lpSum(trabajos[i] * x[i] for i in range(n))

    # No puede trabajar dos días consecutivos
    for i in range(n - 1):
        prob += x[i] + x[i + 1] <= 1

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    return [i for i in range(n) if pulp.value(x[i]) == 1]

def vertex_cover_min(grafo):
    # grafo: instancia de Grafo (no dirigido)
    # devuelve lista de vértices que forman el mínimo vertex cover
    vertices = grafo.obtener_vertices()
    # aristas sin duplicados (cada par una sola vez)
    aristas = set()
    for u in vertices:
        for v in grafo.adyacentes(u):
            aristas.add((min(u, v), max(u, v)))

    prob = pulp.LpProblem("vertex_cover_min", pulp.LpMinimize)

    # x[v] = 1 si el vértice v está en el cover
    x = {v: pulp.LpVariable(f"x_{v}", cat="Binary") for v in vertices}

    # Minimizar cantidad de vértices en el cover
    prob += pulp.lpSum(x[v] for v in vertices)

    # Para toda arista (u,v), al menos uno de los extremos debe estar en el cover
    for u, v in aristas:
        prob += x[u] + x[v] >= 1

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    return [v for v in vertices if pulp.value(x[v]) == 1]