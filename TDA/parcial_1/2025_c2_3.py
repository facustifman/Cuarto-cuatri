"""1. Implementar un algoritmo de división y conquista que reciba un arreglo de K arreglos/listas ordenadas, cada una de H elementos
(es decir, en total hay n = K*H elementos) y devuelva un arreglo con todos los elementos, ya ordenados. El algoritmo debe utilizar la
información del enunciado para considerarse aprobable. NO utilizar un heap para resolver el problema, se está evaluando división y
conquista.
Una vez implementado, puede que no sea posible utilizar el Teorema Maestro para calcular su complejidad. Explicar por qué es el caso.
Dar cuál sería la complejidad con una breve justificación (no es necesario hacer una demostración). En caso que tu implementación sí
permita calcular su complejidad con el Teorema Maestro, recomendamos revisar que esté bien hecho y, si lo está, dar su complejidad
dada por el teorema."""


def merge_dos(a, b):
    resultado = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


def merge_k_ordenados(arreglos):
    if len(arreglos) == 1:
        return arreglos[0]

    mid = len(arreglos) // 2
    izq = merge_k_ordenados(arreglos[:mid])
    der = merge_k_ordenados(arreglos[mid:])
    return merge_dos(izq, der)


"""2. El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un laboratorio
farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un catálogo del valor de
cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad disponible (medible en ml). Rizzoli
sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo bueno es que sabe que puede fraccionar y poner
proporciones de los fármacos; y en ese caso lo vendería en su valor proporcional. Implementar un algoritmo greedy que obtenga los
fármacos (y cantidades) que Rizzoli debe robarse para obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta
familia no se aceptan los robos a medias). Justificar por qué el algoritmo propuesto es Greedy y por qué es, en efecto, óptimo. Indicar
y justificar la complejidad del algoritmo implementado."""


def robo(farmacos, L):
    farmacos.sort(lambda x: x.valor / x.cantidad, reverse=True)
    resultado = []
    liquido_restante = L
    for i in farmacos:
        if i.cantidad <= liquido_restante:
            resultado.append((i, i.cantidad))
            liquido_restante -= i.cantidad
        elif i.cantidad > liquido_restante and liquido_restante != 0:
            resultado.append((i, liquido_restante))
            liquido_restante = 0
            break
    return resultado


# * El algoritmo es Greedy porque en cada decision que se toma busca un optimo local al utilizar la regla de agarrar el que mayor valor/cantidad te da. El algoritmo es optimo porque su construccion se basa en ganancia = valor/cantidad , eso hace que los mas convenientes de agarrar sean siempre los que se muestran al prinicipio del arreglo, por consecuente el liquido restante que se agarra al final es el siguiente en su ganancia.


"""3. El problema conocido como Feedback Edge Set (FES) (cómo problema de optimización) indica: Dado un grafo dirigido, obtener la
menor cantidad de aristas a eliminar de dicho grafo de tal manera que el grafo quede acíclico.
Implementar un algoritmo que, por backtracking, resuelva el problema. Podés considerar que existe una función tiene_ciclo(grafo,
vértices) que devuelve true si el grafo tiene algún ciclo en la componente débilmente conexa definida por los vértices pasados por
parámetro, y también la función componentes_debilmente_conexas(grafo, vertices) que devuelve una lista de listas, cada una
con una componente débilmente conexa del grafo entre los vértices definidos por parámetro."""


def fes(grafo):
    mejor = []
    min_sol = [0]
    vertices = grafo.obtener_vertices()
    bt_fes(grafo, vertices, mejor, min_sol, [], 0, 0)
    return mejor


def bt_fes(grafo, vertices, mejor, min_sol, actual, cant_actual, idx):
    if idx == len(vertices):
        for i in componentes_debilmente_conexas(grafo, actual):  # type: ignore
            if tiene_ciclos(grafo, i):  # type: ignore
                return
        if cant_actual < min_sol[0]:
            min_sol[0] = cant_actual
            mejor.clear()
            mejor.extend(actual)

    vertice = vertices[idx]
    for w in grafo.adyacentes(vertice):
        actual.append()


def fes(grafo, vertices):
    mejor = []  # peor caso posible
    _bt(grafo, vertices, [], mejor)
    return mejor[0]


def _bt(grafo, vertices, eliminadas, mejor):
    if len(eliminadas) >= len(mejor[0]):
        return

    for comp in componentes_debilmente_conexas(grafo, vertices):  # type: ignore
        if tiene_ciclo(grafo, comp):  # type: ignore
            for v in comp:
                for w in grafo.adyacentes(v):
                    if w in comp:
                        grafo.eliminar_arista(v, w)
                        eliminadas.append((v, w))
                        _bt(grafo, vertices, eliminadas, mejor)
                        eliminadas.pop()
                        grafo.agregar_arista(v, w)
            return

    mejor[0] = list(eliminadas)
