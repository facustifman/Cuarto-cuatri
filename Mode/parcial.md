# Parcial — Métodos Numéricos (Curso 08 - Balzarotti, 28/04/26)

---

# Ejercicio 1 — Choque elástico unidimensional

## Planteo del sistema

Con $m_2$ en reposo ($v_{2_0} = 0$), las ecuaciones del choque son:

$$f_1(v_{1f}, v_{2f}) = m_1 v_0 - m_1 v_{1f} - m_2 v_{2f} = 0$$
$$f_2(v_{1f}, v_{2f}) = \tfrac{1}{2}m_1 v_0^2 - \tfrac{1}{2}m_1 v_{1f}^2 - \tfrac{1}{2}m_2 v_{2f}^2 = 0$$

## 1a) Newton-Raphson para sistemas no lineales

El esquema general es:

$$\mathbf{x}^{k+1} = \mathbf{x}^k - J(\mathbf{x}^k)^{-1} \, \mathbf{F}(\mathbf{x}^k)$$

donde $\mathbf{x} = [v_{1f},\ v_{2f}]^T$, es decir, se resuelve el sistema lineal $J^k \Delta\mathbf{x} = -\mathbf{F}^k$ y luego se actualiza.

**Jacobiano:**

$$J(\mathbf{x}) = \begin{bmatrix} \partial f_1/\partial v_{1f} & \partial f_1/\partial v_{2f} \\ \partial f_2/\partial v_{1f} & \partial f_2/\partial v_{2f} \end{bmatrix} = \begin{bmatrix} -m_1 & -m_2 \\ -m_1 v_{1f} & -m_2 v_{2f} \end{bmatrix}$$

**Esquema iterativo completo** (expresado en términos de los datos del problema y las iteraciones $k$ y $k+1$):

$$\begin{bmatrix} -m_1 & -m_2 \\ -m_1 v_{1f}^k & -m_2 v_{2f}^k \end{bmatrix} \begin{bmatrix} \Delta v_{1f} \\ \Delta v_{2f} \end{bmatrix} = -\begin{bmatrix} m_1 v_0 - m_1 v_{1f}^k - m_2 v_{2f}^k \\ \tfrac{1}{2}m_1 v_0^2 - \tfrac{1}{2}m_1(v_{1f}^k)^2 - \tfrac{1}{2}m_2(v_{2f}^k)^2 \end{bmatrix}$$

$$v_{1f}^{k+1} = v_{1f}^k + \Delta v_{1f}, \qquad v_{2f}^{k+1} = v_{2f}^k + \Delta v_{2f}$$

Resolviendo el sistema 2×2 por regla de Cramer:

$$\det(J^k) = (-m_1)(-m_2 v_{2f}^k) - (-m_2)(-m_1 v_{1f}^k) = m_1 m_2 v_{2f}^k - m_1 m_2 v_{1f}^k = m_1 m_2 (v_{2f}^k - v_{1f}^k)$$

$$\Delta v_{1f} = \frac{1}{\det(J^k)}\det\begin{bmatrix} -(m_1 v_0 - m_1 v_{1f}^k - m_2 v_{2f}^k) & -m_2 \\ -(\tfrac{1}{2}m_1 v_0^2 - \tfrac{1}{2}m_1(v_{1f}^k)^2 - \tfrac{1}{2}m_2(v_{2f}^k)^2) & -m_2 v_{2f}^k \end{bmatrix}$$

$$\Delta v_{2f} = \frac{1}{\det(J^k)}\det\begin{bmatrix} -m_1 & -(m_1 v_0 - m_1 v_{1f}^k - m_2 v_{2f}^k) \\ -m_1 v_{1f}^k & -(\tfrac{1}{2}m_1 v_0^2 - \tfrac{1}{2}m_1(v_{1f}^k)^2 - \tfrac{1}{2}m_2(v_{2f}^k)^2) \end{bmatrix}$$

---

# Ejercicio 2 — Gráfico de funciones y punto fijo

## 2a) Identificar cuál curva es $f$ y estimar raíces

**¿Cuál es $f$?**
Las curvas $g_1$ y $g_2$ fueron construidas para reformular $f(x)=0$ como $x = g(x)$. Por eso:
- $f$ es la curva que **cruza el eje $y = 0$** (tiene raíces visibles).
- $g_1$ y $g_2$ tienen sus **puntos fijos** (intersecciones con la recta $y = x$) en los mismos valores $x$ donde $f$ se anula.

Con este criterio, $f$ es la curva que tiene cruces por cero; $g_1$ y $g_2$ son las otras dos.

**Estimación de raíces de $f$** (leyendo la grilla, escala igual en ambos ejes):

| Raíz | Valor representativo | Cota de error absoluto |
|------|---------------------|------------------------|
| $x_1^*$ | $\approx -3.5$ | $\pm 0.5$ (intervalo adecuado: $[-4,\,-3]$) |
| $x_2^*$ | $\approx 0.8$ | $\pm 0.5$ (intervalo inadecuado dado: $[0.33,\,1.33]$) |

## 2b) Convergencia según Teorema de Punto Fijo

El **Teorema de Punto Fijo** garantiza convergencia de $x^{k+1} = g(x^k)$ si existe un intervalo $[a, b]$ tal que:
1. $g$ mapea $[a, b]$ en sí mismo: $g([a,b]) \subseteq [a,b]$
2. $|g'(x)| \leq L < 1$ para todo $x \in [a, b]$ (condición de contracción)

**Criterio gráfico para la derivada:** la pendiente de la curva $g$ en el punto fijo $x^*$ (intersección con $y = x$) debe tener valor absoluto menor que 1, es decir, la curva debe cruzar la diagonal con pendiente más "plana" que 45°.

Para cada raíz $x_i^*$ y cada función $g_j$:

- Si $|g_j'(x_i^*)| < 1$ (pendiente más plana que la diagonal): **converge**.
  - **Intervalo más angosto:** el más pequeño tal que $g_j$ mapea en sí mismo (leer directamente en el gráfico).
  - **Intervalo más ancho:** el más grande donde se sigue cumpliendo $|g_j'| < 1$ y el mapeo en sí mismo (ampliar hasta donde la pendiente alcanza $\pm 1$).
- Si $|g_j'(x_i^*)| > 1$ (pendiente más pronunciada que la diagonal): **diverge** en ese punto.

---

# Ejercicio 3 — EDO de radiación

## Ecuación diferencial

$$-mC\frac{dT}{dt} = \sigma\varepsilon S(T^4 - T_\infty^4)$$

Reescribiendo y usando $C(T) = c_0 + c_1 T = 1 + T$ y $\alpha = \dfrac{\sigma\varepsilon S}{m} = 4\times10^{-7}$:

$$\frac{dT}{dt} = f(T) = \frac{-4\times10^{-7}}{1+T}\,(T^4 - 473^4)$$

**Datos:** $T_0 = T(0) = 298$ K, $T_\infty = 473$ K.

> Como $T_0 < T_\infty$: $T^4 - 473^4 < 0 \Rightarrow dT/dt > 0$, el cuerpo se calienta hacia $T_\infty$ (coherente físicamente).

**Valores auxiliares:**

$$298^4 = 7{,}886 \times 10^9, \qquad 473^4 = 5{,}005 \times 10^{10}$$

$$f(298) = \frac{-4\times10^{-7}}{299}\,(7{,}886\times10^9 - 5{,}005\times10^{10}) = \frac{4\times10^{-7} \times 4{,}217\times10^{10}}{299} = \frac{16{,}867}{299} = 56.41\ \text{K/s}$$

---

## 3a) Runge-Kutta orden 2 con mínimo esfuerzo (h = 2, un solo paso)

El método de Heun (RK2) dado:

$$q_{1u} = h\,f(u_n,\,t_n), \quad q_{2u} = h\,f(u_n + q_{1u},\,t_{n+1}), \quad u_{n+1} = u_n + \tfrac{1}{2}(q_{1u} + q_{2u})$$

**Evaluación $q_1$:**

$$q_1 = 2 \times f(298) = 2 \times 56.41 = 112.83\ \text{K}$$

**Evaluación $q_2$** con $T_\text{pred} = 298 + 112.83 = 410.83$ K:

$$410.83^4 \approx 2.849\times10^{10}$$

$$f(410.83) = \frac{-4\times10^{-7}}{411.83}\,(2{,}849\times10^{10} - 5{,}005\times10^{10}) = \frac{4\times10^{-7}\times 2{,}156\times10^{10}}{411.83} = \frac{8{,}624}{411.83} = 20.94\ \text{K/s}$$

$$q_2 = 2 \times 20.94 = 41.88\ \text{K}$$

**Resultado:**

$$T(2) = 298 + \tfrac{1}{2}(112.83 + 41.88) = 298 + 77.36 \approx \boxed{375\ \text{K}}$$

---

## 3b) Euler Implícito con mínimo esfuerzo (h = 2, un solo paso)

Euler implícito: $T_1 = T_0 + h\,f(T_1)$, es decir:

$$g(T_1) = T_1 - 298 + \frac{8\times10^{-7}}{1+T_1}(T_1^4 - 473^4) = 0$$

Se resuelve con **Newton-Raphson**: $T_1^{k+1} = T_1^k - g(T_1^k)/g'(T_1^k)$

**Derivada:**

$$g'(T) = 1 + 8\times10^{-7}\,\frac{3T^4 + 4T^3 + 473^4}{(1+T)^2}$$

### Iteración 1 — semilla $T_1^{(0)} = 298$

$$g(298) = 0 + \frac{8\times10^{-7}}{299}\times(-4{,}217\times10^{10}) = \frac{-33{,}734}{299} = -112.82$$

$$g'(298) = 1 + 8\times10^{-7}\,\frac{3(7{,}886\times10^9)+4(298^3)+5{,}005\times10^{10}}{299^2} \approx 1 + 0.661 = 1.661$$

$$T_1^{(1)} = 298 - \frac{-112.82}{1.661} = 298 + 67.9 = 365.9\ \text{K}$$

### Iteración 2 — $T_1^{(1)} = 365.9$

$$365.9^4 \approx 1{,}793\times10^{10}$$

$$g(365.9) = 67.9 + \frac{8\times10^{-7}}{366.9}\times(1{,}793\times10^{10}-5{,}005\times10^{10}) = 67.9 - 70.0 = -2.10$$

$$g'(365.9) \approx 1 + 0.618 = 1.618$$

$$T_1^{(2)} = 365.9 + \frac{2.10}{1.618} = 365.9 + 1.30 = 367.2\ \text{K}$$

### Iteración 3 — verificación

$$g(367.2) \approx -0.007 \approx 0\ \checkmark$$

$$\boxed{T(2) \approx 367\ \text{K}}$$

---

# Ejercicio 4 — Sistema lineal

$$A\mathbf{x} = \mathbf{0}, \qquad A = \begin{bmatrix} 3 & 0 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3 \end{bmatrix}$$

## 4a) Matriz de iteración de Jacobi y autovalor por Newton-Raphson

Descomposición $A = D + L + U$:

$$D = \begin{bmatrix} 3&0&0\\0&3&0\\0&0&3 \end{bmatrix}, \qquad L+U = \begin{bmatrix} 0&0&1\\1&0&1\\1&1&0 \end{bmatrix}$$

$$T_J = -D^{-1}(L+U) = -\frac{1}{3}\begin{bmatrix} 0&0&1\\1&0&1\\1&1&0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & -\tfrac{1}{3} \\ -\tfrac{1}{3} & 0 & -\tfrac{1}{3} \\ -\tfrac{1}{3} & -\tfrac{1}{3} & 0 \end{bmatrix}$$

**Polinomio característico** $\det(T_J - \lambda I) = 0$:

Expandiendo el determinante:

$$-\lambda^3 + \frac{2\lambda}{9} - \frac{1}{27} = 0 \implies 27\lambda^3 - 6\lambda + 1 = 0$$

**Elección de semilla para Newton-Raphson:**

Por el Círculo de Gershgorin, los autovalores satisfacen $|\lambda| \leq \frac{2}{3}$.
Semilla: $\lambda^{(0)} = \frac{1}{3}$ (valor intuitivo en el rango esperado, también sugerido por la simetría de la matriz).

**Verificación directa:**

$$p\!\left(\tfrac{1}{3}\right) = 27\left(\tfrac{1}{3}\right)^3 - 6\left(\tfrac{1}{3}\right) + 1 = 1 - 2 + 1 = 0\ \checkmark$$

La semilla es exactamente un cero $\Rightarrow$ Newton-Raphson converge en 0 iteraciones.

$$\boxed{\lambda_1 = \frac{1}{3} \approx 0.333}$$

**Factorización completa:**

$$27\lambda^3 - 6\lambda + 1 = (3\lambda - 1)(9\lambda^2 + 3\lambda - 1)$$

Los otros dos autovalores ($9\lambda^2 + 3\lambda - 1 = 0$):

$$\lambda_{2,3} = \frac{-3 \pm \sqrt{9+36}}{18} = \frac{-1 \pm \sqrt{5}}{6} \implies \lambda_2 \approx 0.206,\quad \lambda_3 \approx -0.539$$

**Radio espectral:** $\rho(T_J) = \max|\lambda_i| = 0.539 < 1 \Rightarrow$ **Jacobi converge** para este sistema.

---

## 4b) Una iteración de Gauss-Seidel desde $\mathbf{x}^{(0)} = [0;\ 0;\ 1]^T$

Fórmulas GS (despejando la diagonal, RHS = 0):

$$x_1^{(k+1)} = \frac{0 - 0\cdot x_2^{(k)} - 1\cdot x_3^{(k)}}{3} = \frac{-x_3^{(k)}}{3}$$

$$x_2^{(k+1)} = \frac{0 - 1\cdot x_1^{(k+1)} - 1\cdot x_3^{(k)}}{3} = \frac{-x_1^{(k+1)} - x_3^{(k)}}{3}$$

$$x_3^{(k+1)} = \frac{0 - 1\cdot x_1^{(k+1)} - 1\cdot x_2^{(k+1)}}{3} = \frac{-x_1^{(k+1)} - x_2^{(k+1)}}{3}$$

**Aplicando con $\mathbf{x}^{(0)} = [0,\ 0,\ 1]^T$:**

$$x_1^{(1)} = \frac{-1}{3} = -\frac{1}{3}$$

$$x_2^{(1)} = \frac{-(-\tfrac{1}{3}) - 1}{3} = \frac{\tfrac{1}{3} - 1}{3} = \frac{-\tfrac{2}{3}}{3} = -\frac{2}{9}$$

$$x_3^{(1)} = \frac{-(-\tfrac{1}{3}) - (-\tfrac{2}{9})}{3} = \frac{\tfrac{3}{9} + \tfrac{2}{9}}{3} = \frac{\tfrac{5}{9}}{3} = \frac{5}{27}$$

$$\boxed{\mathbf{x}^{(1)} = \begin{bmatrix} -1/3 \\ -2/9 \\ 5/27 \end{bmatrix} \approx \begin{bmatrix} -0.333 \\ -0.222 \\ 0.185 \end{bmatrix}}$$

---

## Resumen de resultados

| Ejercicio | Resultado |
|-----------|-----------|
| 3a) RK2 (Heun, h=2) | $T(2) \approx \mathbf{375\ K}$ |
| 3b) Euler Implícito (h=2) | $T(2) \approx \mathbf{367\ K}$ |
| 4a) Autovalor de $T_J$ | $\lambda_1 = \mathbf{1/3}$, semilla $\lambda^{(0)} = 1/3$ (cero exacto) |
| 4b) GS — 1 iteración | $\mathbf{x}^{(1)} = [-1/3,\ -2/9,\ 5/27]^T$ |
