"""11- Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

(i) aumentar el valor del operando en 1;

(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'"""

# Ecuacion de recurrencia:
#   dp[0] = 0
#   dp[1] = 1
#   dp[i] = 1 + min(dp[i-1], dp[i//2])  si i es par
#   dp[i] = 1 + dp[i-1]                  si i es impar
#
# Complejidad: O(K) tiempo y O(K) espacio — se llena una tabla de tamaño K+1
# con trabajo O(1) por celda, y la reconstruccion recorre a lo sumo K pasos.
def operaciones(k):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        dp[i] = 1 + dp[i - 1]
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 2])

    ops = []
    i = k
    while i > 0:
        if i % 2 == 0 and dp[i] == 1 + dp[i // 2]:
            ops.append('por2')
            i //= 2
        else:
            ops.append('mas1')
            i -= 1
    return ops[::-1]


"""14- Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto."""

# La calle es circular: casas 0 y n-1 son vecinas, no se pueden robar juntas.
# Se resuelven dos subproblemas lineales y se toma el mejor:
#   A) casas 0..n-2  B) casas 1..n-1
# Recurrencia lineal:
#   dp[0] = g[0],  dp[1] = max(g[0], g[1])
#   dp[i] = max(dp[i-2] + g[i], dp[i-1])
# Complejidad: O(n) tiempo y espacio.
# dp[i]= max(dp[i-2] +g[i] , dp[i-1])
def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    if n == 1:
        return [0]
    c_1, gan1 = robos(ganancias, 0)
    c_2, gan2 = robos(ganancias, 1)
    return gan1 if c_1 >= c_2 else gan2

def robos(ganancia, casa):
    # casa=0: excluye la ultima casa → usa ganancia[0..n-2], offset=0
    # casa=1: excluye la primera casa → usa ganancia[1..n-1], offset=1
    if casa == 0:
        g = ganancia[:-1]
        offset = 0
    else:
        g = ganancia[1:]
        offset = 1

    n = len(g)
    if n == 0:
        return 0, []

    dp = [0] * n
    dp[0] = g[0]
    if n > 1:
        dp[1] = max(g[0], g[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + g[i], dp[i - 1])

    rec = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            rec.append(i + offset)
            i -= 2
        else:
            i -= 1
    return dp[n - 1], rec[::-1]