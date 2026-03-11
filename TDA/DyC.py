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
