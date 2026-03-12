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


"""11- Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""


def bolsas(capacidad, productos):
    productos.sort(reverse=True)  # Ordenamos los productos de mayor a menor peso
    bolsas = []
    pesos_actuales = []
    for peso in productos:
        if len(bolsas) == 0:
            bolsas.append([peso])
            pesos_actuales.append(peso)
            continue
        for i in range(len(bolsas)):
            if pesos_actuales[i] + peso <= capacidad:
                bolsas[i].append(peso)
                pesos_actuales[i] += peso
                break
            else:
                bolsas.append([peso])
                pesos_actuales.append(peso)

    return bolsas
