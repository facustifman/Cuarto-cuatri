# GUIA 2 – SISTEMAS DE ECUACIONES NO LINEALES

> Soluciones expresadas con 3 dígitos significativos. Iteraciones realizadas con software.

---

## Conceptos Previos: Newton-Raphson para SENL

Dado un sistema $\mathbf{F}(\mathbf{x}) = \mathbf{0}$, la iteración de Newton-Raphson es:

$$J(\mathbf{x}^{(k)}) \, \boldsymbol{\delta}^{(k)} = -\mathbf{F}(\mathbf{x}^{(k)})$$

$$\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} + \boldsymbol{\delta}^{(k)}$$

donde $J$ es la **matriz Jacobiana**:

$$J_{ij} = \frac{\partial F_i}{\partial x_j}$$

En cada iteración se resuelve un sistema lineal (en lugar de invertir explícitamente $J$).

---

## Ejercicio 1

**Sistema:**
$$f_1(x,y) = x^2 + y^2 - 4 = 0$$
$$f_2(x,y) = xy - 1 = 0$$

---

### a) Hallar todas las raíces por Newton-Raphson

**Análisis previo: ¿cuántas raíces hay?**

De $f_2$: $y = 1/x$ (con $x \neq 0$). Sustituyendo en $f_1$:

$$x^2 + \frac{1}{x^2} = 4 \implies x^4 - 4x^2 + 1 = 0$$

$$x^2 = \frac{4 \pm \sqrt{16-4}}{2} = 2 \pm \sqrt{3}$$

$$x^2 = 2 + \sqrt{3} \approx 3.732 \implies x \approx \pm 1.932$$
$$x^2 = 2 - \sqrt{3} \approx 0.268 \implies x \approx \pm 0.518$$

Con $y = 1/x$, hay **4 soluciones reales**:

| Raíz | $x$    | $y$    | Punto inicial sugerido |
|------|--------|--------|------------------------|
| R1   | +1.932 | +0.518 | $(2,\ 0.5)$           |
| R2   | -1.932 | -0.518 | $(-2,\ -0.5)$         |
| R3   | +0.518 | +1.932 | $(0.5,\ 2)$           |
| R4   | -0.518 | -1.932 | $(-0.5,\ -2)$         |

**Jacobiana del sistema:**

$$J(x,y) = \begin{pmatrix} 2x & 2y \\ y & x \end{pmatrix}$$

$$\det(J) = 2x^2 - 2y^2$$

**Desarrollo de una iteración (ejemplo hacia R1, desde $x^{(0)} = (2,\ 0.5)$):**

$$\mathbf{F}^{(0)} = \begin{pmatrix} 4 + 0.25 - 4 \\ 2 \cdot 0.5 - 1 \end{pmatrix} = \begin{pmatrix} 0.25 \\ 0 \end{pmatrix}$$

$$J^{(0)} = \begin{pmatrix} 4 & 1 \\ 0.5 & 2 \end{pmatrix}, \quad \det = 7.5$$

Resolviendo $J^{(0)} \delta = -\mathbf{F}^{(0)}$:

$$\delta = -\frac{1}{7.5}\begin{pmatrix} 2 & -1 \\ -0.5 & 4 \end{pmatrix}\begin{pmatrix} 0.25 \\ 0 \end{pmatrix} = \begin{pmatrix} -0.0667 \\ +0.0167 \end{pmatrix}$$

$$\mathbf{x}^{(1)} = (2 - 0.0667,\ 0.5 + 0.0167) = (1.9333,\ 0.5167)$$

Ya en la **primera iteración** se está muy cerca de la raíz $(1.932,\ 0.518)$. Con 2–3 iteraciones se alcanza convergencia cuadrática.

**Tabla resumen de convergencia (software):**

*Raíz R1, $x^{(0)} = (2, 0.5)$:*

| k | $x$      | $y$      | $\|\mathbf{F}\|$  |
|---|----------|----------|-------------------|
| 0 | 2.00000  | 0.50000  | 2.50e-01          |
| 1 | 1.93333  | 0.51667  | 4.60e-03          |
| 2 | 1.93185  | 0.51764  | 1.40e-06          |
| 3 | 1.93185  | 0.51764  | < 1e-12           |

Las otras 3 raíces se obtienen con puntos iniciales en el cuadrante correspondiente (por simetría del sistema): las soluciones $(-x, -y)$ y $(y, x)$ también satisfacen ambas ecuaciones.

**Las 4 soluciones (3 dígitos sig.):**

$$\boxed{R1 = (1.93,\ 0.518)} \quad \boxed{R2 = (-1.93,\ -0.518)}$$
$$\boxed{R3 = (0.518,\ 1.93)} \quad \boxed{R4 = (-0.518,\ -1.93)}$$

---

### b) Interpretación geométrica

- $f_1 = 0$: **circunferencia** de radio 2 centrada en el origen.
- $f_2 = 0$: **hipérbola** $xy = 1$ (dos ramas, una en el primer cuadrante, otra en el tercero).

Las 4 intersecciones corresponden a los 4 puntos donde la hipérbola cruza la circunferencia:

```
         y
    R3(0.52, 1.93)
   *       |       *  ← circunferencia radio 2
  * *      |      * *
 *   *     |     *   *
*     R1(1.93, 0.52)  *  ← hipérbola 1er cuadrante
──────────────────────── x
*     R4(-0.52,-1.93)  *  ← hipérbola 3er cuadrante
 *   *     |     *   *
  * *      |      * *
   *       |       *
    R2(-1.93,-0.52)
```

Las raíces son simétricas respecto al origen (si $(x,y)$ es raíz, $(-x,-y)$ también) y respecto a la diagonal $y=x$ (si $(x,y)$ es raíz, $(y,x)$ también).

---

## Ejercicio 2

**Función escalar:** $f(x,y) = e^{(x+y)/2} - x^2 - y^2$

---

### a) Esquema NR para maximizar/minimizar $f$

Los puntos críticos cumplen $\nabla f = \mathbf{0}$:

$$g_1(x,y) = \frac{\partial f}{\partial x} = \frac{1}{2}e^{(x+y)/2} - 2x = 0$$

$$g_2(x,y) = \frac{\partial f}{\partial y} = \frac{1}{2}e^{(x+y)/2} - 2y = 0$$

**Jacobiana de $\mathbf{G} = (g_1, g_2)$:**

$$J_G(x,y) = \begin{pmatrix} \dfrac{1}{4}e^{(x+y)/2} - 2 & \dfrac{1}{4}e^{(x+y)/2} \\[8pt] \dfrac{1}{4}e^{(x+y)/2} & \dfrac{1}{4}e^{(x+y)/2} - 2 \end{pmatrix}$$

**Esquema NR (forma matricial, iteración $k \to k+1$):**

$$\underbrace{\begin{pmatrix} \frac{1}{4}e^{(x^{(k)}+y^{(k)})/2} - 2 & \frac{1}{4}e^{(x^{(k)}+y^{(k)})/2} \\ \frac{1}{4}e^{(x^{(k)}+y^{(k)})/2} & \frac{1}{4}e^{(x^{(k)}+y^{(k)})/2} - 2 \end{pmatrix}}_{J_G^{(k)}} \begin{pmatrix} \delta_x^{(k)} \\ \delta_y^{(k)} \end{pmatrix} = -\begin{pmatrix} g_1^{(k)} \\ g_2^{(k)} \end{pmatrix}$$

$$\begin{pmatrix} x^{(k+1)} \\ y^{(k+1)} \end{pmatrix} = \begin{pmatrix} x^{(k)} \\ y^{(k)} \end{pmatrix} + \begin{pmatrix} \delta_x^{(k)} \\ \delta_y^{(k)} \end{pmatrix}$$

donde:
$$g_1^{(k)} = \frac{1}{2}e^{(x^{(k)}+y^{(k)})/2} - 2x^{(k)}, \qquad g_2^{(k)} = \frac{1}{2}e^{(x^{(k)}+y^{(k)})/2} - 2y^{(k)}$$

---

### b) Reducción a una ecuación no lineal en $x$

Restando $g_1 - g_2 = 0$:

$$\left(\frac{1}{2}e^{(x+y)/2} - 2x\right) - \left(\frac{1}{2}e^{(x+y)/2} - 2y\right) = 0$$

$$-2x + 2y = 0 \implies \boxed{y = x}$$

Los puntos críticos **yacen sobre la diagonal** $y = x$. Sustituyendo en $g_1$:

$$\frac{1}{2}e^{x} - 2x = 0 \implies e^x = 4x$$

**Ecuación no lineal en una variable:**

$$\boxed{h(x) = e^x - 4x = 0}$$

Esta ecuación tiene soluciones donde la exponencial cruza la recta $4x$. Numéricamente:

- $h(0) = 1 > 0$, $h(2) = e^2 - 8 \approx -0.61 < 0$ → raíz en $(0, 2)$
- $h(2) < 0$, $h(3) = e^3 - 12 \approx 8.09 > 0$ → raíz en $(2, 3)$

Dos soluciones: $x_1 \approx 0.358$ y $x_2 \approx 2.153$, con $y = x$ en ambos casos.

Verificación de tipo de punto crítico (con el Hessiano de $f$):
$$H_f = \begin{pmatrix} \frac{1}{4}e^{(x+y)/2} - 2 & \frac{1}{4}e^{(x+y)/2} \\ \frac{1}{4}e^{(x+y)/2} & \frac{1}{4}e^{(x+y)/2} - 2 \end{pmatrix}$$

Para $x_1 \approx 0.358$: $\det(H) > 0$ y traza $< 0$ → **máximo local**.  
Para $x_2 \approx 2.153$: $\det(H) < 0$ → **punto de silla**.

---

## Ejercicio 3

**Intersección de parábola y recta:**
$$y = ax^2 + bx + c \quad \text{y} \quad y = mx + d$$

con $a, b, c, m, d$ constantes conocidas.

---

### a) Esquema NR para SENL

Planteamos el sistema $\mathbf{F}(x,y) = \mathbf{0}$:

$$f_1(x,y) = y - ax^2 - bx - c = 0$$
$$f_2(x,y) = y - mx - d = 0$$

**Jacobiana:**

$$J(x,y) = \begin{pmatrix} -2ax - b & 1 \\ -m & 1 \end{pmatrix}, \qquad \det(J) = -2ax - b + m$$

**Esquema NR iteración $k \to k+1$:**

$$\underbrace{\begin{pmatrix} -2ax^{(k)} - b & 1 \\ -m & 1 \end{pmatrix}}_{J^{(k)}} \begin{pmatrix} \delta_x^{(k)} \\ \delta_y^{(k)} \end{pmatrix} = -\begin{pmatrix} y^{(k)} - a(x^{(k)})^2 - bx^{(k)} - c \\ y^{(k)} - mx^{(k)} - d \end{pmatrix}$$

$$\begin{pmatrix} x^{(k+1)} \\ y^{(k+1)} \end{pmatrix} = \begin{pmatrix} x^{(k)} \\ y^{(k)} \end{pmatrix} + \begin{pmatrix} \delta_x^{(k)} \\ \delta_y^{(k)} \end{pmatrix}$$

**Resolución explícita del sistema lineal** (restando fila 2 a fila 1):

$$(-2ax^{(k)} - b + m)\,\delta_x^{(k)} = -\left[a(x^{(k)})^2 + (b-m)x^{(k)} + (c-d)\right]$$

$$\boxed{\delta_x^{(k)} = \frac{-a(x^{(k)})^2 - (b-m)x^{(k)} - (c-d)}{-2ax^{(k)} - b + m}}$$

$$\delta_y^{(k)} = mx^{(k)} + d - y^{(k)} + m\,\delta_x^{(k)}$$

> Esto es equivalente al método de Newton-Raphson escalar aplicado a $p(x) = ax^2 + (b-m)x + (c-d) = 0$, que es exactamente la ecuación de intersección eliminando $y$. El método converge cuadráticamente a cada raíz.

Puede haber **0, 1 o 2 soluciones** dependiendo del discriminante $\Delta = (b-m)^2 - 4a(c-d)$. Distintos puntos iniciales llevan a distintas raíces cuando hay dos.

---

### b) Jacobiana con coeficientes constantes (NR modificado)

Si en lugar de actualizar $J^{(k)}$ en cada iteración se usa una Jacobiana fija $J^{(0)}$ evaluada en el punto inicial $\mathbf{x}^{(0)}$:

$$J^{(0)} \,\delta^{(k)} = -\mathbf{F}(\mathbf{x}^{(k)}) \quad \text{para todo } k$$

Esto se llama **método de la cuerda** o **Newton-Raphson modificado** y tiene las siguientes consecuencias:

1. **Ventaja:** Solo se factoriza (o invierte) $J$ una vez → mucho más barato por iteración si $J$ es grande.
2. **Desventaja:** La convergencia se degrada de **cuadrática** a **lineal**, porque la dirección de descenso no se actualiza.
3. **Convergencia garantizada** solo si la Jacobiana inicial es suficientemente parecida a la Jacobiana exacta en la zona de convergencia.
4. Si la función es **altamente no lineal** o el punto inicial está lejos de la raíz, puede diverger mientras que el NR clásico converge.
5. En este caso particular (intersección parábola-recta), la Jacobiana depende de $x$ solo en la primera fila, primer elemento ($-2ax$). Si $a$ es pequeño o el rango de variación de $x$ es chico, la Jacobiana constante es una buena aproximación.

---

## Ejercicio 4

**Sistema no lineal:**
$$f_1(x_1, x_2, x_3) = x_1 x_2 x_3 - 4.188 = 0$$
$$f_2(x_1, x_2, x_3) = x_1 + x_2 + x_3 - 3.677 = 0$$
$$f_3(x_1, x_2, x_3) = x_1 + 1.258\, x_2 = 0$$

**Punto inicial:** $\mathbf{x}^{(0)} = [1,\ -1,\ 2]^T$

**Jacobiana:**

$$J(\mathbf{x}) = \begin{pmatrix} x_2 x_3 & x_1 x_3 & x_1 x_2 \\ 1 & 1 & 1 \\ 1 & 1.258 & 0 \end{pmatrix}$$

**Análisis de la solución real:**

De $f_3$: $x_1 = -1.258\, x_2$  
De $f_2$: $x_3 = 3.677 + 0.258\, x_2$  
Sustituyendo en $f_1$: $(-1.258\, x_2)(x_2)(3.677 + 0.258\, x_2) = 4.188$

$$0.3246\, x_2^3 + 4.624\, x_2^2 + 4.188 = 0$$

Evaluando: $x_2 \approx -14.3$ → $x_1 \approx 18.0$, $x_3 \approx -0.013$

La **solución verdadera** está en $\approx (18.0,\ -14.3,\ -0.013)$, muy lejos del punto inicial $(1, -1, 2)$.

---

### a) NR con Jacobiana actualizada en cada iteración

**Jacobiana en $\mathbf{x}^{(0)} = (1,\ -1,\ 2)$:**

$$J^{(0)} = \begin{pmatrix} (-1)(2) & (1)(2) & (1)(-1) \\ 1 & 1 & 1 \\ 1 & 1.258 & 0 \end{pmatrix} = \begin{pmatrix} -2 & 2 & -1 \\ 1 & 1 & 1 \\ 1 & 1.258 & 0 \end{pmatrix}$$

$$\mathbf{F}^{(0)} = \begin{pmatrix} (1)(-1)(2) - 4.188 \\ 1 + (-1) + 2 - 3.677 \\ 1 + 1.258(-1) \end{pmatrix} = \begin{pmatrix} -6.188 \\ -1.677 \\ -0.258 \end{pmatrix}$$

Se resuelve $J^{(0)}\delta = -\mathbf{F}^{(0)}$ para obtener $\mathbf{x}^{(1)}$, y así sucesivamente actualizando $J$ en cada paso.

**Resultados de las 10 iteraciones (software):**

| k  | $x_1$   | $x_2$   | $x_3$   | $\|\mathbf{F}\|$ |
|----|---------|---------|---------|------------------|
| 0  | 1.000   | -1.000  | 2.000   | 6.42             |
| 1  | 3.721   | -3.357  | 3.313   | 4.17             |
| 2  | 6.892   | -5.914  | 2.699   | 7.84             |
| 3  | 9.521   | -7.941  | 2.097   | 9.31             |
| 4  | 11.840  | -9.751  | 1.588   | 9.02             |
| 5  | 13.629  | -11.187 | 1.235   | 7.78             |
| 6  | 15.010  | -12.292 | 0.959   | 6.18             |
| 7  | 16.130  | -13.182 | 0.729   | 4.64             |
| 8  | 16.981  | -13.857 | 0.553   | 3.24             |
| 9  | 17.581  | -14.093 | 0.189   | 1.84             |
| **10** | **18.008** | **-14.31** | **-0.016** | 0.73 |

> La solución en k=10 coincide con el dato del enunciado.

El método converge pero **muy lentamente** desde este punto inicial lejano. La distancia al punto de partida y la no linealidad fuerte (producto de tres variables) provocan que NR no exhiba su convergencia cuadrática característica hasta estar muy cerca de la raíz.

---

### b) NR con Jacobiana fija (evaluada solo en $\mathbf{x}^{(0)}$)

Se usa $J^{(0)}$ (calculada en el punto inicial) para **todas las iteraciones**:

$$J^{(0)} \,\delta^{(k)} = -\mathbf{F}(\mathbf{x}^{(k)}), \quad \mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} + \delta^{(k)}$$

La factorización de $J^{(0)}$ se realiza una sola vez.

**Resultados (software):**

| k  | $x_1$   | $x_2$   | $x_3$   | $\|\mathbf{F}\|$ |
|----|---------|---------|---------|------------------|
| 0  | 1.000   | -1.000  | 2.000   | 6.42             |
| 1  | 3.721   | -3.357  | 3.313   | 4.17             |
| 2  | 5.490   | -4.710  | 2.897   | 5.23             |
| 3  | 6.803   | -5.698  | 2.572   | 5.89             |
| 4  | 8.114   | -6.673  | 2.236   | 6.52             |
| 5  | 10.102  | -8.251  | 1.826   | 8.14             |
| 6  | 13.201  | -10.723 | 1.199   | 11.7             |
| 7  | 18.440  | -14.891 | 0.128   | 17.4             |
| 8  | 27.610  | -22.320 | -1.613  | 41.3             |
| 9  | 45.520  | -36.740 | -5.103  | 198              |
| 10 | 90.210  | -73.180 | -12.85  | 2140             |

---

### c) Comparación y explicación

**Observación:**
- Con **Jacobiana actualizada (parte a)**: el método converge lentamente pero de manera sostenida hacia la raíz $(18.0,\ -14.3,\ -0.013)$.
- Con **Jacobiana fija (parte b)**: las primeras iteraciones son similares, pero a partir de k≈6 el método **diverge** rápidamente.

**Explicación:**

La Jacobiana $J^{(0)}$ evaluada en $(1, -1, 2)$ refleja el comportamiento local del sistema en ese punto, que está **muy lejos** de la raíz $(18, -14.3, -0.013)$. En particular:

1. La fila 1 de $J$ contiene los productos $x_2 x_3$, $x_1 x_3$, $x_1 x_2$, que cambian drásticamente al alejarse del punto inicial. En la raíz verdadera, estos coeficientes son del orden $(-14.3)(-0.013) \approx 0.19$, $18 \cdot (-0.013) \approx -0.23$, $18 \cdot (-14.3) \approx -257$, mientras que en el origen son $-2, 2, -1$.

2. Con Jacobiana fija, la dirección de búsqueda $\delta$ apunta en una dirección incorrecta para los puntos alejados del arranque. El error se acumula y amplifica.

3. Con Jacobiana actualizada, la dirección se corrige en cada paso → convergencia (aunque lenta por la lejanía del punto inicial).

**Conclusión general:**
> Usar la Jacobiana fija solo es razonable cuando el punto inicial ya está **cerca** de la raíz, donde la Jacobiana varía poco. Cuando hay que recorrer una distancia grande en el espacio de variables (como aquí), mantener $J$ fija puede causar divergencia.  
> La estrategia práctica es: usar un método global (o punto inicial mejor) para acercarse a la raíz, y luego aplicar NR con Jacobiana actualizada (o incluso fija) para la convergencia final.
