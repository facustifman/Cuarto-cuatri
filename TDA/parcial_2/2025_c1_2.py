"""1. Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar
la máxima cantidad de charlas a dar de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas.
Implementar un modelo de programación lineal que resuelva el problema de Interval Scheduling. Indicar la cantidad de
inecuaciones definidas en el modelo. Pueden asumir que hay una función solapamientos(intervalo), que da todos los intervalos que
se solapan con el intervalo, y la pueden usar en el modelo.

variables:
Xi: se da o no se da la charla

Obj = max(sum(Xi)) Quiero maximizar la sumatoria de las charlas a dar
Xi + Xj < 1 para todo Xj devuelto por la función solapamientos(Xi), para todo Xi perteneciente al intervalo de charlas

Complejidad: se tiene N inecuaciones por cada intervalo considerando el peor caso de que todos coinciden

"""



"""2. Tenemos un grafo no dirigido que representa una grilla de n × n. Definimos que un vértice en la fila i y columna j es el vértice (i, j).
Todos los vértices tienen exactamente 4 adyacentes, salvo los de los bordes, es decir los de la primera y última fila o columna.
Implementar una función que dado el grafo y m puntos iniciales distintos en la grilla (i1, j1), · · · ,(im, jm), determine si existen m
caminos disjuntos (de vértices) donde cada uno comience en un punto inicial, y termine en m puntos diferentes del borde. En los
ejemplos del dorso, el de la izquierda tiene solución (la cuál se muestra) mientras que el de la derecha no tiene solución. Utilizar
redes de flujo para resolver este problema. Indicar y justificar la complejidad del algoritmo implementado.
"""
def CrearGrafo(bool):
    pass

def flujo(red, s, t):
    pass

def camino_grilla(grilla, iniciales):
    """
    Determina si existen m caminos disjuntos en vértices desde los m puntos
    iniciales hasta m vértices distintos del borde, usando redes de flujo.

    Idea: node splitting para disjunción de vértices.
    Cada vértice (i,j) se divide en (i,j,'in') → (i,j,'out') con capacidad 1,
    lo que garantiza que ningún vértice sea usado por más de un camino.

    Super fuente S conectada a cada punto inicial con capacidad 1.
    Super sumidero T conectado desde cada vértice del borde con capacidad 1.
    Si el flujo máximo == m, existen los m caminos disjuntos.

    Complejidad:
      - Nodos: O(n²) → 2n² + 2 tras el splitting
      - Aristas: O(n²) (grilla) + O(n²) (splits) + O(n) (bordes→T) + O(m) (S→iniciales)
      - Edmonds-Karp con BFS: O(V·E) por camino aumentante, y a lo sumo m caminos
        → O(m · n²) en total, con m ≤ n² → O(n⁴) en el peor caso
    """
    n = len(grilla)
    S = 's'
    T = 't'

    red = CrearGrafo(True)
    red.agregarvertice(S)
    red.agregarvertice(T)

    # Agregar todos los vértices divididos en _in y _out
    for i in range(n):
        for j in range(n):
            red.agregarvertice((i, j, 'in'))
            red.agregarvertice((i, j, 'out'))
            # Capacidad 1 en el split: garantiza disjunción de vértices
            red.agregararista((i, j, 'in'), (i, j, 'out'), 1)

    # Super fuente a cada punto inicial
    for (i, j) in iniciales:
        red.agregararista(S, (i, j, 'in'), 1)

    # Vértices del borde conectados al super sumidero
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                red.agregararista((i, j, 'out'), T, 1)

    # Aristas de la grilla: cada arista no dirigida se agrega en ambas direcciones
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(n):
            for di, dj in direcciones:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    red.agregararista((i, j, 'out'), (ni, nj, 'in'), 1)

    resultado = flujo(red, S, T)
    suma = sum(f for (_, v), f in resultado.items() if v == T)
    return suma == len(iniciales)

#La complejidad del algoritmo es O(n^2)

"""3. El problema de Camino Hamiltoniano con inicio y fin es el siguiente: Dado un grafo, un vértice de inicio y otro de fin, ¿existe un
camino Hamiltoniano dentro del grafo que empiece en el vértice de inicio y termine en el vértice de fin?
Demostrar que el problema de Camino Hamiltoniano con inicio y fin es un problema NP-Completo. Recomendamos recordar que el
problema de Camino Hamiltoniano es un problema NP-Completo."""

def verificador(grafo, camino, i , f , n ):
    return len(grafo)==len(camino) and camino[0]==i and camino[n]== f

"""Para poder demostrar que el problema de camino Hamiltoniano con inicio y fin es NP-completo, procedo a realizar una reducción desde el problema de camino Hamiltoniano, que ya se sabe que es NP-completo.
Para ello, dado un grafo G =(V, E) del problema del camino Hamiltoniano, construyo un nuevo grafo G' = (V', E') para el problema del camino Hamiltoniano con inicio y fin de la siguiente manera:
1. Selecciono un vértice arbitrario v0 en V.
2. Creo dos nuevos vértices s y t, que serán el inicio y fin del camino Hamiltoniano en G'.
3. Defino V' = V ∪ {s, t}.
4. Defino E' = E ∪ {(s, v0), (v0, t)}.
A continuación, demuestro que la reducción es correcta:
Para ello debo mostrar la implicancia en ambas direcciones, es decir, hay solución en G si y solo si hay solución en G' y viceversa.

-Implicancia 1:
Si existe un camino Hamiltoniano en G, entonces existe un camino Hamiltoniano con inicio y fin en G'.
Supongamos que existe un camino Hamiltoniano en G que visita todos los vértices en V exactamente una vez. Entonces, puedo construir un camino Hamiltoniano con inicio y fin en G' que comienza en s, sigue el camino Hamiltoniano en G desde v0 y termina en t. Este camino visita todos los vértices en V' exactamente una vez. Si no fuese de esta forma, entonces el camino en G no sería un camino Hamiltoniano y se contradice la suposición inicial.
-Implicancia 2:
Si existe un camino Hamiltoniano con inicio y fin en G', entonces existe un camino Hamiltoniano en G.
Supongamos que existe un camino Hamiltoniano con inicio y fin en G' que comienza en s y termina en t, visitando todos los vértices en V' exactamente una vez. Entonces, al eliminar los vértices s y t del camino, obtengo un camino que visita todos los vértices en V exactamente una vez, lo que constituye un camino Hamiltoniano en G. Si no fuese de esta forma, entonces el camino en G' no sería un camino Hamiltoniano con inicio y fin y se contradice la suposición inicial.

"""


"""4. Dado un grafo en forma de grilla como el dado a continuación (y también a los del ejercicio 2), donde cada vértice tiene un peso
w(v), se desea maximizar la sumatoria de los pesos de un Independent Set sobre dicho grafo.
a. Dar un algoritmo greedy que sirva de aproximación para la solución al problema.
b. Demostrar que cualquier vértice es parte de la solución aproximada, o bien tiene peso menor (o igual) a alguno de sus adyacentes,
que es en efecto parte de dicha solución.
c. Analizar qué tan buena es la aproximación obtenida."""

#Un algoritmo 