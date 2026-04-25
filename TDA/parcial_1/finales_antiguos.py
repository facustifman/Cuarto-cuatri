# PROBLEMAS CONOCIDOS:
#    - Scheduling/Juan el vago:
#        OPT[n] = max(OPT[n - 2] + ganancia(n), OPT[n - 1])
#    - Problema del cambio:
#        OPT[n] = 1 + min(OPT[n - i]), para todo i perteneciente al sistema monetario
#    - Problema de los n escalones/Formas distintas de dar cambio:
#        OPT[n] = \sum OPT[n - i], siendo i todos los escalones/billetes anteriores a n.
#    - Laberinto:
#        OPT[i][j] = matriz[i - 1][j - 1] + max(OPT[i - 1][j], OPT[i][j - 1])
#    - Teclado del telefono:
#        OPT[n][m] = \sum_{v = vecinos de m} OPT[n - 1][v]
#    - Mochila/Subset-sum:
#        OPT[n][W] = max(OPT[n - 1][W - peso(OPT[n][W])] + valor(OPT[n][W]), OPT[n - 1][W])
#    - Londres-California:
#        California:
#            OPT_C[n] = min(OPT_L[n - 1] + M, OPT_C[n - 1]) + C[n]
#        Londres:
#            OPT_L[n] = min(OPT_C[n - 1] + M, OPT_L[n - 1]) + L[n]
#    - Problema de la soga:
#        OPT[n] = max(max(i * (n - i), OPT[i] * OPT[n - i], OPT[i] * (i * n), i * OPT[n - 1]))
#    - Problema de Osvaldo:
#        OPT[n] = max(0, OPT[k - 1] + p[k] - p[k - 1])


# 4/11/24

"""1. Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
máxima y cuyo peso no exceda el valor de W."""


# objetos.valor y objetos.pesos
def mochila_agregado(objetos, K, W):
    mejor = []
    max_sol = [0]
    bt_mochila_agregado(objetos, mejor, max_sol, 0, [], 0, W, K)
    return mejor


def bt_mochila_agregado(
    objetos, mejor, max_sol, idx, actual, valor_actual, peso_actual, minimo_objetos
):
    if (len(objetos) - idx) + len(actual) < minimo_objetos:
        return

    if idx == len(objetos):
        if valor_actual > max_sol[0] and len(actual) >= minimo_objetos:
            mejor.clear()
            mejor.extend(actual)
            max_sol[0] = valor_actual
        return

    objeto = objetos[idx]

    if peso_actual - objeto.peso >= 0:
        actual.append(objeto)
        valor_actual += objeto.valor
        peso_actual -= objeto.peso
        bt_mochila_agregado(
            objetos,
            mejor,
            max_sol,
            idx + 1,
            actual,
            valor_actual,
            peso_actual,
            minimo_objetos,
        )
        actual.pop()
        valor_actual -= objeto.valor
        peso_actual += objeto.peso
    bt_mochila_agregado(
        objetos,
        mejor,
        max_sol,
        idx + 1,
        actual,
        valor_actual,
        peso_actual,
        minimo_objetos,
    )


"""3. Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
es la de maximizar la ganancia dada por p[k] − p[j].
Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. Indicar y
justificar la complejidad del algoritmo implementado."""

# * La ecuacion de recurrencia es: opt[k]= max(0, OPT[k - 1] + p[k] - p[k - 1])


def osvaldo(p):
    opt = [0] * len(p)
    for i in range(len(p)):
        opt[i] = max(0, opt[i - 1] + p[i] - p[i - 1])

    return opt


"""5. Resolver el problema de Osvaldo (ejercicio 3) pero por división y conquista. Indicar y justificar adecuadamente la
complejidad del algoritmo implementado. Es probable que la complejidad de ambas soluciones no quede igual, no te
estreses por ello."""


# Solución divide y conquista limpia
# T(n) = 2T(n/2) + O(n)  →  O(n log n) por Teorema Maestro (caso 2, a=2, b=2, f(n)=O(n))
def osvaldo_dyc_sol(p, izq=None, der=None):
    if izq is None:
        izq = 0
    if der is None:
        der = len(p) - 1

    # Caso base: un solo día, no se puede comprar y vender
    if izq >= der:
        return 0

    mid = (izq + der) // 2

    ganancia_izq = osvaldo_dyc_sol(p, izq, mid)
    ganancia_der = osvaldo_dyc_sol(p, mid + 1, der)

    # Caso cruzado: comprar en la mitad izquierda, vender en la derecha
    # El mejor cruce es siempre el mínimo de la izquierda y el máximo de la derecha
    min_compra = min(p[izq : mid + 1])
    max_venta = max(p[mid + 1 : der + 1])
    ganancia_cross = max(0, max_venta - min_compra)

    return max(ganancia_izq, ganancia_der, ganancia_cross)


# 19/02/24


"""1. Imaginá que estamos organizando un torneo de guardias en un castillo. El castillo tiene un suelo dividido en una
cuadrícula de tamaño n x m, y cada celda puede estar ocupada por un guardia o estar vacía. Los guardias tienen la
habilidad de vigilar todas las celdas adyacentes a su posición, incluidas las diagonales, es decir, pueden ver las celdas
vecinas que están justo al lado, arriba, abajo, a la izquierda, a la derecha o en las esquinas.
Se nos pide colocar la mayor cantidad posible de guardias en el castillo sin que ninguno pueda vigilar a otro. Esto
significa que no podemos colocar dos guardias en celdas adyacentes, ya que estarían vigilándose mutuamente.
Implementar un algoritmo greedy que permita colocar el mayor número posible de guardias en el castillo sin que se
vigilen entre sí. Indicar y justificar la complejidad del algoritmo. Indicar por qué se trata, en efecto, de un algoritmo
greedy. El algorimto, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo."""


def colocar_guardias(matriz):
    celdas_vistas = set()
    colocacion = []
    for n in range(len(matriz)):
        for m in range(len(matriz[0])):
            if puedo_colocar(matriz, celdas_vistas, n, m):
                colocacion.append((n, m))
                agregar_celdas(n, m, celdas_vistas)

    return colocacion


def puedo_colocar(celdas_vistas, n, m):
    return (n, m) not in celdas_vistas


def agregar_celdas(n, m, celdas_vistas):
    for i in range(n - 1, n + 2):
        for j in range(m - 1, m + 2):
            celdas_vistas.add((i, j))


"""2. Implementar un algoritmo que, utilizando backtracking, resuelva el problema del cambio (obtener la forma de dar
cambio en la mínima cantidad de monedas) con una nueva restricción: no se tiene una cantidad indefinida de cada
moneda, sino una cantidad específica (y esto hace que pueda no haber solución). Suponer que la función a invocar
es cambio(n, monedas, cantidad_x_monedas), donde n sea el valor a devolver en cambio, monedas sea una lista
ordenada de los valores de las monedas, y cantidad_x_monedas un diccionario."""


def cambio(n, monedas, cantidad_monedas):
    min_monedas = [float("inf")]
    monedas.sort(reverse=True)
    mejor = {}
    bt_cambio(n, monedas, cantidad_monedas, min_monedas, mejor, {}, 0, 0)
    return mejor


def bt_cambio(
    cambio_a_devolver,
    monedas,
    cantidad_monedas,
    min_monedas,
    mejor,
    actual,
    cantidad_actual,
    idx,
):
    if idx == len(monedas):
        return
    if cambio_a_devolver == 0:
        if cantidad_actual < min_monedas[0]:
            min_monedas[0] = cantidad_actual
            mejor.clear()
            mejor.update(actual)
            return

    moneda = monedas[idx]
    if puedo_utilizar(moneda, cantidad_monedas, cambio_a_devolver):
        cantidad_monedas[moneda] -= 1
        cambio_a_devolver -= moneda
        if moneda in actual:
            actual[moneda] += 1
        else:
            actual[moneda] = 1
        cantidad_actual += 1
        bt_cambio(
            cambio_a_devolver,
            monedas,
            cantidad_monedas,
            min_monedas,
            mejor,
            actual,
            cantidad_actual,
            idx + 1,
        )
        bt_cambio(
            cambio_a_devolver,
            monedas,
            cantidad_monedas,
            min_monedas,
            mejor,
            actual,
            cantidad_actual,
            idx,
        )
        cantidad_monedas[moneda] += 1
        cantidad_actual -= 1
        cambio_a_devolver += moneda
        actual[moneda] -= 1
    bt_cambio(
        cambio_a_devolver,
        monedas,
        cantidad_monedas,
        min_monedas,
        mejor,
        actual,
        cantidad_actual,
        idx + 1,
    )


def puedo_utilizar(moneda, cantidad_monedas, cambio_a_devolver):
    if cantidad_monedas[moneda] > 0 and cambio_a_devolver - moneda >= 0:
        return True
    return False


"""4. Contamos con una lista de n coordenadas satelitales (latitud-longitud) que conforman un polígono convexo, ordenadas
en sentido antihorario. Queremos mostrar toda el área interior del polígono con el mayor tamaño posible en nuestra
pantalla rectangular de la computadora. El programa que muestra el mapa acepta como parámetros 2 coordenadas para
construir el rectángulo a mostrar: los correspondientes a los límites inferior izquierdo y superior derecho, tal que toda
la imagen quede dentro de los límites. Implementar un algoritmo que resuelva el problema con complejidad O(log n).
Justificar adecuadamente la complejidad del algoritmo implementado."""
