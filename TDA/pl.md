# Apunte Segunda Clase: Programación Lineal

## Independent Set por Programación Lineal

### Definición de variables

Para todo vértice $v$:

- $x_v = 1$ si $v$ pertenece al conjunto independiente
- $x_v = 0$ en caso contrario

### Formulación del problema

$$\max \sum_v x_v$$

$$\text{s.a.} \quad x_u + x_v \leq 1 \quad \forall (u,v) \in E$$

### Truco de la Big M

**Objetivo:** Relajar restricciones complicadas utilizando una constante $M$ suficientemente grande.

**Idea:** Si $Y_i = 0$, la restricción se activa. Si $Y_i = 1$, la restricción se relaja (se vuelve inactiva).

#### Inecuación con Big M

$$Y_i + \sum_k Y_k \leq 1 + M(1 - Y_i)$$

**Interpretación:**

- Cuando $Y_i = 1$: $1 + \sum_k Y_k \leq 1 + M \cdot 0 = 1$ (restricción activa)
- Cuando $Y_i = 0$: $\sum_k Y_k \leq 1 + M$ (restricción relajada, prácticamente inactiva si $M$ es grande)

#### Problema del cambio

**Variables:**

- $x_i$: cantidad de cada tipo de moneda a usar
- $y_i$: variable binaria que indica si se usa o no la moneda $i
- $M$: constante grande
- $C$: cantidad total a alcanzar
- $v_i$: valor de cada tipo de moneda
- $N$: número de tipos de monedas

**Formulación:**
$$\min \sum_i x_i$$
$$\text{s.a.} \quad \sum_i v_i x_i = C$$
$$x_i \leq M y_i \quad \forall i$$
$$y_i \in \{0,1\} \quad \forall i$$

#### Problema del coloreo

**Variables:**

- $x_{v,c} = 1$ si el vértice $v$ es coloreado con el color $c$, 0 en caso contrario
- $y_c = 1$ si el color $c$ es utilizado, 0 en caso contrario
- $M$: constante grande
- $V$: conjunto de vértices
- $C$: conjunto de colores

**Formulación:**
$$\min \sum_{c \in C} y_c$$
$$\text{s.a.} \quad \sum_{c \in C} x_{v,c} = 1 \quad \forall v \in V$$
$$x_{u,c} + x_{v,c} \leq y_c \quad \forall (u,v) \in E, \forall c \in C$$
$$y_c \in \{0,1\} \quad \forall c \in C$$
$$x_{v,c} \in \{0,1\} \quad \forall v \in V, \forall c \in C$$

#### Problema del Viajante

**Variables:**
- $x_{i,j} = 1$ si el viajante va de la ciudad $i$ a la ciudad $j$, 0 en caso contrario
- $M$: constante grande
- $N$: número de ciudades
- $d_{i,j}$: distancia entre las ciudades $i$ y $j$
- $C$: conjunto de ciudades
- $u_i$: variable auxiliar para evitar subciclos
- $y_i$: variable binaria que indica si la ciudad $i$ es visitada, 0 en caso contrario

**Formulación:**
$$\min \sum_{i,j} d_{i,j} x_{i,j}$$
$$\text{s.a.} \quad \sum_{j} x_{i,j} = 1 \quad \forall i \in C$$
$$\sum_{i} x_{i,j} = 1 \quad \forall j \in C$$
$$u_i - u_j + N x_{i,j} \leq N - 1 \quad \forall i \neq j, i,j \in C$$
$$x_{i,j} \in \{0,1\} \quad \forall i,j \in C$$
$$u_i \geq 0 \quad \forall i \in C$$
$$y_i \in \{0,1\} \quad \forall i \in C$$
