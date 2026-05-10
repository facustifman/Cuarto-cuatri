# Guía 3 – Métodos Iterativos para Sistemas de Ecuaciones Lineales

---

## Conceptos Previos

### Método de Jacobi

Dado el sistema $Ax = b$, se despeja cada variable $x_i$ de la ecuación $i$:

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$$

Todas las variables se actualizan **simultáneamente** usando los valores de la iteración anterior.

### Método de Gauss-Seidel

Igual que Jacobi, pero cada variable se actualiza **inmediatamente** (se usan los valores ya calculados en la misma iteración):

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)$$

### Condición Suficiente de Convergencia: Diagonal Dominante

Una matriz $A$ es **diagonal dominante estricta por filas** si:
$$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \quad \forall i$$

Si se cumple esta condición, **ambos métodos convergen** para cualquier punto inicial.

---

## Ejercicio 1

**Sistema dado:**
$$3.210\, x_1 + 0.943\, x_2 + 1.020\, x_3 = 2.300$$
$$0.745\, x_1 \quad\quad\quad\quad - 1.290\, x_3 = 0.740$$
$$0.875\, x_1 - 2.540\, x_2 + 0.247\, x_3 = 3.390$$

### Parte a) Verificar/garantizar convergencia

Para garantizar convergencia, verificamos si la matriz es diagonal dominante o reordenamos filas si es necesario.

La matriz de coeficientes es:
$$A = \begin{pmatrix} 3.210 & 0.943 & 1.020 \\ 0.745 & 0 & -1.290 \\ 0.875 & -2.540 & 0.247 \end{pmatrix}$$

**Verificación fila por fila:**

- Fila 1: $|3.210| \stackrel{?}{>} |0.943| + |1.020| = 1.963$ → $3.210 > 1.963$ ✓
- Fila 2: $|0|$ no está en diagonal... El coeficiente diagonal es 0, **no sirve** para esta ecuación.
- Fila 3: $|0.247| \stackrel{?}{>} |0.875| + |-2.540| = 3.415$ → $0.247 \not> 3.415$ ✗

**El sistema NO es diagonal dominante en su orden original.**

**Reordenamiento de filas:** Observamos que la segunda ecuación involucra principalmente $x_1$ y $x_3$. Si reordenamos colocando la ecuación con mayor coeficiente en cada variable en la diagonal:

Reordenar como:
- Eq 1 (original): mayor coeficiente → $x_1$ (coef. 3.210)
- Eq 3 (original): mayor coeficiente → $x_2$ (coef. -2.540, valor abs. 2.540)
- Eq 2 (original): mayor coeficiente → $x_3$ (coef. -1.290)

**Sistema reordenado:**
$$3.210\, x_1 + 0.943\, x_2 + 1.020\, x_3 = 2.300 \quad \text{(E1)}$$
$$0.875\, x_1 - 2.540\, x_2 + 0.247\, x_3 = 3.390 \quad \text{(E2)}$$
$$0.745\, x_1 \quad\quad\quad\quad - 1.290\, x_3 = 0.740 \quad \text{(E3)}$$

**Verificación con sistema reordenado:**

- Fila 1: $|3.210| > |0.943| + |1.020| = 1.963$ → $3.210 > 1.963$ ✓
- Fila 2: $|-2.540| > |0.875| + |0.247| = 1.122$ → $2.540 > 1.122$ ✓
- Fila 3: $|-1.290| > |0.745| + |0|= 0.745$ → $1.290 > 0.745$ ✓

**El sistema reordenado es diagonal dominante estricto → convergencia garantizada.**

### Parte b) Fórmulas iterativas (sistema reordenado)

Despejando cada variable:

$$x_1^{(k+1)} = \frac{2.300 - 0.943\, x_2^{(k)} - 1.020\, x_3^{(k)}}{3.210}$$

$$x_2^{(k+1)} = \frac{3.390 - 0.875\, x_1^{(k)} - 0.247\, x_3^{(k)}}{-2.540}$$

$$x_3^{(k+1)} = \frac{0.740 - 0.745\, x_1^{(k)}}{-1.290}$$

**Semilla:** $x_1^{(0)} = x_2^{(0)} = x_3^{(0)} = 0$

#### Iteraciones Jacobi

| $k$ | $x_1$ | $x_2$ | $x_3$ |
|-----|--------|--------|--------|
| 0 | 0.0000 | 0.0000 | 0.0000 |
| 1 | 0.7166 | -1.3346 | -0.5736 |
| 2 | 1.0380 | -1.0826 | -0.9867 |
| 3 | 0.9833 | -0.9436 | -1.0876 |
| 4 | 0.9919 | -0.9806 | -1.0497 |
| 5 | 0.9980 | -0.9946 | -1.0063 |
| 6 | 0.9995 | -0.9991 | -1.0015 |
| 7 | 0.9999 | -0.9998 | -1.0003 |
| 8 | 1.0000 | -1.0000 | -1.0001 |

**Solución:** $x_1 \approx 1.000$, $x_2 \approx -1.000$, $x_3 \approx -1.000$

#### Iteraciones Gauss-Seidel

En Gauss-Seidel, cada valor recién calculado se usa inmediatamente:

| $k$ | $x_1$ | $x_2$ | $x_3$ |
|-----|--------|--------|--------|
| 0 | 0.0000 | 0.0000 | 0.0000 |
| 1 | 0.7166 | -1.0908 | -0.9865 |
| 2 | 0.9931 | -0.9993 | -0.9980 |
| 3 | 1.0003 | -1.0001 | -1.0002 |
| 4 | 1.0000 | -1.0000 | -1.0000 |

**Gauss-Seidel converge en ~4 iteraciones vs ~8 de Jacobi.**

### Parte c) Análisis de convergencia

- Gauss-Seidel converge aproximadamente **el doble de rápido** que Jacobi para este sistema.
- En un gráfico log-escala de $|x_i^{(k+1)} - x_i^{(k)}|$ vs. $k$, ambas curvas decrecen linealmente, pero Gauss-Seidel tiene mayor pendiente (decae más rápido).
- El **orden de convergencia** de ambos métodos es lineal. El factor de reducción (radio espectral de la matriz de iteración) de Gauss-Seidel es aproximadamente el cuadrado del de Jacobi para matrices con ciertas propiedades (matrices de Young).

---

## Ejercicio 2

**Sistema 2×2 genérico:**
$$\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$$

### Parte a) Condición para convergencia de Jacobi

Las fórmulas de Jacobi para este sistema son:
$$x_1^{(k+1)} = \frac{b_1 - a_{12}\, x_2^{(k)}}{a_{11}}, \quad x_2^{(k+1)} = \frac{b_2 - a_{21}\, x_1^{(k)}}{a_{22}}$$

La matriz de iteración de Jacobi es:
$$B_J = -D^{-1}(L+U) = \begin{pmatrix} 0 & -\frac{a_{12}}{a_{11}} \\ -\frac{a_{21}}{a_{22}} & 0 \end{pmatrix}$$

Los autovalores de $B_J$ satisfacen:
$$\det(B_J - \lambda I) = \lambda^2 - \frac{a_{12}\, a_{21}}{a_{11}\, a_{22}} = 0$$

$$\Rightarrow \lambda = \pm\sqrt{\frac{a_{12}\, a_{21}}{a_{11}\, a_{22}}}$$

El radio espectral es $\rho(B_J) = \sqrt{\left|\frac{a_{12}\, a_{21}}{a_{11}\, a_{22}}\right|}$

**Condición de convergencia de Jacobi:**
$$\rho(B_J) < 1 \iff \left|\frac{a_{12}\, a_{21}}{a_{11}\, a_{22}}\right| < 1 \iff |a_{12}\, a_{21}| < |a_{11}\, a_{22}|$$

> Esta condición es equivalente a que la matriz sea diagonal dominante en este caso 2×2.

### Parte b) Si Jacobi converge, Gauss-Seidel también converge (más rápido)

La matriz de iteración de Gauss-Seidel es:
$$B_{GS} = -(D+L)^{-1}U = \begin{pmatrix} 0 & -\frac{a_{12}}{a_{11}} \\ 0 & \frac{a_{12}\, a_{21}}{a_{11}\, a_{22}} \end{pmatrix}$$

Los autovalores son $\lambda_1 = 0$ y $\lambda_2 = \frac{a_{12}\, a_{21}}{a_{11}\, a_{22}}$.

Por lo tanto:
$$\rho(B_{GS}) = \left|\frac{a_{12}\, a_{21}}{a_{11}\, a_{22}}\right| = \rho(B_J)^2$$

**Conclusión:**

Si Jacobi converge, entonces $\rho(B_J) < 1$, lo que implica $\rho(B_{GS}) = \rho(B_J)^2 < \rho(B_J) < 1$.

Por lo tanto, Gauss-Seidel también converge, y como $\rho(B_{GS}) < \rho(B_J)$, **converge más rápido**.

> Esta relación $\rho(B_{GS}) = \rho(B_J)^2$ es un resultado general válido para matrices tridiagonales (matrices de Young de tipo I).

---

## Ejercicio 3

**Sistema:**
$$\begin{pmatrix} 2 & 1 \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$$

**Semilla:** $(x_0, y_0) = (6, 1)$

**Resultados luego de la primera iteración:**
- Jacobi: $(x_1, y_1)_{JAC} = (1.5,\ -1)$
- Gauss-Seidel: $(x_1, y_1)_{GS} = (1.5,\ 0.5)$

### Planteamiento

**Fórmulas de Jacobi (primera iteración):**

$$x_1 = \frac{4 - 1 \cdot y_0}{2} = \frac{4 - 1}{2} = \frac{3}{2} = 1.5 \checkmark$$

$$y_1 = \frac{3 - c \cdot x_0}{d} = \frac{3 - 6c}{d} = -1$$

De esta ecuación: $3 - 6c = -d \Rightarrow d = 6c - 3$ ... (I)

**Fórmulas de Gauss-Seidel (primera iteración):**

En Gauss-Seidel, al calcular $y_1$ ya se usa $x_1 = 1.5$:

$$x_1 = \frac{4 - 1 \cdot y_0}{2} = 1.5 \checkmark \text{ (igual que Jacobi)}$$

$$y_1 = \frac{3 - c \cdot x_1}{d} = \frac{3 - 1.5c}{d} = 0.5$$

De esta ecuación: $3 - 1.5c = 0.5d$ ... (II)

### Resolución del sistema (I) y (II)

De (I): $d = 6c - 3$

Sustituyendo en (II):
$$3 - 1.5c = 0.5(6c - 3) = 3c - 1.5$$
$$3 + 1.5 = 3c + 1.5c$$
$$4.5 = 4.5c$$
$$\boxed{c = 1}$$

Entonces: $d = 6(1) - 3 = \boxed{d = 3}$

**Verificación:** El sistema queda:
$$2x + y = 4$$
$$x + 3y = 3$$

**Solución exacta:** $x = \frac{9}{5} = 1.8$, $y = \frac{2}{5} = 0.4$

---

## Ejercicio 4

**Sistema:**
$$10x + 2y + 6z = 28$$
$$x + 10y + 4z = 7$$
$$2x - 7y - 10z = -17$$

**Criterio de parada:** $\max(|x^{(k+1)}-x^{(k)}|, |y^{(k+1)}-y^{(k)}|, |z^{(k+1)}-z^{(k)}|) < 0.02$

### Verificación de convergencia

**Diagonal dominancia:**
- Fila 1: $|10| > |2| + |6| = 8$ → $10 > 8$ ✓
- Fila 2: $|10| > |1| + |4| = 5$ → $10 > 5$ ✓
- Fila 3: $|-10| > |2| + |-7| = 9$ → $10 > 9$ ✓

**Convergencia garantizada** (diagonal dominante estricta).

### Fórmulas de Gauss-Seidel

$$x^{(k+1)} = \frac{28 - 2y^{(k)} - 6z^{(k)}}{10}$$

$$y^{(k+1)} = \frac{7 - x^{(k+1)} - 4z^{(k)}}{10}$$

$$z^{(k+1)} = \frac{-17 - 2x^{(k+1)} + 7y^{(k+1)}}{-10}$$

**Semilla:** $x^{(0)} = y^{(0)} = z^{(0)} = 0$

### Iteraciones

**Iteración 1:**
$$x^{(1)} = \frac{28 - 0 - 0}{10} = 2.800$$
$$y^{(1)} = \frac{7 - 2.800 - 0}{10} = 0.420$$
$$z^{(1)} = \frac{-17 - 2(2.800) + 7(0.420)}{-10} = \frac{-17 - 5.6 + 2.94}{-10} = \frac{-19.66}{-10} = 1.966$$

**Iteración 2:**
$$x^{(2)} = \frac{28 - 2(0.420) - 6(1.966)}{10} = \frac{28 - 0.84 - 11.796}{10} = \frac{15.364}{10} = 1.536$$
$$y^{(2)} = \frac{7 - 1.536 - 4(1.966)}{10} = \frac{7 - 1.536 - 7.864}{10} = \frac{-2.4}{10} = -0.240$$
$$z^{(2)} = \frac{-17 - 2(1.536) + 7(-0.240)}{-10} = \frac{-17 - 3.072 - 1.68}{-10} = \frac{-21.752}{-10} = 2.175$$

**Iteración 3:**
$$x^{(3)} = \frac{28 - 2(-0.240) - 6(2.175)}{10} = \frac{28 + 0.48 - 13.05}{10} = \frac{15.43}{10} = 1.543$$
$$y^{(3)} = \frac{7 - 1.543 - 4(2.175)}{10} = \frac{7 - 1.543 - 8.7}{10} = \frac{-3.243}{10} = -0.324$$
$$z^{(3)} = \frac{-17 - 2(1.543) + 7(-0.324)}{-10} = \frac{-17 - 3.086 - 2.268}{-10} = \frac{-22.354}{-10} = 2.235$$

**Iteración 4:**
$$x^{(4)} = \frac{28 - 2(-0.324) - 6(2.235)}{10} = \frac{28 + 0.648 - 13.41}{10} = \frac{15.238}{10} = 1.524$$
$$y^{(4)} = \frac{7 - 1.524 - 4(2.235)}{10} = \frac{7 - 1.524 - 8.94}{10} = \frac{-3.464}{10} = -0.346$$
$$z^{(4)} = \frac{-17 - 2(1.524) + 7(-0.346)}{-10} = \frac{-17 - 3.048 - 2.422}{-10} = \frac{-22.47}{-10} = 2.247$$

**Verificación criterio de parada (iter 3→4):**

$|x^{(4)} - x^{(3)}| = |1.524 - 1.543| = 0.019 < 0.02$ ✓

$|y^{(4)} - y^{(3)}| = |-0.346 - (-0.324)| = 0.022 > 0.02$ ✗ → se necesita otra iteración

**Iteración 5:**
$$x^{(5)} = \frac{28 - 2(-0.346) - 6(2.247)}{10} = \frac{28 + 0.692 - 13.482}{10} = \frac{15.21}{10} = 1.521$$
$$y^{(5)} = \frac{7 - 1.521 - 4(2.247)}{10} = \frac{7 - 1.521 - 8.988}{10} = \frac{-3.509}{10} = -0.351$$
$$z^{(5)} = \frac{-17 - 2(1.521) + 7(-0.351)}{-10} = \frac{-17 - 3.042 - 2.457}{-10} = \frac{-22.499}{-10} = 2.250$$

**Verificación criterio (iter 4→5):**

$|1.521 - 1.524| = 0.003 < 0.02$ ✓

$|-0.351 - (-0.346)| = 0.005 < 0.02$ ✓

$|2.250 - 2.247| = 0.003 < 0.02$ ✓

**Criterio satisfecho en la iteración 5.**

**Solución:** $x \approx 1.521$, $y \approx -0.351$, $z \approx 2.250$

**Verificación:** La solución exacta es $x = 1.5$, $y = -0.35$, $z = 2.25$.

---

## Ejercicio 5

**Sistema:**
$$a \quad\quad\quad + d = 2$$
$$a + 4b \quad\quad - d = 4$$
$$a \quad + c \quad\quad = 2$$
$$\quad\quad\quad\quad c + d = 2$$

### Análisis previo

La matriz del sistema es:
$$A = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 1 & 4 & 0 & -1 \\ 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 2 \\ 4 \\ 2 \\ 2 \end{pmatrix}$$

**Verificación diagonal dominancia:**
- Fila 1: $|1| \stackrel{?}{>} |0| + |0| + |1| = 1$ → $1 \not> 1$ ✗ (no estricta)
- Fila 2: $|4| > |1| + |0| + |-1| = 2$ → $4 > 2$ ✓
- Fila 3: $|1| > |1| + |0| + |0| = 1$ → $1 \not> 1$ ✗ (no estricta)
- Fila 4: $|1| > |0| + |1| + |0| = 1$ → $1 \not> 1$ ✗ (no estricta)

**La matriz NO es diagonal dominante estricta** → la convergencia no está garantizada por la condición suficiente.

### Fórmulas de Jacobi

$$a^{(k+1)} = 2 - d^{(k)}$$
$$b^{(k+1)} = \frac{4 - a^{(k)} + d^{(k)}}{4}$$
$$c^{(k+1)} = 2 - a^{(k)}$$
$$d^{(k+1)} = 2 - c^{(k)}$$

### Fórmulas de Gauss-Seidel

$$a^{(k+1)} = 2 - d^{(k)}$$
$$b^{(k+1)} = \frac{4 - a^{(k+1)} + d^{(k)}}{4}$$
$$c^{(k+1)} = 2 - a^{(k+1)}$$
$$d^{(k+1)} = 2 - c^{(k+1)}$$

### Iteraciones (semilla: todos cero)

#### Jacobi

| $k$ | $a$ | $b$ | $c$ | $d$ |
|-----|-----|-----|-----|-----|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 2 | 1 | 2 | 2 |
| 2 | 0 | 1 | 0 | 0 |
| 3 | 2 | 1 | 2 | 2 |
| 4 | 0 | 1 | 0 | 0 |

**Jacobi oscila indefinidamente entre dos estados** → **NO converge**.

#### Gauss-Seidel

| $k$ | $a$ | $b$ | $c$ | $d$ |
|-----|-----|-----|-----|-----|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 2 | 0.5 | 0 | 2 |
| 2 | 0 | 1.0 | 2 | 0 |
| 3 | 2 | 0.5 | 0 | 2 |

**Gauss-Seidel también oscila → NO converge.**

### ¿Por qué ocurre esto?

La solución exacta es $a = 1, b = 1, c = 1, d = 1$ (verificar: $1+1=2$, $1+4-1=4$, $1+1=2$, $1+1=2$).

El problema es que la matriz tiene **autovalores de la matriz de iteración con módulo = 1** (radio espectral $\rho = 1$). Esto provoca oscilación permanente.

La condición diagonal dominante **débil** (con $\geq$ en lugar de $>$) no garantiza convergencia. En este caso particular, la relación entre ecuaciones genera ciclos.

**Conclusión:** Para este sistema, los métodos iterativos no convergen. Se requiere un método directo (eliminación gaussiana) para obtener la solución.

---

## Ejercicio 6

**Matriz:**
$$A = \begin{pmatrix} 2 & -1 & 1 \\ 2 & 3 & 2 \\ -1 & -1 & 2 \end{pmatrix}$$

### Parte a) Análisis de convergencia (condición suficiente y necesaria)

#### Condición suficiente: Diagonal dominante estricta

- Fila 1: $|2| \stackrel{?}{>} |-1| + |1| = 2$ → $2 \not> 2$ ✗
- Fila 2: $|3| > |2| + |2| = 4$ → $3 \not> 4$ ✗
- Fila 3: $|2| > |-1| + |-1| = 2$ → $2 \not> 2$ ✗

**La condición suficiente NO se cumple.** No podemos garantizar convergencia por este criterio.

#### Condición necesaria y suficiente: Radio espectral < 1

**Matriz de iteración de Jacobi:**

$$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix}, \quad L+U = \begin{pmatrix} 0 & -1 & 1 \\ 2 & 0 & 2 \\ -1 & -1 & 0 \end{pmatrix}$$

$$B_J = -D^{-1}(L+U) = \begin{pmatrix} 0 & 1/2 & -1/2 \\ -2/3 & 0 & -2/3 \\ 1/2 & 1/2 & 0 \end{pmatrix}$$

**Polinomio característico de $B_J$:**

$$\det(B_J - \lambda I) = 0$$

$$-\lambda^3 + 0\cdot\lambda^2 + \left(\frac{1}{4} + \frac{1}{4} + \frac{4}{9} - \frac{1}{3}\right)\lambda + \cdots$$

Calculando el polinomio característico:

$$-\lambda\left(\lambda^2 - \frac{1}{4} - \frac{1}{9}\right) - \frac{1}{2}\left(\frac{2}{3}\lambda\right) + \cdots$$

Desarrollando $\det(B_J - \lambda I)$:

$$= -\lambda^3 + \lambda\left(\frac{1}{4} + \frac{1}{4} - \frac{4}{9}\right) + \left(\frac{1}{2}\cdot\frac{1}{2}\cdot 0 + \frac{1}{2}\cdot\frac{2}{3}\cdot\frac{1}{2} + (-\frac{1}{2})\cdot(-\frac{2}{3})\cdot\frac{1}{2}\right)$$

Calculando los elementos del determinante directamente:

$$\det\begin{pmatrix} -\lambda & 1/2 & -1/2 \\ -2/3 & -\lambda & -2/3 \\ 1/2 & 1/2 & -\lambda \end{pmatrix}$$

$$= -\lambda(\lambda^2 + 1/3) - \frac{1}{2}(\frac{2\lambda}{3} + \frac{1}{3}) + (-\frac{1}{2})(-\frac{\lambda}{3} + \frac{\lambda}{3})$$

Expandiendo por primera fila:

$$= -\lambda\left[(-\lambda)(-\lambda) - (-2/3)(1/2)\right] - \frac{1}{2}\left[(-2/3)(-\lambda) - (-2/3)(1/2)\right] + (-1/2)\left[(-2/3)(1/2) - (-\lambda)(1/2)\right]$$

$$= -\lambda[\lambda^2 + 1/3] - \frac{1}{2}[\frac{2\lambda}{3} + \frac{1}{3}] - \frac{1}{2}[-\frac{1}{3} + \frac{\lambda}{2}]$$

$$= -\lambda^3 - \frac{\lambda}{3} - \frac{\lambda}{3} - \frac{1}{6} + \frac{1}{6} - \frac{\lambda}{4}$$

$$= -\lambda^3 - \frac{11\lambda}{12}$$

$$= -\lambda\left(\lambda^2 + \frac{11}{12}\right) = 0$$

**Autovalores de $B_J$:**

$$\lambda_1 = 0, \quad \lambda_{2,3} = \pm\sqrt{-\frac{11}{12}} = \pm i\sqrt{\frac{11}{12}}$$

$$|\lambda_{2,3}| = \sqrt{\frac{11}{12}} \approx 0.957 < 1$$

**Radio espectral:** $\rho(B_J) \approx 0.957 < 1$ → **Jacobi converge.**

#### Análisis de Gauss-Seidel

La matriz de iteración de Gauss-Seidel es $B_{GS} = -(D+L)^{-1}U$.

Para matrices de Young (tipo I), $\rho(B_{GS}) = \rho(B_J)^2$. Sin embargo, esta matriz no es de tipo estrictamente tridiagonal, por lo que calculamos directamente.

$$D + L = \begin{pmatrix} 2 & 0 & 0 \\ 2 & 3 & 0 \\ -1 & -1 & 2 \end{pmatrix}, \quad U = \begin{pmatrix} 0 & -1 & 1 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$$

$$(D+L)^{-1} = \frac{1}{12}\begin{pmatrix} 6 & 0 & 0 \\ -4 & 4 & 0 \\ -1 & 2 & 6 \end{pmatrix}$$

$$B_{GS} = -(D+L)^{-1}U = \frac{1}{12}\begin{pmatrix} 0 & 6 & -6 \\ 0 & 4 & -12 \\ 0 & -1+0 & \cdots \end{pmatrix}$$

Calculando $B_{GS}$:

$$B_{GS} = -\frac{1}{12}\begin{pmatrix} 6 & 0 & 0 \\ -4 & 4 & 0 \\ -1 & 2 & 6 \end{pmatrix}\begin{pmatrix} 0 & -1 & 1 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} = -\frac{1}{12}\begin{pmatrix} 0 & -6 & 6 \\ 0 & 4 & 4 \\ 0 & 1 & 3 \end{pmatrix}$$

$$B_{GS} = \begin{pmatrix} 0 & 1/2 & -1/2 \\ 0 & -1/3 & -1/3 \\ 0 & -1/12 & -1/4 \end{pmatrix}$$

**Autovalores:** $\det(B_{GS} - \lambda I) = 0$

Como la primera columna de $B_{GS}$ es nula, $\lambda = 0$ es autovalor. Los otros se obtienen del bloque $2\times 2$:

$$\begin{vmatrix} -1/3 - \lambda & -1/3 \\ -1/12 & -1/4 - \lambda \end{vmatrix} = 0$$

$$(-1/3 - \lambda)(-1/4 - \lambda) - (1/3)(1/12) = 0$$

$$\lambda^2 + \frac{7}{12}\lambda + \frac{1}{12} - \frac{1}{36} = 0$$

$$\lambda^2 + \frac{7}{12}\lambda + \frac{2}{36} = 0 \quad\Rightarrow\quad \lambda^2 + \frac{7}{12}\lambda + \frac{1}{18} = 0$$

$$\lambda = \frac{-7/12 \pm \sqrt{49/144 - 4/18}}{2} = \frac{-7/12 \pm \sqrt{49/144 - 32/144}}{2} = \frac{-7/12 \pm \sqrt{17/144}}{2}$$

$$\lambda = \frac{-7/12 \pm \sqrt{17}/12}{2} = \frac{-7 \pm \sqrt{17}}{24}$$

$$\lambda_1 = \frac{-7 + 4.123}{24} \approx \frac{-2.877}{24} \approx -0.120$$

$$\lambda_2 = \frac{-7 - 4.123}{24} \approx \frac{-11.123}{24} \approx -0.463$$

**Radio espectral:** $\rho(B_{GS}) \approx 0.463 < 1$ → **Gauss-Seidel converge.**

Además, $\rho(B_{GS}) \approx 0.463 < \rho(B_J) \approx 0.957$, lo que confirma que **Gauss-Seidel converge más rápido**.

### Parte b) ¿"Cuando uno converge, el otro también"?

**La afirmación es FALSA en general.**

**Contraejemplo:** Considerar la matriz:
$$A = \begin{pmatrix} 1 & 2 & -2 \\ 1 & 1 & 1 \\ 2 & 2 & 1 \end{pmatrix}$$

Existen casos donde:
- Jacobi converge pero Gauss-Seidel diverge.
- Gauss-Seidel converge pero Jacobi diverge.

**En el caso del Ejercicio 6:** Ambos convergen, pero esto es una coincidencia de la estructura particular de esta matriz, no una regla general.

**Casos donde la implicación SÍ vale:**
1. Si la matriz es **simétrica definida positiva** → ambos pueden converger (aunque no siempre).
2. Si la matriz es **diagonal dominante estricta** → ambos convergen (condición suficiente).
3. Para matrices de **Young de tipo I** (matrices tridiagonales por bloques), si Jacobi converge, Gauss-Seidel converge con $\rho_{GS} = \rho_J^2$.

**Conclusión:** La afirmación es falsa como regla general. Solo bajo condiciones especiales (como diagonal dominante estricta) ambos métodos están garantizados a converger simultáneamente.

---

## Resumen de Criterios

| Criterio | Jacobi | Gauss-Seidel |
|----------|--------|--------------|
| Diagonal dominante estricta | ✓ converge | ✓ converge |
| $\rho(B) < 1$ (necesaria y suficiente) | ✓ converge | ✓ converge |
| Matriz SPD (simétrica def. positiva) | No garantizado | ✓ converge |
| Si Jacobi converge (caso general) | — | No se puede concluir |
| Si GS converge (caso general) | No se puede concluir | — |
| Matrices de Young tipo I | relacionados por $\rho_{GS} = \rho_J^2$ | |
