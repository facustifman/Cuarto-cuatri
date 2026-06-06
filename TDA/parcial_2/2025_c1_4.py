"""1. Manejamos un negocio que atiende clientes en Atenas y en Roma. Nos interesa cada mes decidir si operar en una u otra ciudad.
Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: A y R, con valores para todos los meses hasta n.
Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo C por la mudanza. Dados los
arreglos de costos de operación en Atenas (A) y Roma (R), implementar un modelo de programación lineal que determine qué
meses se operará desde Atenas, y en cuáles desde Roma, de forma de minimizar el costo total. Indicar la cantidad de inecuaciones.

Variables:
  Xi ∈ {0,1} para cada mes i=1..n: Xi=1 significa operar en Atenas, Xi=0 en Roma.
  Yi ∈ {0,1} para cada i=1..n-1: Yi=1 significa que hubo mudanza entre el mes i e i+1.

Obj: min  Σ(A[i]*Xi + R[i]*(1-Xi)) + C*Σ(Yi)

Restricciones de mudanza (capturan si Xi ≠ Xi+1):
  Yi >= Xi - Xi+1    para i=1..n-1   (mudanza de Atenas a Roma)
  Yi >= Xi+1 - Xi    para i=1..n-1   (mudanza de Roma a Atenas)
  (como minimizamos y Yi tiene coeficiente positivo C, el modelo lo fuerza a 0 cuando no hay cambio)

Dominio:
  0 <= Xi <= 1   para i=1..n
  0 <= Yi <= 1   para i=1..n-1

Cantidad de inecuaciones:
  2*(n-1) restricciones de mudanza + 2n + 2*(n-1) de dominio = O(n)
  Las principales son las 2*(n-1) restricciones de mudanza.
"""


"""2. Para poder cortar con el juego del rival, Scaloni cuenta con información precisa minuto a minuto. En un momento dado, tiene la
información perfecta de qué jugador puede darle un pase a cuál otro (independientemente de quién tenga la pelota) o marcar un gol.
Scaloni quiere saber a qué jugador, o jugadores, es indispensable marcar para evitar que nos marquen un gol. Suponiendo que una
jugada arranca en el arquero contrario, y que se tiene la información de qué jugador de ese equipo puede pasarle la pelota a cuál/es
otro/s (incluyendo al arquero), considerando que esto no es necesariamente recíproco (no todos los jugadores pueden hacer los mismos
pases o goles, ¿o vos podés dar los mismos pases que Messi?), y cuáles jugadores podrían marcar un gol en ese momento, indicar
cuáles son los mínimos jugadores contrarios a marcar de tal forma que no sea posible que nos marquen un gol (no podemos marcar
al arquero). Resolver este problema utilizando redes de flujo. Pueden suponer que la función flujo(red, s, t) les devuelve
tanto la asignación de flujo a cada arista, como también la Red Residual resultante de aplicar el algoritmo de Ford-Fulkerson. Indicar
y justificar la complejidad del algoritmo planteado. Para todo el problema, considerar que, si bien hay un único arquero, podrían
haber n jugadores de campo (simplemente para no quedarse con que son 10 nada más).

""" 
def flujo(red,s,t):
    pass
def CrearGrafo():
    pass

def marcas(jugadores, arquero, goleadores):
    """
    Devuelve el mínimo conjunto de jugadores a marcar para evitar un gol.

    Reducción a mínimo corte de vértices:
      - Node splitting: cada jugador v → (v_in, v_out) con capacidad 1.
        El arquero tiene capacidad ∞ en su split (no se puede marcar).
      - Aristas de pase: v_out → w_in con capacidad ∞ (cortamos vértices, no aristas).
      - Super fuente S → arquero_in con ∞.
      - Cada goleador: goleador_out → T con ∞.
      - Max-flow = min vertex cut = mínimo de jugadores a marcar.

    Para extraer el corte del residual:
      - BFS desde S en el residual.
      - Un jugador v debe marcarse si v_in es alcanzable pero v_out no lo es.

    Complejidad:
      - V = O(n), E = O(n²) → red con O(n) nodos y O(n²) aristas.
      - Flujo máximo ≤ n (a lo sumo n jugadores de campo).
      - Edmonds-Karp: O(flujo * E) = O(n * n²) = O(n³).
    """
    INF = float("inf")
    S = "S"
    T = "T"

    red = CrearGrafo()
    red.AgregarVertice(S)
    red.AgregarVertice(T)

    # Node splitting para todos los jugadores
    for v in jugadores.vertices():
        red.AgregarVertice(v + "_in")
        red.AgregarVertice(v + "_out")
        # El arquero no se puede marcar → capacidad infinita en su split
        capacidad = INF if v == arquero else 1
        red.AgregarArista(v + "_in", v + "_out", capacidad)

    # Super fuente conectada al arquero
    red.AgregarArista(S, arquero + "_in", INF)

    # Aristas de pase: v_out → w_in con capacidad ∞ (no cortamos aristas)
    for v in jugadores.vertices():
        for w in jugadores.adyacentes(v):
            red.AgregarArista(v + "_out", w + "_in", INF)

    # Goleadores conectados al super sumidero
    for g in goleadores:
        red.AgregarArista(g + "_out", T, INF)

    _, residual = flujo(red, S, T)

    # Extraer el corte mínimo: jugadores donde v_in es alcanzable pero v_out no
    alcanzables = set()
    queue = [S]
    while queue:
        u = queue.pop(0)
        alcanzables.add(u)
        for v in residual.adyacentes(u):
            if v not in alcanzables and residual.capacidad(u, v) > 0:
                queue.append(v)
    jugadores_a_marcar = []
    for v in jugadores.vertices():
        if v + "_in" in alcanzables and v + "_out" not in alcanzables:
            jugadores_a_marcar.append(v)
    return jugadores_a_marcar


"""3. El problema conocido como Feedback Edge Set (FES) indica: Dado un grafo dirigido y un número entero k, ¿existe un subset de
aristas del grafo, de tamaño a lo sumo k, tal que si eliminamos dichas aristas del grafo, este queda acíclico?
Demostrar que FES es un problema NP-Completo. Recomendamos utilizar Vertex-Cover, partiendo desde un grafo no dirigido.
También recomendamos pensar un poco en cómo demostramos en clase que Camino Hamiltoniano era NP-Completo a partir de
Ciclo Hamiltoniano (o también similar a algo que seguramente debas pensar para el ejercicio 2).
"""
"""4. Dado un grafo bipartito (no dirigido) donde cada vértice v tiene un valor positivo w(v) asociado, queremos obtener un Vertex Cover
de suma mínima. Este problema es NP-Difícil, por lo que aplicaremos el siguiente algoritmo de aproximación:
    1. Inicializaremos resultado = ∅ como un conjunto vacío.
    2. Vemos todas las aristas del grafo (sin ningún orden particular). Si la arista está cubierta, es decir, algún vértice de sus extremos
    está en el conjunto resultado, la ignoramos. Sino, agregamos a resultado al vértice del extremo de la arista cuyo valor sea menor
    (si son iguales, cualquiera de los dos).
    3. Devolvemos resultado.
    ¿Podemos considerarla una buena aproximación? Calcular la cota de aproximación para justificar tu respuesta."""