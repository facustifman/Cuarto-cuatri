"""3- Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.

"""


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


"""Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.

"""


def merge_sort(arr):
    return _merge_sort_rec(arr, 0, len(arr) - 1)


def _merge_sort_rec(arr, izq, der):
    if izq >= der:
        return [arr[izq]]

    mid = (izq + der) // 2
    izquierda = _merge_sort_rec(arr, izq, mid)
    derecha = _merge_sort_rec(arr, mid + 1, der)

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


"""9-Implementar una función (que utilice división y conquista) de complejidad O(n logn) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. Ejemplos:"""


def mas_de_la_mitad(arr):
    candidato = mas_de_la_mitad_rec(arr, 0, len(arr) - 1)
    return contar_ocurrencias(arr, candidato, 0, len(arr) - 1) > len(arr) // 2


def mas_de_la_mitad_rec(arr, izq, der):
    if izq == der:
        return arr[izq]

    mid = (izq + der) // 2
    izquierda = mas_de_la_mitad_rec(arr, izq, mid)
    derecha = mas_de_la_mitad_rec(arr, mid + 1, der)

    if izquierda == derecha:
        return izquierda

    count_izquierda = contar_ocurrencias(arr, izquierda, izq, der)
    count_derecha = contar_ocurrencias(arr, derecha, izq, der)

    if count_izquierda > (der - izq + 1) // 2:
        return True
    if count_derecha > (der - izq + 1) // 2:
        return True
    return False


def contar_ocurrencias(arr, num, izq, der):
    count = 0
    for i in range(izq, der + 1):
        if arr[i] == num:
            count += 1
    return count


"""7-Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con un orden de complejidad mejor que O(n^2). Justificar la complejidad del algoritmo mediante el teorema maestro.

"""


def puntos_mas_cercanos(puntos):
    if len(puntos) < 2:
        return float("inf"), None, None
    puntos.sort(key=lambda x: x[0])
    return _puntos_mas_cercanos_rec(puntos, 0, len(puntos) - 1)


def _puntos_mas_cercanos_rec(puntos, izq, der):
    if der - izq <= 3:
        return _puntos_mas_cercanos_bruto(puntos, izq, der)

    mid = (izq + der) // 2
    d_izquierda, p1_izq, p2_izq = _puntos_mas_cercanos_rec(puntos, izq, mid)
    d_derecha, p1_der, p2_der = _puntos_mas_cercanos_rec(puntos, mid + 1, der)

    d_min = min(d_izquierda, d_derecha)
    p1_min = p1_izq if d_izquierda < d_derecha else p1_der
    p2_min = p2_izq if d_izquierda < d_derecha else p2_der

    banda = [p for p in puntos if abs(p[0] - puntos[mid][0]) < d_min]
    banda.sort(key=lambda x: x[1])

    for i in range(len(banda)):
        for j in range(i + 1, min(i + 7, len(banda))):
            d = distancia(banda[i], banda[j])
            if d < d_min:
                d_min = d
                p1_min, p2_min = banda[i], banda[j]

    return d_min, p1_min, p2_min


def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def _puntos_mas_cercanos_bruto(puntos, izq, der):
    d_min = float("inf")
    p1_min = p2_min = None
    for i in range(izq, der + 1):
        for j in range(i + 1, der + 1):
            d = distancia(puntos[i], puntos[j])
            if d < d_min:
                d_min = d
                p1_min, p2_min = puntos[i], puntos[j]
    return d_min, p1_min, p2_min


"""8- Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente ordenado de menor a mayor. El arreglo B se encuentra desordenado. Indicar, por división y conquista, la cantidad de inversioes necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). Justificar la complejidad del algoritmo mediante el teorema maestro."""


def contar_inversiones(A, B):
    if len(A) != len(B):
        raise ValueError("Los arreglos deben tener la misma longitud")
    return _contar_inversiones_rec(A, B, 0, len(A) - 1)


def _contar_inversiones_rec(A, B, izq, der):
    if izq >= der:
        return 0

    mid = (izq + der) // 2
    inv_izquierda = _contar_inversiones_rec(A, B, izq, mid)
    inv_derecha = _contar_inversiones_rec(A, B, mid + 1, der)
    inv_merge = _contar_inversiones_merge(A, B, izq, mid, der)

    return inv_izquierda + inv_derecha + inv_merge


def _contar_inversiones_merge(A, B, izq, mid, der):
    i = izq
    j = mid + 1
    k = izq
    inversions = 0

    while i <= mid and j <= der:
        if B[i] <= B[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = B[j]
            inversions += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        A[k] = B[i]
        i += 1
        k += 1

    while j <= der:
        A[k] = B[j]
        j += 1
        k += 1

    return inversions


"""12- Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples). ¿Cual es la complejidad del algoritmo?"""


def alternar(arr):
    _alternar_rec(arr, 0, len(arr) - 1)
    return arr


def _alternar_rec(arr, izq, der):
    n = der - izq + 1
    if n <= 2:
        return

    m = n // 2
    for i in range(m // 2):
        arr[izq + m // 2 + i], arr[izq + m + i] = (
            arr[izq + m + i],
            arr[izq + m // 2 + i],
        )

    _alternar_rec(arr, izq, izq + m - 1)
    _alternar_rec(arr, izq + m, der)
