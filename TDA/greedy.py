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


"""6-Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar"""


def cambio(monedas, monto):
    monedas.sort(reverse=True)  # Ordenamos las monedas de mayor a menor valor
    resultado = []
    for moneda in monedas:
        while monto >= moneda:
            resultado.append(moneda)
            monto -= moneda
    return resultado


"""8-Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar"""


# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    peso_restante = W
    valor_total = 0
    elementos.sort(key=lambda x: x[0] / x[1], reverse=True)
    seleccionados = []
    for valor, peso in elementos:
        if peso <= peso_restante:
            seleccionados.append((valor, peso))
            valor_total += valor
            peso_restante -= peso
    return seleccionados, valor_total

#* La complejidad del algoritmo es O(n log n) debido a la ordenación de los elementos por su valor/peso, y luego O(n) para iterar sobre los elementos seleccionados. El algoritmo no siempre encuentra la solución óptima, ya que se basa en una heurística de valor/peso que puede no ser la mejor opción en todos los casos. Por ejemplo, si hay un elemento con un valor muy alto pero un peso también muy alto, el algoritmo podría no seleccionarlo aunque sea la mejor opción para maximizar el valor total. Se trata de un algoritmo Greedy porque toma decisiones basadas en la mejor opción local (valor/peso) sin considerar las consecuencias a largo plazo, lo que puede llevar a soluciones subóptimas.


"""9- Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline. Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia. Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. Es decir, dados los arreglos de: T tiempo de duraciones de las tareas y L representando al deadline de cada tarea, si definimos que una tarea i empieza en S_i, entonces termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0).
Nuestra latencia máxima será aquella i que maximice el valor L_i.
Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente. Indicar y justificar la complejidad del algoritmo implementado.
Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique: (el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar"""

def minimizar_latencia(L_deadline, T_tareas):
    tareas = list(zip(T_tareas, L_deadline))
    tareas.sort(key=lambda x: x[1])  # Ordenamos por deadline
    orden = []
    tiempo_acumulado = 0

    for duracion, deadline in tareas:
        tiempo_acumulado += duracion
        latencia = max(0, tiempo_acumulado - deadline)
        orden.append((duracion, latencia))

    return orden

#* La complejidad del algoritmo es O(n log n) debido a la ordenación de las tareas por su deadline, y luego O(n) por recorrer los elementos para calcular la latencia. El algoritmo no siempre encuentra la solución óptima, ya que se basa en una heurística de ordenar por deadline, lo que puede no ser la mejor opción en todos los casos. Por ejemplo, si hay una tarea con un deadline muy cercano pero una duración muy larga, el algoritmo podría no seleccionarla aunque sea la mejor opción para minimizar la latencia máxima. Se trata de un algoritmo Greedy porque toma decisiones basadas en la mejor opción local (ordenar por deadline) sin considerar las consecuencias a largo plazo, lo que puede llevar a soluciones subóptimas.

"""11- Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""


def bolsas(capacidad, productos):
    productos.sort(reverse=True)  # Ordenamos los productos de mayor a menor peso
    bolsas = []
    for producto in productos:
        colocado = False
        for bolsa in bolsas:
            if sum(bolsa) + producto <= capacidad:
                bolsa.append(producto)
                colocado = True
                break
        if not colocado:
            bolsas.append([producto])  # Creamos una nueva bolsa para el producto
    return bolsas

"""12- El mafioso arnook, hay que ordenar por km finales y que no se pisen los inicios, """
#los pedidos son(inicio, fin)
def asignar_mafias(pedidos):
    pedidos.sort(key=lambda x: x[1])  # Ordenamos los pedidos por su horario de fin
    seleccionados = []
    ultimo_fin = -1

    for inicio, fin in pedidos:
        if inicio >= ultimo_fin:
            seleccionados.append((inicio, fin))
            ultimo_fin = fin

    return seleccionados


"""
13- Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?"""
def cobertura(casas, R, K):
    kilometros_recorridos = 0
    antenas = []
    casas.sort()
    for casa in casas:
        if casa > kilometros_recorridos:
            antenas.append(casa + R)
            kilometros_recorridos = casa + 2 * R
    return antenas

#* La complejidad del algoritmo es O(n log n) debido a la ordenación de las casas, y luego O(n) para iterar sobre las casas y determinar dónde colocar las antenas. Se trata de un algoritmo Greedy porque toma decisiones basadas en la mejor opción local (colocar una antena en la casa más cercana que aún no tiene cobertura) sin considerar las consecuencias a largo plazo, lo que puede llevar a soluciones subóptimas. El algoritmo no siempre da la solución óptima, ya que puede haber casos donde colocar una antena en una casa específica no sea la mejor opción para minimizar el número total de antenas necesarias. Por ejemplo, si hay varias casas muy cercanas entre sí, el algoritmo podría colocar una antena en cada una de ellas, aunque una sola antena podría cubrir todas esas casas si se colocara estratégicamente.

