"""Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario. De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). Se pide: a. una función de orden 
O(logn) que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests."""

def encontrar_cero(arr,izq, der):
    if izq > der:
        return -1  # No se encontró un 0

    mid = (izq + der) // 2
    
    if arr[mid] == 0:
        if mid == 0 or arr[mid - 1] == 1:
            return mid  # Se encontró el primer 0
        else:
            return encontrar_cero(arr, izq, mid - 1)  # Buscar en la mitad izquierda
    else:
        return encontrar_cero(arr, mid + 1, der)  # Buscar en la mitad derecha
    return -1  # No se encontró un 0

"""Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número 
n=25 debe devolver 5. Justificar la complejidad del algoritmo."""

def parte_entera_raiz(n):
    if n < 2:
        return n

    return _raiz_binaria(n, 0, n)

def _raiz_binaria(n, izq, der):
    if izq > der:
        return der

    mid = (izq + der) // 2
    cuadrado = mid * mid

    if cuadrado == n:
        return mid
    if cuadrado < n:
        return _raiz_binaria(n, mid + 1, der)
    return _raiz_binaria(n, izq, mid - 1)

"""Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro."""

def merge_sort(arr, izq, der):
    if izq >= der:
        return [arr[izq]]

    mid = (izq + der) // 2
    izquierda = merge_sort(arr, izq, mid)
    derecha = merge_sort(arr, mid + 1, der)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

""" Implementar una función, que utilice división y conquista, de complejidad O(log n), que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar la complejidad de la solución."""

def candidato_mayoritario(arr, izq, der):
    if izq == der:
        return arr[izq]

    medio = (izq + der) // 2

    candidato_izq = candidato_mayoritario(arr, izq, medio)
    candidato_der = candidato_mayoritario(arr, medio + 1, der)

    if candidato_izq == candidato_der:
        return candidato_izq

    cantidad_izq = contar(arr, candidato_izq, izq, der)
    cantidad_der = contar(arr, candidato_der, izq, der)

    if cantidad_izq > cantidad_der:
        return candidato_izq
    return candidato_der


def contar(arr, candidato, izq, der):
    if candidato is None:
        return 0

    cantidad = 0
    for i in range(izq, der + 1):
        if arr[i] == candidato:
            cantidad += 1
    return cantidad


def mas_de_la_mitad(arr):
    if not arr:
        return False

    candidato = candidato_mayoritario(arr, 0, len(arr) - 1)
    return contar(arr, candidato, 0, len(arr) - 1) > len(arr) // 2


"""Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad). Indicar y justificar su complejidad temporal.

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón."""

def alternar(arr):
    _alternar_rec(arr, 0, len(arr) - 1)
    return arr

def _alternar_rec(arr, izq, der):
    n = der - izq + 1
    if n <= 2:
        return

    m = n // 2
    for i in range(m // 2):
        arr[izq + m // 2 + i], arr[izq + m + i] = arr[izq + m + i], arr[izq + m // 2 + i]

    _alternar_rec(arr, izq, izq + m - 1)
    _alternar_rec(arr, izq + m, der)
    
    
"""Debido a la trágica situación actual, es necesario realizar tests para detectar si alguna persona está contagiada de COVID-19. El problema es que los insumos tienden a ser bastante caros, y no vivimos en un país al que los recursos le sobren.

Supongamos que por persona se toma más de una muestra (lo cual es cierto, pero a fines del ejercicio supongamos que son muchas muestras), y que podemos realizar un testeo a más de una persona al mismo tiempo mezclando las muestras (lo cual también es cierto): determinamos un conjunto de personas a testear, obtenemos una muestra de cada una de ellas, las “juntamos”, y al conjunto le realizamos el test. Si el test resulta negativo, implica que todas las personas testeadas en conjunto resultaron negativas. Si resulta positivo, implica que al menos una de las personas testedas resulta positiva.

Suponer que existe una función pcr(grupo), que devuelve true si al menos una persona del grupo es COVID-positivo, y false en caso contrario (los grupos pueden estar formados por 1 o más personas). Suponer que la positividad es extremadamente baja, e inclusive pueden suponer que va a haber una única persona contagiada (por simplicidad).

Implementar un algoritmo que dado un conjunto de n personas, devuelva la o las personas contagiadas, utilizando la menor cantidad de tests posibles (considerando la notación Big Oh). En dicha notación, ¿cuántos tests se estarán utilizando?

Pueden considerar que habrá una única persona contagiada, pero esto no cambiará el análisis a realizar."""

def pcr(grupo):
    pass
def encontrar_contagiado(personas, izq, der):
    if izq == der:
        return [personas[izq]] if pcr([personas[izq]]) else []

    mid = (izq + der) // 2
    grupo_izq = personas[izq:mid + 1]
    grupo_der = personas[mid + 1:der + 1]

    if pcr(grupo_izq):
        return encontrar_contagiado(personas, izq, mid)
    elif pcr(grupo_der):
        return encontrar_contagiado(personas, mid + 1, der)
    else:
        return []  # No hay contagiados en ninguno de los grupos
    
    
"""Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada."""

def raiz(func, a, b):
    if func(a) * func(b) > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo")
    mid = (a + b) / 2
    if abs(func(mid)) < 1e-7:  # Tolerancia para
        return mid
    elif func(a) * func(mid) < 0:
        return raiz(func, a, mid)
    else:
        return raiz(func, mid, b)
    

"""Sea una matriz A
n×n, con todos valores distintos. Un índice 
(i,j) es un máximo local si 
A[i,j] es estrictamente mayor que todos su vecinos que existan (arriba, abajo, izquierda, derecha). Implementar un algoritmo de División y Conquista que permita encontrar algún máximo local en tiempo 
O(n). Justificar adecuadamente la complejidad del algoritmo. Prestar mucha atención a la ecuación de recurrencia escrita, ya que esto puede develar un error en el algoritmo planteado."""

def maximo_local(matriz, izq, der, sup, inf):
    if izq > der or sup > inf:
        return None

    mid_col = (izq + der) // 2
    max_row = sup
    for i in range(sup, inf + 1):
        if matriz[i][mid_col] > matriz[max_row][mid_col]:
            max_row = i
            
    if (mid_col == 0 or matriz[max_row][mid_col] > matriz[max_row][mid_col - 1]) and \
       (mid_col == len(matriz[0]) - 1 or matriz[max_row][mid_col] > matriz[max_row][mid_col + 1]):
        return (max_row, mid_col)
    elif mid_col > 0 and matriz[max_row][mid_col - 1] > matriz[max_row][mid_col]:
        return maximo_local(matriz, izq, mid_col - 1, sup, inf)
    else:
        return maximo_local(matriz, mid_col + 1, der, sup, inf)
    
    
#! Parciales DYC

"""Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor xi. Todos los xi son valores diferentes.
Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta (es decir, los hijos
que tenga y su padre, si tiene). Implementar un algoritmo por división y conquista que obtenga algún mínimo local del árbol en
O(log n). Justificar apropiadamente la complejidad del algoritmo implementado.
Considerar que el árbol tiene en su estructura el nombre del nodo, su valor, y las referencias a sus hijos izquierdo y derecho."""

def encontrar_minimo_local(nodo):
    if nodo is None:
        return None
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo
    if nodo.izquierdo and nodo.izquierdo.valor < nodo.valor:
        return encontrar_minimo_local(nodo.izquierdo)
    if nodo.derecho and nodo.derecho.valor < nodo.valor:
        return encontrar_minimo_local(nodo.derecho)
    return nodo

"""Implementar una función que, dado un arreglo ordenado y sin repetidos de valores enteros no negativos, obtenga el mínimo valor que no se encuentre en el arreglo. Indicar y justificar adecuadamente la complejidad del algoritmo."""

def minimo_faltante(arr, izq, der):
    if izq > der:
        return izq
    
    mid = (izq + der) // 2
    if arr[mid] == mid:
        return minimo_faltante(arr, mid + 1, der)
    else:
        return minimo_faltante(arr, izq, mid - 1)
    
"""Sea A una matríz de n × n (con n ≥ 3) con todos valores diferentes. Definimos la vecindad de una celda como las 8 celdas vecinas
(arriba, abajo, derecha, izquierda, y las 4 diagonales), siempre que existan (en los bordes algunas no existirán). Un elemento A [i, j] es
un máximo local si su valor es estrictamente mayor que el valor de todas las celdas vecinas. Implementar un algoritmo de división y
conquista que encuentre un máximo local en tiempo O(n). Justificar adecuadamente la complejidad del algoritmo implementado."""

def maximo_local(matriz, izq, der, sup, inf):
    if izq > der or sup > inf:
        return None
    
    mid_col = (izq + der) // 2
    max_row = sup
    for i in range(sup, inf + 1):
        if matriz[i][mid_col] > matriz[max_row][mid_col]:
            max_row = i
            
    if (mid_col == 0 or matriz[max_row][mid_col] > matriz[max_row][mid_col - 1]) and \
       (mid_col == len(matriz[0]) - 1 or matriz[max_row][mid_col] > matriz[max_row][mid_col + 1]):
        return (max_row, mid_col)
    elif mid_col > 0 and matriz[max_row][mid_col - 1] > matriz[max_row][mid_col]:
        return maximo_local(matriz, izq, mid_col - 1, sup, inf)
    else:
        return maximo_local(matriz, mid_col + 1, der, sup, inf)