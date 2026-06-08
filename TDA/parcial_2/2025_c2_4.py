"""1. El 2-Partition Problem como problema de optimización se describe tal que: Dado un conjunto de n números positivos T =
{T1, T2, . . . , Tn}, se particionan los números en dos subconjuntos S1 y S2 (con intersección vacía y unión = T) de forma de minimizar
la sumatoria de cualquiera de los subconjuntos (mın m ́ax(S1, S2)).
Implementar un modelo de programación lineal que dados los valores de los Ti nos permita obtener la asignación óptima para S1
y S2. Indicar la cantidad de inecuaciones definidas en el modelo.

Variables:
  Xi ∈ {0,1} para i=1..n: Xi=1 significa Ti ∈ S1, Xi=0 significa Ti ∈ S2.
  M ≥ 0: variable auxiliar que representa el máximo entre las dos sumas.

Obj: min M

Restricciones:
  M >= Σ Ti * Xi              (M acota la suma de S1)
  M >= Σ Ti * (1 - Xi)        (M acota la suma de S2)

  Como minimizamos M y estas dos inecuaciones lo pisan desde abajo,
  el modelo fuerza M = max(suma(S1), suma(S2)).

Dominio:
  0 <= Xi <= 1   para i=1..n

Cantidad de inecuaciones:
  2 restricciones principales + 2n de dominio = O(n)
  Las 2 centrales son las únicas que importan en términos del modelo.

(!) Error del modelo anterior: poner x_i * T_i <= y elemento a elemento
    minimiza el máximo elemento individual, no la suma de cada subconjunto.
    La restricción debe ser sobre la SUMA total de cada subconjunto.
"""

"""2. Tito trabaja para la mafia. Debe llevar en camiones de caudales el dinero recaudado por la organización a modo de devolver favores a
diferentes estaciones de policía. Entre diferentes rutas puede tener que cambiar de camión (para no ser fácilmente detectado), donde
cada camión puede tener diferente capacidad. Además, en algunos puntos (escondites de la mafia) puede recoger más dinero.
Tito entonces cuenta con un grafo dirigido con las diferentes rutas, y puntos donde pueda tener que ir cambiando de camión según
como cambie de ruta. El grafo es pesado y las aristas tienen como peso la capacidad del camión de caudales a usar por esa ruta. En
cada vértice tenemos un punto donde podría (o no) poder recoger dinero o tener que dejar un agradecimiento, lo cual está modelado
con un valor w(v) (si es positivo, al pasar por allí podemos recoger dinero, si es negativo es que debemos dejar un agradecimiento,
si es 0, es simplemente un punto de cambio de camión y nada más). Tito puede comenzar cada recorrido desde donde desee, si
bien tiene sentido ir empezando desde algún escondite. Usando redes de flujo, implementar un algoritmo que reciba dicho grafo y
determine si es posible pagar todos los agradecimientos correspondientes. No es necesario indicar cómo serían los recorridos. Indicar y
justificar la complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo.

"""

def es_posible_pagar_agradecimientos(grafo, w):
    red = RedDeFlujo()
    fuente = 'fuente'
    sumidero = 'sumidero'
    red.agregar_vertice(fuente)
    red.agregar_vertice(sumidero)
    for v in grafo:
        if w[v] > 0:
            red.agregar_arista(fuente, v, w[v])  # Capacidad igual al dinero que se puede recoger
        elif w[v] < 0:
            red.agregar_arista(v, 'sumidero', -w[v])  # Capacidad igual al agradecimiento a pagar
    for u in grafo:
        for v in grafo[u]:
            red.agregar_arista(u, v, grafo[u][v])  # Capacidad según el camión disponible en la ruta
    flujo = red.calcular_flujo_maximo(fuente, sumidero)
    total_agradecimientos = sum(-w[v] for v in grafo if w[v] < 0)
    flujo_maximo = sum(f for (v,w), f in flujo.items() if w == sumidero)  # Flujo total que llega al sumidero
    
    return flujo_maximo == total_agradecimientos

#la complejidad del algoritmo depende de la implementación del cálculo de flujo máximo. Si usamos el algoritmo de Edmonds-Karp, la complejidad sería O(V * E^2), donde V es el número de vértices y E el número de aristas en la red de flujo. Dado que la red tiene O(n) vértices (donde n es el número de vértices en el grafo original) y O(n^2) aristas (en el peor caso, cada vértice puede estar conectado a todos los demás), la complejidad total sería O(n^5).

"""3. El problema de Coloreo de Boquita se enuncia como: Dado un Grafo donde cada vértice tiene un peso w(v) positivo, se desea pintar
cada vértice de un color diferente de entre 4 posibilidades: Azul, Amarillo, Rojo o Blanco. Ningún vértice puede tener el mismo color
de un adyacente. Aquellos vértices pintados con Rojo o Blanco nos dan como penalidad el peso de dicho vértice (los pintados de Azul
o Amarillo no nos dan ninguna penalidad). Si excedemos un valor K en penalidad, nos vamos a la B. Dado un grafo y un valor K, ¿es
posible pintar a los vértice, tal que ningún par de adyacentes compartan color (entre los 4 colores disponibles), y que la suma de las
penalidades obtenidas sea a lo sumo K, de forma de no irnos a la B?
Demostrar que el problema de Coloreo de Boquita es un problema NP-Completo. Recomendamos recordar que 4-Coloreo es un
problema NP-Completo.

--- Demostración ---

1. Coloreo de Boquita ∈ NP:
   Certificado: la asignación de colores a cada vértice.
   Verificación en poly: recorrer todas las aristas y chequear que los extremos tienen
   colores distintos, y sumar las penalidades de vértices Rojo/Blanco y verificar ≤ K. O(V+E). ✓

2. Coloreo de Boquita es NP-Hard: reducción desde 4-Coloreo (4C ≤p Boquita).

   Construcción:
   Dado un grafo G = (V, E) instancia de 4-Coloreo, construyo la instancia de Boquita:
     - G' = G  (mismo grafo, mismos vértices y aristas)
     - w(v) = 1 para todo v ∈ V
     - K = |V|  (= n, la suma de todos los pesos)

   La reducción es trivial: O(V). La instancia de Boquita es (G', w, K).

   Corrección (doble implicancia):

   (→) Si G tiene un 4-coloreo válido c: V → {Azul, Amarillo, Rojo, Blanco},
       uso el mismo coloreo en G'. Como c es válido para 4-Coloreo, ningún par de
       adyacentes comparte color. La penalidad es a lo sumo Σ w(v) = n = K.
       Entonces G' tiene una solución Boquita con penalidad ≤ K. ✓

   (←) Si G' tiene una solución Boquita con penalidad ≤ K = n,
       el coloreo asignado usa los 4 colores disponibles (Azul, Amarillo, Rojo, Blanco)
       sin que ningún par de adyacentes comparta color.
       Entonces ese mismo coloreo es un 4-coloreo válido de G. ✓

   (!) Error de la reducción con K=0: si K=0 ningún vértice puede ser Rojo ni Blanco,
       por lo que solo quedan 2 colores (Azul y Amarillo). Eso reduce a 2-Coloreo
       (grafos bipartitos), que es fácil, no a 4-Coloreo.
       La clave es poner K = n para que la restricción de penalidad sea vacuamente
       satisfecha y el único requisito sea el coloreo válido con 4 colores.

   Queda demostrado que 4C ≤p Boquita. Como 4-Coloreo es NP-Completo, Boquita también lo es.
"""

