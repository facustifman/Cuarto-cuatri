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
