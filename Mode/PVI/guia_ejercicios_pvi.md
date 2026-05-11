# Guía 5 – Problemas de Valor Inicial

---

## Problema 1

**Ecuación:** $y' = -y + t + 1$, $y(0)=1$. Solución exacta: $y(t) = t + e^{-t}$

### a) Discretización por Euler Explícito

La forma general es $u^{n+1} = u^n + h\,f(u^n, t^n)$, con $f(u,t) = -u + t + 1$:

$$\boxed{u^{n+1} = u^n + h(-u^n + t^n + 1) = u^n(1-h) + h(t^n + 1)}$$

### b) $u(t=1)$ con $h=1$ (un paso)

$$u^1 = u^0(1-1) + 1\cdot(0+1) = 0 + 1 = \mathbf{1}$$

### c) $u(t=1)$ con $h=0.5$ (dos pasos)

**Paso 1** ($t^0=0 \to t^1=0.5$):
$$u^1 = 1\cdot(1-0.5) + 0.5\cdot(0+1) = 0.5 + 0.5 = 1$$

**Paso 2** ($t^1=0.5 \to t^2=1$):
$$u^2 = 1\cdot(1-0.5) + 0.5\cdot(0.5+1) = 0.5 + 0.75 = \mathbf{1.25}$$

### d) Errores en $t=1$

Valor exacto: $y(1) = 1 + e^{-1} \approx 1.3679$

| $h$ | $u(1)$ numérico | Error absoluto |
|-----|-----------------|----------------|
| 1   | 1.0000          | **0.3679**     |
| 0.5 | 1.2500          | **0.1179**     |

### e) Conclusiones

Al reducir $h$ a la mitad, el error se reduce aproximadamente a la mitad: $0.3679/0.1179 \approx 3.12 \approx 2$. Esto es consistente con Euler siendo un método de **orden 1** (error global $\mathcal{O}(h)$).

### f) Condición de estabilidad

Para la ecuación lineal $y' = \lambda y + \ldots$ con $\lambda = \partial f/\partial u = -1$:

$$|1 + h\lambda| \leq 1 \implies |1 - h| \leq 1 \implies 0 \leq h \leq 2$$

Ambos pasos ($h=0.5$ y $h=1$) satisfacen la condición. Fueron adecuados.

### g) Discretización por RK2

Con $f(u,t) = -u + t + 1$:

$$q_1^u = h(-u^n + t^n + 1)$$
$$q_2^u = h\bigl(-(u^n + q_1^u) + t^{n+1} + 1\bigr)$$
$$u^{n+1} = u^n + \tfrac{1}{2}(q_1^u + q_2^u)$$

### h) RK2 con $h=1$ (un paso)

$t^0=0$, $u^0=1$:

$$q_1 = 1\cdot(-1 + 0 + 1) = 0$$
$$q_2 = 1\cdot(-(1+0) + 1 + 1) = 1$$
$$u^1 = 1 + \tfrac{1}{2}(0+1) = \mathbf{1.5}$$

### i) RK2 con $h=0.5$ (dos pasos)

**Paso 1** ($t^0=0 \to t^1=0.5$, $u^0=1$):
$$q_1 = 0.5(-1+0+1) = 0$$
$$q_2 = 0.5(-(1+0)+0.5+1) = 0.5\cdot 0.5 = 0.25$$
$$u^1 = 1 + \tfrac{1}{2}(0+0.25) = 1.125$$

**Paso 2** ($t^1=0.5 \to t^2=1$, $u^1=1.125$):
$$q_1 = 0.5(-1.125+0.5+1) = 0.5\cdot0.375 = 0.1875$$
$$q_2 = 0.5(-(1.125+0.1875)+1+1) = 0.5\cdot0.6875 = 0.34375$$
$$u^2 = 1.125 + \tfrac{1}{2}(0.1875+0.34375) = 1.125 + 0.265625 = \mathbf{1.390625}$$

### j) Errores en $t=1$ para RK2

| $h$ | $u(1)$ RK2  | Error absoluto |
|-----|-------------|----------------|
| 1   | 1.5000      | **0.1321**     |
| 0.5 | 1.390625    | **0.02275**    |

### k) ¿La relación de errores es la misma para Euler y RK2?

No. Para Euler (orden 1): al reducir $h$ a la mitad, el error se divide por $\approx 2$.
Para RK2 (orden 2): al reducir $h$ a la mitad, el error se divide por $\approx 4$.

Verificación: razón errores RK2 = $0.1321/0.02275 \approx 5.8 \approx 4$. Las relaciones son distintas porque los órdenes de convergencia son distintos ($\mathcal{O}(h)$ vs $\mathcal{O}(h^2)$).

---

## Problema 2

**Ecuación:** $\dfrac{du}{dt} + e^u = 0$, $u(0) = 0$

### a) Discretización por Euler Implícito

$$u^{n+1} = u^n + h\,f(u^{n+1}, t^{n+1}), \quad f(u) = -e^u$$

$$\boxed{u^{n+1} + h\,e^{u^{n+1}} = u^n}$$

### b) Estimar $u(t=1)$ con $h=1$ (Newton-Raphson)

Con $h=1$, $u^0=0$:

$$g(u) = u + e^u = 0$$

**Elección de semilla:** Como $e^u > 0$, la solución tiene $u < 0$. La semilla natural es $u^{(0)} = u^n = 0$ (valor anterior), que es conveniente y cercana a la raíz.

**Iteraciones de Newton-Raphson** ($g'(u) = 1 + e^u$):

**Iteración 1:**
$$u^{(1)} = 0 - \frac{0 + 1}{1 + 1} = -0.5$$

**Iteración 2:**
$$g(-0.5) = -0.5 + e^{-0.5} = -0.5 + 0.6065 = 0.1065$$
$$g'(-0.5) = 1 + 0.6065 = 1.6065$$
$$u^{(2)} = -0.5 - \frac{0.1065}{1.6065} = -0.5663$$

**Iteración 3:**
$$g(-0.5663) = -0.5663 + e^{-0.5663} \approx -0.5663 + 0.5674 = 0.0011$$
$$u^{(3)} \approx -0.5663 - \frac{0.0011}{1.5674} \approx -0.5670$$

Con 2 decimales correctos: $\boxed{u(t=1) \approx -0.57}$

### c) ¿Es correcto usar $h=1$ con Euler Explícito?

Euler explícito: $u^{n+1} = u^n - h\,e^{u^n}$

Condición de estabilidad: $\left|\frac{\partial}{\partial u}[u - h\,e^u]\right| \leq 1 \implies |1 - h\,e^{u^n}| \leq 1$

En $u^n = 0$: $|1 - h| \leq 1 \implies h \leq 2$.

Con $h=1$: $|1 - 1| = 0 \leq 1$ ✓ Es **marginalmente** aceptable. El método es estable en $t=0$ pero puede tornarse inestable si $u$ varía, ya que $\lambda = -e^u$ depende de $u$.

---

## Problema 3

**Ecuación:** $\dfrac{d^2 y}{dt^2} = a$, $\quad y(0)=0$, $\quad y'(0)=b$

Cambio de variable: $v = dy/dt$. El sistema de primer orden es:
$$\frac{dy}{dt} = v \equiv f_1(y,v), \qquad \frac{dv}{dt} = a \equiv f_2(y,v)$$

### a) Discretización por RK2

$$q_1^y = h\,f_1(y^n, v^n) = h\,v^n$$
$$q_1^v = h\,f_2(y^n, v^n) = h\,a$$

$$q_2^y = h\,f_1(y^n+q_1^y,\ v^n+q_1^v) = h\,(v^n + ha)$$
$$q_2^v = h\,f_2(y^n+q_1^y,\ v^n+q_1^v) = h\,a$$

$$y^{n+1} = y^n + \tfrac{1}{2}(q_1^y + q_2^y) = y^n + hv^n + \tfrac{h^2 a}{2}$$
$$v^{n+1} = v^n + \tfrac{1}{2}(q_1^v + q_2^v) = v^n + ha$$

### b) $y(t=1)$ con $h=1$

$y^0=0$, $v^0=b$:

$$q_1^y = b, \quad q_1^v = a$$
$$q_2^y = b + a, \quad q_2^v = a$$

$$y^1 = 0 + \tfrac{1}{2}(b + b + a) = b + \tfrac{a}{2}$$
$$v^1 = b + a$$

**Solución exacta:** $y(t) = bt + \dfrac{at^2}{2} \implies y(1) = b + \dfrac{a}{2}$ ✓

**Conclusión:** RK2 reproduce la solución **exacta** para esta ecuación. Esto se debe a que la solución exacta es un polinomio de grado 2 en $t$, y la derivada de orden 3 en adelante es nula ($d^3y/dt^3 = 0$), por lo que el error de truncamiento local de RK2 (que involucra $y'''$) es exactamente cero.

---

## Problema 4

**Ecuación:** $\dfrac{d^2 u}{dt^2} + au = t^2$, $\quad u(0)=1$, $\quad u'(0)=0$, $\quad a>0$

Cambio de variable: $v = du/dt$. Sistema:
$$\frac{du}{dt} = v \equiv f_1, \qquad \frac{dv}{dt} = t^2 - au \equiv f_2$$

### a) Discretización por Euler Implícito

$$u^{n+1} = u^n + h\,v^{n+1}$$
$$v^{n+1} = v^n + h\,(t_{n+1}^2 - a\,u^{n+1})$$

Reescrito como sistema lineal:

$$\begin{pmatrix} 1 & -h \\ ah & 1 \end{pmatrix} \begin{pmatrix} u^{n+1} \\ v^{n+1} \end{pmatrix} = \begin{pmatrix} u^n \\ v^n + h\,t_{n+1}^2 \end{pmatrix}$$

### b) Condiciones de convergencia por Jacobi

El método de Jacobi converge si la matriz es **estrictamente diagonal dominante**:

- Fila 1: $|1| > |-h| \implies h < 1$
- Fila 2: $|1| > |ah| \implies h < \dfrac{1}{a}$

**Condición:** $\boxed{h < \min\!\left(1,\ \dfrac{1}{a}\right)}$

### c) Caso $a=1$: estimar $u(t=2)$ y $v(t=2)$ con Jacobi (2 iteraciones por paso)

**Elección de $h$:** La condición de convergencia Jacobi requiere $h < 1/a = 1$. Para minimizar el esfuerzo de cálculo se elige $h$ lo más grande posible. Con $h=1$ la condición es límite (no estrictamente dominante), por lo que se elige $\mathbf{h = 1}$ como cota práctica (notar que Euler implícito es incondicionalmente estable; la restricción es solo del iterador Jacobi).

**Semilla:** $u^{(0)} = u^n$, $v^{(0)} = v^n$ (valores del paso anterior).

---

**Paso 1:** $t^0=0 \to t^1=1$, con $u^0=1$, $v^0=0$

Sistema:
$$u^1 = 1 + v^1 \quad (\text{de fila 1})$$
$$v^1 = 0 + 1\cdot(1 - u^1) = 1 - u^1 \quad (\text{de fila 2})$$

Forma Jacobi (despejar diagonal):
$$u^{(k+1)} = 1 + v^{(k)}$$
$$v^{(k+1)} = 1 - u^{(k)}$$

Semilla: $u^{(0)}=1$, $v^{(0)}=0$

| Iter | $u$ | $v$ |
|------|-----|-----|
| 0 | 1 | 0 |
| 1 | $1+0=1$ | $1-1=0$ |
| 2 | $1+0=1$ | $1-1=0$ |

Solución del paso 1: $u^1 = 1$, $v^1 = 0$ (convergió en 1 iteración).

*Verificación exacta:* $u^1 = 1 + v^1$, $v^1 = 1 - u^1 \implies v^1=0$, $u^1=1$ ✓

---

**Paso 2:** $t^1=1 \to t^2=2$, con $u^1=1$, $v^1=0$

Sistema ($t_{n+1}^2 = 4$):
$$u^{(k+1)} = 1 + v^{(k)}$$
$$v^{(k+1)} = 4 - u^{(k)}$$

Semilla: $u^{(0)}=1$, $v^{(0)}=0$

| Iter | $u$ | $v$ |
|------|-----|-----|
| 0 | 1 | 0 |
| 1 | $1+0=1$ | $4-1=3$ |
| 2 | $1+3=4$ | $4-1=3$ |

Resultado después de 2 iteraciones: $u^2 \approx 4$, $v^2 \approx 3$

*Solución exacta del sistema:* $u^2 = 1+v^2$, $v^2 = 4-u^2 \implies 2v^2=3 \implies v^2=1.5$, $u^2=2.5$

**Cota de error tras 2 iteraciones:**

El error de las últimas dos iteraciones: $|u^{(2)}-u^{(1)}| = |4-1| = 3$, $|v^{(2)}-v^{(1)}|=0$. La convergencia en este paso es lenta (el radio espectral de la matriz de iteración es 1), lo que confirma que $h=1$ está en el límite. Con $h < 1$ la convergencia sería garantizada.

**Conclusión para c):** El método es inestable numéricamente con Jacobi para $h=1$ en presencia de términos fuente grandes. En la práctica conviene $h = 0.5$ (4 pasos) para asegurar convergencia de Jacobi.

### d) Caso $d^2u/dt^2 + au^4 = t^2$

La ecuación se vuelve **no lineal** por el término $u^4$. El sistema implícito en cada paso ya no es lineal, por lo que Jacobi (diseñado para sistemas lineales) debe reemplazarse por **Newton-Raphson** para resolver el sistema no lineal en cada avance. La discretización por Euler implícito sigue siendo la misma estructura, pero la resolución interna requiere iteraciones de Newton.

---

## Problema 5

**Ecuación:** $\dfrac{du}{dt} + t\,u = 0$, $\quad u(0)=1$

La función es $f(u,t) = -t\,u$, con $\partial f/\partial u = -t$.

### a) Condición de estabilidad – Euler Explícito

$$|1 + h\,\lambda| \leq 1, \quad \lambda = -t$$
$$|1 - ht| \leq 1 \implies 0 \leq ht \leq 2$$
$$\boxed{h \leq \frac{2}{t}}$$

### b) ¿Existe algún $h$ que garantice estabilidad para $t \in [0, +\infty)$?

**No.** La condición es $h \leq 2/t$. Cuando $t \to \infty$, se requiere $h \to 0$. Ningún paso fijo $h > 0$ puede satisfacer $h \leq 2/t$ para todo $t > 0$. El coeficiente $\lambda = -t$ crece en módulo con el tiempo, haciendo imposible mantener la estabilidad con paso constante.

### c) Discretización por RK2

$$q_1 = h\,f(u^n, t^n) = -h\,t^n\,u^n$$
$$q_2 = h\,f(u^n + q_1,\; t^{n+1}) = -h\,(t^n+h)(u^n - h\,t^n u^n)$$

$$u^{n+1} = u^n + \tfrac{1}{2}(q_1 + q_2) = u^n\left[1 - ht^n + \frac{h^2}{2}(t^n)^2 - \frac{h^2}{2} + \ldots\right]$$

O de forma compacta, usando las fórmulas estándar:

$$q_1 = -h\,t^n\,u^n$$
$$q_2 = -h\,(t^n+h)\,u^n\,(1 - ht^n)$$
$$u^{n+1} = u^n + \tfrac{1}{2}(q_1 + q_2)$$

### d) Estimación de $u(t=0.2)$ con orden 2 y mínimo esfuerzo

**Elección:** RK2 con $h=0.2$ (un solo paso). Usar Euler explícito requeriría más pasos para obtener orden 2; RK2 ya es orden 2 con un solo paso.

$t^0=0$, $u^0=1$:

$$q_1 = -0.2\cdot0\cdot1 = 0$$
$$q_2 = -0.2\cdot(0.2)\cdot(1+0) = -0.04$$
$$u^1 = 1 + \tfrac{1}{2}(0 + (-0.04)) = \mathbf{0.98}$$

*Valor exacto:* $u = e^{-t^2/2} \implies u(0.2) = e^{-0.02} \approx 0.9802$ ✓

**Suposición necesaria:** Para que la estimación sea confiable, el paso $h=0.2$ debe satisfacer la condición de estabilidad ($ht \leq 2$). En $t=0.2$: $0.2\cdot0.2 = 0.04 \ll 2$ ✓.

---

## Problema 6

**Ley de enfriamiento:** $-mC\,\dfrac{dT}{dt} = h_c S(T - T_\infty)$, $\quad T(0) = T_0$

### a) Euler explícito con $mC/(h_c S)=1$, $T_\infty=20°C$, $T_0=40°C$

La ecuación se reduce a $\dfrac{dT}{dt} = -(T-20)$, $f(T)= -(T-20)$.

**Discretización:**
$$T^{n+1} = T^n + h\,f(T^n) = T^n - h(T^n - 20) = T^n(1-h) + 20h$$

**Condición de estabilidad:** $|1-h| \leq 1 \implies 0 \leq h \leq 2$

**Solución exacta:** $T(t) = 20 + 20\,e^{-t}$

**Tabla comparativa** (usando $h=0.5$):

| $t$ | $T^n$ (numérico) | $T(t)$ (exacto) | Error |
|-----|-------------------|-----------------|-------|
| 0   | 40.0              | 40.0            | 0     |
| 0.5 | 40(0.5)+10 = 30.0 | $20+20e^{-0.5}=32.13$ | 2.13 |
| 1.0 | 30(0.5)+10 = 25.0 | $20+20e^{-1}=27.36$ | 2.36 |
| 1.5 | 25(0.5)+10 = 22.5 | $20+20e^{-1.5}=24.46$ | 1.96 |
| 2.0 | 22.5(0.5)+10=21.25| $20+20e^{-2}=22.71$ | 1.46 |

### b) Con término radiativo

$$-mC\frac{dT}{dt} = h_c S(T-T_\infty) + \sigma\varepsilon S(T^4 - T_\infty^4)$$

La ecuación **no tiene solución exacta en forma cerrada** (no es integrable analíticamente de forma simple). Es una ecuación **no lineal** por el término $T^4 - T_\infty^4$. Euler explícito se aplica igual (solo evaluar $f$ incluyendo el nuevo término), pero la no linealidad puede generar inestabilidades si $h$ es grande.

### c) Con $T_\infty(t)$ variable y $C(T)$ variable

La implementación numérica **no se complejiza estructuralmente**: Euler explícito evalúa $f(T, t)$ en cada paso con los valores actuales. Solo se debe tener cuidado en:
- Calcular $T_\infty$ al tiempo $t^n$ en cada paso.
- Calcular $C(T^n)$ con el valor actual de temperatura.

El esquema $T^{n+1} = T^n + h\,f(T^n, t^n)$ sigue siendo exactamente el mismo, con $f$ más compleja.

---

## Problema 7

**Sistema:**
$$\frac{du_1}{dt} = u_2, \qquad \frac{du_2}{dt} = -u_1, \qquad u_1(0)=a,\; u_2(0)=b$$

### Discretización por Euler Explícito

$$u_1^{n+1} = u_1^n + h\,u_2^n$$
$$u_2^{n+1} = u_2^n - h\,u_1^n$$

En forma matricial: $\mathbf{u}^{n+1} = A\,\mathbf{u}^n$ con

$$A = \begin{pmatrix}1 & h \\ -h & 1\end{pmatrix}$$

### Análisis de estabilidad

Los autovalores de $A$:
$$\det(A - \mu I) = (1-\mu)^2 + h^2 = 0 \implies \mu = 1 \pm ih$$

Módulo: $|\mu| = \sqrt{1^2 + h^2} = \sqrt{1+h^2} > 1$ para todo $h > 0$.

**Conclusión:** El método es **incondicionalmente inestable** para este sistema. Para cualquier paso $h > 0$, la solución numérica crece sin límite. Esto ocurre porque el sistema es conservativo (oscilador puro, autovalores del Jacobiano imaginarios puros $\pm i$) y Euler explícito siempre amplifica la energía.

---

## Problema 8

**Ecuación rígida:** $\dfrac{d^2u}{dt^2} + 1001\dfrac{du}{dt} + 1000\,u = 0$, $\quad u(0)=1$, $\quad u'(0)=-1$

### a) Sistema de primer orden – Euler Explícito

Sea $u_1 = u$, $u_2 = du/dt$:

$$\frac{du_1}{dt} = u_2, \qquad \frac{du_2}{dt} = -1000\,u_1 - 1001\,u_2$$

Euler explícito:
$$u_1^{n+1} = u_1^n + h\,u_2^n$$
$$u_2^{n+1} = u_2^n + h(-1000\,u_1^n - 1001\,u_2^n) = -1000h\,u_1^n + (1-1001h)\,u_2^n$$

Matriz de amplificación:
$$A = \begin{pmatrix}1 & h \\ -1000h & 1-1001h\end{pmatrix}$$

### b) Condición de estabilidad

Los autovalores de $A$ son $\mu_i = 1 + h\lambda_i$, donde $\lambda_i$ son las raíces del polinomio característico de la EDO:

$$\lambda^2 + 1001\lambda + 1000 = 0$$
$$\lambda = \frac{-1001 \pm \sqrt{1001^2 - 4000}}{2} = \frac{-1001 \pm \sqrt{998001}}{2} \approx \frac{-1001 \pm 999}{2}$$

$$\lambda_1 = -1, \qquad \lambda_2 = -1000$$

*Verificación:* autovalores de $A$: $\det(A-\mu I) = (1-\mu)(1-1001h-\mu)+1000h^2 = 0$, resolviendo $\mu_1 = 1-h$, $\mu_2 = 1-1000h$.

Condiciones de estabilidad $|\mu_i| \leq 1$:
- $|\mu_1| = |1-h| \leq 1 \implies 0 \leq h \leq 2$
- $|\mu_2| = |1-1000h| \leq 1 \implies 0 \leq 1000h \leq 2 \implies h \leq 0.002$

La condición restrictiva es la del autovalor **rápido** ($\lambda_2 = -1000$):

$$\boxed{k_{\max} = \frac{2}{1000} = 0.002}$$

Este es un problema **rígido** (*stiff*): aunque la dinámica de interés puede ser lenta ($\lambda_1=-1$), el autovalor $\lambda_2=-1000$ obliga a usar pasos muy pequeños en Euler explícito.

---

## Problema 9

**Ecuación:** $\dfrac{d^2u}{dt^2} + \dfrac{du}{dt} + u = t$, $\quad u(0)=1$, $\quad u'(0)=1$

Sistema: $u_1 = u$, $u_2 = u'$:
$$\frac{du_1}{dt} = u_2 \equiv f_1, \qquad \frac{du_2}{dt} = t - u_2 - u_1 \equiv f_2$$

### a) Euler Implícito hacia $u(t=2)$

Euler implícito es incondicionalmente estable. Para minimizar el esfuerzo se elige el mayor $h$ posible: $\mathbf{h=2}$ (un solo paso de $t=0$ a $t=2$).

$$u_1^1 = u_1^0 + 2\,u_2^1 \qquad \Rightarrow \qquad u_1^1 - 2\,u_2^1 = 1 \tag{I}$$
$$u_2^1 = u_2^0 + 2\,(t^1 - u_2^1 - u_1^1) = 1 + 2(2 - u_2^1 - u_1^1) \qquad \Rightarrow \qquad 2\,u_1^1 + 3\,u_2^1 = 5 \tag{II}$$

**El sistema es lineal** (la EDO es lineal). En forma matricial:

$$\begin{pmatrix}1 & -2 \\ 2 & 3\end{pmatrix}\begin{pmatrix}u_1^1 \\ u_2^1\end{pmatrix} = \begin{pmatrix}1 \\ 5\end{pmatrix}$$

### b) Resolución por eliminación de Gauss

De (I): $u_1^1 = 1 + 2\,u_2^1$

Sustituyendo en (II):
$$2(1 + 2u_2^1) + 3u_2^1 = 5 \implies 2 + 7u_2^1 = 5 \implies u_2^1 = \frac{3}{7}$$

$$u_1^1 = 1 + \frac{6}{7} = \frac{13}{7}$$

$$\boxed{u(t=2) \approx \frac{13}{7} \approx 1.857, \qquad u'(t=2) \approx \frac{3}{7} \approx 0.429}$$

### c) ¿Podría resolverse por Jacobi?

El método de Jacobi requiere dominancia diagonal estricta:
- Fila 1: $|1| > |-2| \implies 1 > 2$ ❌

**No converge por Jacobi con $h=2$.** Para hacerlo converger, debe elegirse $h < 1$ (condición derivada de la fila 1: $|1| > |h|$). Por ejemplo, con $h=0.5$ (4 pasos de integración):

Sistema por paso:
$$\begin{pmatrix}1 & -0.5 \\ 0.5 & 1.5\end{pmatrix}\begin{pmatrix}u_1 \\ u_2\end{pmatrix} = \ldots$$

Fila 1: $|1| > 0.5$ ✓; Fila 2: $|1.5| > |0.5|$ ✓ → Jacobi converge.

### d) Análisis de errores

| Tipo de error | Etapa donde se introduce |
|---------------|--------------------------|
| **Inherente** | Condiciones iniciales aproximadas o datos del problema con incertidumbre |
| **Truncamiento** | Al discretizar la EDO con Euler (se cortan términos de la serie de Taylor $\mathcal{O}(h^2)$); error global $\mathcal{O}(h)$ |
| **Redondeo** | En cada operación aritmética de punto flotante durante el cálculo numérico |

### e) Estimación por RK2 con mínimo esfuerzo

**Mínimo esfuerzo:** $h=1$ (dos pasos), ya que RK2 con $h=1$ satisface la estabilidad del problema (verificar a continuación).

**Paso 1** ($t^0=0 \to t^1=1$, $u_1^0=1$, $u_2^0=1$):

$$q_1^{u_1} = 1\cdot1 = 1, \quad q_1^{u_2} = 1\cdot(0-1-1) = -2$$

Con $u_1+q_1=2$, $u_2+q_1=-1$, $t^1=1$:
$$q_2^{u_1} = 1\cdot(-1) = -1, \quad q_2^{u_2} = 1\cdot(1-(-1)-2) = 0$$

$$u_1^1 = 1+\tfrac{1}{2}(1+(-1)) = 1, \quad u_2^1 = 1+\tfrac{1}{2}(-2+0) = 0$$

**Paso 2** ($t^1=1 \to t^2=2$, $u_1^1=1$, $u_2^1=0$):

$$q_1^{u_1} = 1\cdot0 = 0, \quad q_1^{u_2} = 1\cdot(1-0-1) = 0$$

Con $u_1+q_1=1$, $u_2+q_1=0$, $t^2=2$:
$$q_2^{u_1} = 1\cdot0 = 0, \quad q_2^{u_2} = 1\cdot(2-0-1) = 1$$

$$u_1^2 = 1+\tfrac{1}{2}(0+0) = 1, \quad u_2^2 = 0+\tfrac{1}{2}(0+1) = 0.5$$

$$\boxed{u(t=2) \approx 1, \quad u'(t=2) \approx 0.5 \quad \text{(RK2)}}$$

**Suposición necesaria:** Para que la estimación sea confiable, el paso $h=1$ debe garantizar estabilidad. Esto puede verificarse analizando los autovalores del Jacobiano (ítem f).

### f) Análisis de estabilidad – Euler Explícito

El Jacobiano del sistema es:
$$J = \begin{pmatrix}0 & 1 \\ -1 & -1\end{pmatrix}$$

Autovalores de $J$: $\lambda^2 + \lambda + 1 = 0 \implies \lambda_{1,2} = \dfrac{-1 \pm i\sqrt{3}}{2}$

Para Euler explícito, los multiplicadores de amplificación son $\mu_i = 1 + h\lambda_i$:

$$|\mu|^2 = \left|1 + h\cdot\frac{-1\pm i\sqrt{3}}{2}\right|^2 = \left(1-\frac{h}{2}\right)^2 + \frac{3h^2}{4} = 1 - h + h^2$$

La ecuación que relaciona $\lambda_i$ con $h$ es:

$$\boxed{|\mu|^2 = 1 - h + h^2 \leq 1}$$

**Condiciones para estabilidad:** se requiere $1 - h + h^2 \leq 1 \implies h^2 - h \leq 0 \implies h(h-1)\leq 0$. Esto se satisface para $\mathbf{0 \leq h \leq 1}$.

En general, los autovalores del sistema $\lambda_i$ deben cumplir que $|1 + h\lambda_i| \leq 1$, es decir, los multiplicadores de amplificación deben caer dentro del **círculo unitario del plano complejo**.

---

## Problema 10

**Modelo SIR:**
$$\frac{dS}{dt} = -\frac{a}{N}SI, \quad \frac{dI}{dt} = \frac{a}{N}SI - bI, \quad \frac{dR}{dt} = bI$$

Con $S(0)=99$, $I(0)=1$, $R(0)=0$.

### a) Discretización por Euler Explícito

$$S^{n+1} = S^n - h\,\frac{a}{N}\,S^n I^n$$
$$I^{n+1} = I^n + h\left(\frac{a}{N}\,S^n I^n - b\,I^n\right)$$
$$R^{n+1} = R^n + h\,b\,I^n$$

### b) Estimación de $I(t=1)$ con $h=1$, $a=0.25$, $b=0.1$, $N=100$

$S^0=99$, $I^0=1$, $R^0=0$:

$$S^1 = 99 - 1\cdot\frac{0.25}{100}\cdot99\cdot1 = 99 - 0.2475 = 98.7525$$

$$I^1 = 1 + 1\cdot\left(\frac{0.25}{100}\cdot99\cdot1 - 0.1\cdot1\right) = 1 + (0.2475 - 0.1) = \mathbf{1.1475}$$

$$R^1 = 0 + 1\cdot0.1\cdot1 = 0.1$$

**Verificación:** $S^1 + I^1 + R^1 = 98.7525 + 1.1475 + 0.1 = 100 = N$ ✓ (se conserva la población).

### c) Discretización por RK2

$$q_1^S = h\,f_S(S^n,I^n) = -\frac{ah}{N}S^n I^n$$
$$q_1^I = h\,f_I(S^n,I^n) = h\left(\frac{a}{N}S^n I^n - bI^n\right)$$
$$q_1^R = h\,f_R(I^n) = hb\,I^n$$

$$q_2^S = -\frac{ah}{N}(S^n+q_1^S)(I^n+q_1^I)$$
$$q_2^I = h\left[\frac{a}{N}(S^n+q_1^S)(I^n+q_1^I) - b(I^n+q_1^I)\right]$$
$$q_2^R = hb\,(I^n+q_1^I)$$

$$S^{n+1} = S^n + \tfrac{1}{2}(q_1^S + q_2^S)$$
$$I^{n+1} = I^n + \tfrac{1}{2}(q_1^I + q_2^I)$$
$$R^{n+1} = R^n + \tfrac{1}{2}(q_1^R + q_2^R)$$

### d) Gráfico e interpretación

```
Comportamiento típico de S, I, R:

Población
  100 |S──────\
      |        \───────────────────
      |         \
      |      I   \───
      |     /^     ───────────────────
      |    / |peak  
      |   /  |
      |  /   |         R ───────────
      | /    |        /
      |/     |       /
    0 +──────────────────────────── t
      0               
```

- **S(t):** decrece monotónicamente (susceptibles → infectados).
- **I(t):** primero crece hasta un pico (cuando $\frac{a}{N}S > b$) y luego decrece (infectados se recuperan más rápido de lo que se generan nuevos).
- **R(t):** crece monotónicamente (recuperados acumulados).

**Modelo real:** El modelo **SIR** describe la propagación de **enfermedades infecciosas** (epidemias) como gripe, sarampión, COVID-19, etc. $a$ es la tasa de contagio, $b$ la tasa de recuperación, y $N$ la población total. El cociente $R_0 = a/b$ es el número básico de reproducción: si $R_0 > 1$ la epidemia se propaga, si $R_0 < 1$ se extingue.
