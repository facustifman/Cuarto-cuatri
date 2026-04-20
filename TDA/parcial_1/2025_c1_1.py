"""1. Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor xi

. Todos los xi son valores diferentes.
Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta (es decir, los hijos
que tenga y su padre, si tiene). Implementar un algoritmo por división y conquista que obtenga algún mínimo local del árbol en
O(log n). Justificar apropiadamente la complejidad del algoritmo implementado.
Considerar que el árbol tiene en su estructura el nombre del nodo, su valor, y las referencias a sus hijos izquierdo y derecho.
"""

from multiprocessing.heap import Heap


def minimo_local(raiz):
    if raiz == None:
        return None

    # Caso hoja: es siempre mínimo local
    if raiz.izq == None and raiz.der == None:
        return raiz

    # Si ambos hijos existen y son MAYORES, la raíz es mínimo local
    if (
        raiz.izq != None
        and raiz.izq.valor > raiz.valor
        and raiz.der != None
        and raiz.der.valor > raiz.valor
    ):
        return raiz

    # Si al menos un hijo es menor, recurse hacia ese lado
    if raiz.izq != None and raiz.izq.valor < raiz.valor:
        return minimo_local(raiz.izq)
    else:
        return minimo_local(raiz.der)


"""2. El explorador Roberto se embarcó en una misión para encontrar el legendario Templo de los Vientos. En el vasto desierto, hay oasis
donde puede recoger provisiones esenciales como agua y comida. Cada oasis tiene recursos limitados. Sin suficientes provisiones,
Roberto no podrá cruzar el desierto. Sólo vamos a considerar el hecho de tener k cantidad de provisiones (no si son una cosa u otra).
Implementar un algoritmo greedy que permita a Roberto llegar al templo con la menor cantidad de paradas posibles en los oasis.
Indicar y justificar la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución
óptima? Si lo hace, justificar, si no dar un contraejemplo. Datos que se reciben:
Una lista de n elementos que nos indica cuántas provisiones (en cantidad) se pueden conseguir en cada uno de los n oasis.
Una lista con las distancias del inicio de la travesía al primer oasis, del primero al segundo, del segundo al tercero, y así hasta el
final de la travesía (la lista tiene n + 2 elementos).
La cantidad de provisiones iniciales de Roberto.
Una constante KM_PROVISION que indica cuántas provisiones se debe consumir para caminar un KM."""


def camino_al_templo(provisiones_iniciales, oasis, distancias, KM_PROVISION):
    paradas = 0
    provisiones_actuales = provisiones_iniciales
    oasis_visitados = Heap()
    for i in range(len(oasis)):
        oasis_visitados.push(oasis[i])
        if provisiones_actuales < distancias[i] * KM_PROVISION:
            if oasis_visitados.is_empty():
                return -1  # No hay oasis para reabastecer
            mejor_oasis = oasis_visitados.pop()  # Oasis con más provisiones
            provisiones_actuales += mejor_oasis
            paradas += 1
            if provisiones_actuales < distancias[i] * KM_PROVISION:
                return -1  # Aún no es suficiente para llegar al siguiente oasis
        provisiones_actuales -= distancias[i] * KM_PROVISION
    return paradas


# * La complejidad del algoritmo es O(n log n) debido a la gestión de la estructura de datos Heap para mantener los oasis visitados. El algoritmo es Greedy porque en cada paso toma la decision local de reabastecer en el oasis con mas provisiones disponibles, buscando minimizar el numero de paradas. El algoritmo no siempre da la solucion optima, ya que puede haber casos donde reabastecer en un oasis con menos provisiones pero mas cercano al siguiente oasis pueda ser mejor a largo plazo. Por ejemplo, si el primer oasis tiene 10 provisiones y el segundo tiene 5, pero el segundo está mucho más cerca del siguiente oasis, podría ser mejor reabastecer en el segundo oasis para evitar una parada adicional en el futuro.
