"""4- Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado."""


def charlas(horarios):
    # Ordenamos las charlas por su horario de fin
    horarios.sort(key=lambda x: x[1])
    seleccionadas = []
    ultimo_fin = -1

    for inicio, fin in horarios:
        if inicio >= ultimo_fin:
            seleccionadas.append((inicio, fin))
            ultimo_fin = fin

    return seleccionadas
