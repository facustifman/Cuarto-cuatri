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
