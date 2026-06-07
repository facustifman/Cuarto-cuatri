"""
Problema: m máquinas lentas (velocidad 1) + k máquinas rápidas (velocidad 2).
n trabajos con longitudes p[i]. Minimizar el makespan (tiempo en que termina la última máquina).

Algoritmo greedy: asignar cada trabajo a la máquina que termine antes.
  - Máquina lenta procesa trabajo p en tiempo p.
  - Máquina rápida procesa trabajo p en tiempo p/2.

Complejidad: O(n * (m+k))  [con heap: O(n log(m+k))]
"""

import heapq


def asignar_trabajos(m, k, trabajos):
    """
    m: cantidad de máquinas lentas (velocidad 1)
    k: cantidad de máquinas rápidas (velocidad 2)
    trabajos: lista de longitudes de los pedidos

    Retorna el makespan (tiempo que tarda la última máquina en terminar).
    """
    # heap de (tiempo_fin, id_máquina, velocidad)
    heap = []
    for i in range(m):
        heapq.heappush(heap, (0, i, 1))
    for i in range(k):
        heapq.heappush(heap, (0, m + i, 2))

    asignacion = {i: [] for i in range(m + k)}

    for trabajo in trabajos:
        tiempo_fin, maquina, velocidad = heapq.heappop(heap)
        tiempo_proceso = trabajo / velocidad
        nuevo_fin = tiempo_fin + tiempo_proceso
        asignacion[maquina].append(trabajo)
        heapq.heappush(heap, (nuevo_fin, maquina, velocidad))

    makespan = max(t for t, _, _ in heap)
    return makespan, asignacion


# ---------- demostración de la cota 3-aproximación ----------

if __name__ == "__main__":
    m, k = 2, 1
    trabajos = [10, 8, 7, 6, 5, 4]

    makespan, asignacion = asignar_trabajos(m, k, trabajos)
    print(f"Makespan obtenido: {makespan:.2f}")
    for maq, jobs in asignacion.items():
        tipo = "rápida" if maq >= m else "lenta "
        vel = 2 if maq >= m else 1
        carga = sum(j / vel for j in jobs)
        print(f"  Máquina {maq} ({tipo}): trabajos {jobs}, carga {carga:.2f}")
