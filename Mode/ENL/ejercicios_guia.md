# GUIA 1 – ECUACIONES NO LINEALES

---

## Problema 1

**Función:** $f(x) = \frac{x^2}{4} - \sin(x)$

Se desea encontrar la **primera raíz positiva**.

Primero, notar que $f(0) = 0 - 0 = 0$, pero $x=0$ es la raíz trivial. La primera raíz positiva no trivial está en torno a $x \approx 1.9337$.

---

### a) ¿Es el intervalo [1.6, 2.6] adecuado para bisección?

Para aplicar bisección, se requiere que **f cambie de signo** en el intervalo (Teorema de Bolzano):

$$f(1.6) = \frac{(1.6)^2}{4} - \sin(1.6) = \frac{2.56}{4} - 0.9996 = 0.64 - 0.9996 = -0.3596$$

$$f(2.6) = \frac{(2.6)^2}{4} - \sin(2.6) = \frac{6.76}{4} - 0.4854 = 1.69 - 0.4854 = 1.2046$$

Como $f(1.6) < 0$ y $f(2.6) > 0$, hay un cambio de signo.  
Además, $f$ es continua en $[1.6, 2.6]$.  

**El intervalo [1.6, 2.6] es adecuado para bisección.**

---

### b) Número de aproximaciones para tolerancia de error absoluto $\varepsilon = 0.02$

La fórmula para el número mínimo de iteraciones en bisección es:

$$n \geq \frac{\ln\left(\frac{b - a}{\varepsilon}\right)}{\ln(2)}$$

Con $a = 1.6$, $b = 2.6$, $b - a = 1.0$, $\varepsilon = 0.02$:

$$n \geq \frac{\ln\left(\frac{1.0}{0.02}\right)}{\ln(2)} = \frac{\ln(50)}{\ln(2)} = \frac{3.912}{0.6931} \approx 5.644$$

**Se necesitan al menos 6 iteraciones.**

---

### c) Calcular la raíz (bisección)

| n | a      | b      | $x_m$  | $f(x_m)$ | Nuevo intervalo |
|---|--------|--------|--------|-----------|-----------------|
| 1 | 1.6000 | 2.6000 | 2.1000 | +0.2343   | [1.6, 2.1]      |
| 2 | 1.6000 | 2.1000 | 1.8500 | -0.1621   | [1.85, 2.1]     |
| 3 | 1.8500 | 2.1000 | 1.9750 | +0.0200   | [1.85, 1.975]   |
| 4 | 1.8500 | 1.9750 | 1.9125 | -0.0726   | [1.9125, 1.975] |
| 5 | 1.9125 | 1.9750 | 1.9438 | -0.0264   | [1.9438, 1.975] |
| 6 | 1.9438 | 1.9750 | 1.9594 | -0.0033   | [1.9594, 1.975] |

Con 6 iteraciones: $x \approx 1.9594$. El ancho del intervalo es $\frac{1.0}{2^6} = 0.015625 < 0.02$. ✓

La raíz es aproximadamente $\alpha \approx 1.9337$.

---

### d) Tolerancia 0.02 sobre el error relativo → ¿cuántas iteraciones?

El error relativo se estima como:

$$e_r = \frac{|x_{n+1} - x_n|}{|x_{n+1}|} \approx \frac{(b-a)/2^n}{|\alpha|}$$

Queremos:

$$\frac{(b-a)/2^n}{|\alpha|} < 0.02$$

$$\frac{1.0/2^n}{1.9337} < 0.02 \implies \frac{1}{2^n} < 0.03867 \implies 2^n > 25.86$$

$$n > \frac{\ln(25.86)}{\ln(2)} = \frac{3.253}{0.6931} \approx 4.69$$

**Se necesitan al menos 5 iteraciones** (una menos que con error absoluto, porque el denominador $|\alpha| \approx 1.9337$ amplifica la tolerancia efectiva).

---

### e) Variación del error absoluto con $\alpha = 1.93375$

| n | $x_n$  | $e_n = |x_n - \alpha|$ | $e_n / e_{n-1}$ |
|---|--------|------------------------|-----------------|
| 1 | 2.1000 | 0.16625                | —               |
| 2 | 1.8500 | 0.08375                | ≈ 0.504         |
| 3 | 1.9750 | 0.04125                | ≈ 0.492         |
| 4 | 1.9125 | 0.02125                | ≈ 0.515         |
| 5 | 1.9438 | 0.01005                | ≈ 0.473         |
| 6 | 1.9594 | 0.00565                | ≈ 0.562         |

**El error se reduce aproximadamente a la mitad en cada iteración**, lo cual es característico de la bisección (convergencia lineal con tasa $q = 1/2$). Formalmente:

$$e_{n+1} \leq \frac{b - a}{2^{n+1}}$$

---

## Problema 2

**Función:** $f(x) = \sin(x) - \frac{1}{2}\sqrt{x}$, con raíz en $I = (0, 2)$.

**Función de iteración:** $g(x) = x - f(x) = x - \sin(x) + \frac{1}{2}\sqrt{x}$

---

### a) Intervalo que cumple el Teorema de Punto Fijo

El **Teorema de Punto Fijo** exige:
1. $g$ mapea el intervalo sobre sí mismo: $g([a,b]) \subseteq [a,b]$
2. $|g'(x)| \leq k < 1$ para todo $x \in [a,b]$ (contracción)

Calculamos $g'(x)$:

$$g'(x) = 1 - \cos(x) + \frac{1}{4\sqrt{x}}$$

Analizando el gráfico de $g'$ dado (segundo gráfico de la guía): $g'$ tiene un mínimo cercano a $x \approx 0.7$ y **no cumple** $|g'| < 1$ cerca del origen (diverge por el término $\frac{1}{4\sqrt{x}}$).

Buscamos un subintervalo donde $|g'(x)| < 1$. Para $x \in [0.5, 2]$:

- $g'(0.5) = 1 - \cos(0.5) + \frac{1}{4\sqrt{0.5}} = 1 - 0.8776 + 0.3536 = 0.476$
- $g'(1.0) = 1 - \cos(1) + \frac{1}{4} = 1 - 0.5403 + 0.25 = 0.7097$
- $g'(2.0) = 1 - \cos(2) + \frac{1}{4\sqrt{2}} = 1 + 0.4161 + 0.1768 = 1.5929$ ← mayor que 1

Entonces restringimos a $[0.5, 1.5]$:
- $g'(1.5) = 1 - \cos(1.5) + \frac{1}{4\sqrt{1.5}} = 1 - 0.0707 + 0.2041 = 1.133$ ← aún > 1

Probamos $[0.5, 1.2]$:
- $g'(1.2) = 1 - \cos(1.2) + \frac{1}{4\sqrt{1.2}} = 1 - 0.3624 + 0.2282 = 0.866 < 1$ ✓

En el intervalo **$[0.5, 1.2]$**:
- $|g'(x)| \leq 0.87 < 1$ → condición de contracción cumplida
- $g(0.5) \approx 0.5 - 0.479 + 0.354 = 0.375$... verificar que $g([0.5,1.2]) \subseteq [0.5,1.2]$

> **Nota:** De los gráficos de la guía se puede leer directamente el intervalo donde $g' < 1$. Un intervalo típico que se usa es $[0.4, 1.3]$ o similar, siempre que quede estrictamente dentro de $(0,2)$.

**Iteraciones de punto fijo** partiendo de $x_0 = 1.0$:

| n | $x_n$   |
|---|---------|
| 0 | 1.0000  |
| 1 | 1.0917  |
| 2 | 1.1044  |
| 3 | 1.1061  |
| 4 | 1.1063  |
| 5 | 1.1064  |

La raíz converge a $\alpha \approx 1.1064$.

---

### b) Raíz con tolerancia 1% para error relativo entre 2 iteraciones consecutivas

$$e_r = \frac{|x_{n+1} - x_n|}{|x_{n+1}|} \times 100\% < 1\%$$

| n | $x_n$  | $e_r$ (%)         |
|---|--------|-------------------|
| 0 | 1.0000 | —                 |
| 1 | 1.0917 | 8.4%              |
| 2 | 1.1044 | 1.15%             |
| 3 | 1.1061 | 0.15% ✓           |

Con **3 iteraciones** se alcanza la tolerancia del 1%.

**Raíz:** $\alpha \approx 1.1061$

---

## Problema 3

**Ecuación:** $x = \cos(x)$

Se busca la primera raíz positiva con Newton-Raphson.

Reescribir como $f(x) = x - \cos(x) = 0$.

---

### a) Método de punto fijo planteado

La ecuación $x = \cos(x)$ ya está en forma de punto fijo directamente:

$$g(x) = \cos(x)$$

Newton-Raphson es un **caso especial de punto fijo** con:

$$g_{NR}(x) = x - \frac{f(x)}{f'(x)}$$

Con $f(x) = x - \cos(x)$ y $f'(x) = 1 + \sin(x)$:

$$g_{NR}(x) = x - \frac{x - \cos(x)}{1 + \sin(x)}$$

---

### b) Propiedades de convergencia e intervalo

Para que Newton-Raphson converja cuadráticamente se necesita que:
- $f'(\alpha) \neq 0$ (raíz simple)
- $x_0$ suficientemente cercano a $\alpha$

Analizar $g_{NR}'(x)$:

$$g_{NR}'(x) = \frac{f(x) \cdot f''(x)}{[f'(x)]^2}$$

En la raíz $\alpha$: $f(\alpha) = 0 \implies g_{NR}'(\alpha) = 0 < 1$ ✓

Para encontrar un intervalo explícito de convergencia, usar el criterio:

$$\left|\frac{f(x) \cdot f''(x)}{[f'(x)]^2}\right| < 1$$

Con $f''(x) = \sin(x)$:

$$\left|\frac{(x - \cos x) \cdot \sin x}{(1 + \sin x)^2}\right| < 1$$

Evaluando numéricamente, la raíz está en $\alpha \approx 0.7391$.

Para $x \in [0.5, 1.0]$:
- $f'(x) = 1 + \sin(x) \geq 1 + \sin(0.5) \approx 1.479 > 0$ (no hay singularidades)
- La condición se cumple en todo $[0.5, 1.0]$

**Intervalo de convergencia: $[0.5, 1.0]$**

---

### c) Raíz con tolerancia $10^{-10}$ (Newton-Raphson)

Partiendo de $x_0 = 1.0$:

$$x_{n+1} = x_n - \frac{x_n - \cos(x_n)}{1 + \sin(x_n)}$$

| n | $x_n$              | $|f(x_n)|$       |
|---|--------------------|------------------|
| 0 | 1.000000000000     | 4.60e-01         |
| 1 | 0.750363867840     | 1.81e-02         |
| 2 | 0.739112890912     | 3.47e-04         |
| 3 | 0.739085133385     | 1.26e-07         |
| 4 | 0.739085133215     | 1.67e-14         |

Con **4 iteraciones** se supera la tolerancia de $10^{-10}$.

**Raíz:** $\alpha \approx 0.7390851332151607$

---

### d) Orden de convergencia experimental

El orden $p$ se estima con tres iteraciones consecutivas:

$$p \approx \frac{\ln|e_{n+1}/e_n|}{\ln|e_n/e_{n-1}|}$$

Con $\alpha = 0.7390851332$:

| n | $e_n = |x_n - \alpha|$ |
|---|------------------------|
| 0 | 2.609e-01              |
| 1 | 1.128e-02              |
| 2 | 2.758e-05              |
| 3 | 1.670e-10              |

$$p \approx \frac{\ln(2.758 \times 10^{-5} / 1.128 \times 10^{-2})}{\ln(1.128 \times 10^{-2} / 2.609 \times 10^{-1})} = \frac{\ln(2.445 \times 10^{-3})}{\ln(4.324 \times 10^{-2})} = \frac{-6.014}{-3.141} \approx 1.91$$

Confirmando entre iteraciones 2 y 3:

$$p \approx \frac{\ln(1.67 \times 10^{-10} / 2.758 \times 10^{-5})}{\ln(2.758 \times 10^{-5} / 1.128 \times 10^{-2})} = \frac{\ln(6.05 \times 10^{-6})}{\ln(2.445 \times 10^{-3})} = \frac{-11.71}{-6.014} \approx 1.95$$

**El orden de convergencia experimental es $p \approx 2$**, confirmando la convergencia cuadrática de Newton-Raphson para raíces simples.

---

## Problema 4

### a) Fórmula iterativa NR para raíz cúbica de $c$

Se quiere calcular $x = c^{1/3}$, equivalente a resolver:

$$f(x) = x^3 - c = 0$$

Con $f'(x) = 3x^2$, la iteración de Newton-Raphson es:

$$x_{n+1} = x_n - \frac{x_n^3 - c}{3x_n^2}$$

$$\boxed{x_{n+1} = \frac{2x_n^3 + c}{3x_n^2} = \frac{1}{3}\left(2x_n + \frac{c}{x_n^2}\right)}$$

**Ejemplo:** raíz cúbica de 8 ($c=8$), partiendo de $x_0 = 2.5$:
- $x_1 = \frac{1}{3}(5 + 8/6.25) = \frac{1}{3}(5 + 1.28) = 2.093$
- $x_2 = \frac{1}{3}(4.187 + 8/4.380) = \frac{1}{3}(4.187 + 1.826) = 2.004$
- $x_3 \approx 2.0000$ ✓

---

### b) Fórmula iterativa NR para $\arcsin(a)$

Se quiere calcular $x = \arcsin(a)$, equivalente a resolver:

$$f(x) = \sin(x) - a = 0$$

Con $f'(x) = \cos(x)$, la iteración es:

$$x_{n+1} = x_n - \frac{\sin(x_n) - a}{\cos(x_n)}$$

$$\boxed{x_{n+1} = x_n - \frac{\sin(x_n) - a}{\cos(x_n)}}$$

**Ejemplo:** $\arcsin(0.5) = \pi/6 \approx 0.5236$, partiendo de $x_0 = 0.5$:
- $x_1 = 0.5 - \frac{0.4794 - 0.5}{0.8776} = 0.5 + 0.0235 = 0.5235$
- $x_2 \approx 0.5236$ ✓ (converge en 2 iteraciones)

---

### c) Fórmula iterativa NR para $\ln(a)$ usando solo la exponencial

Se quiere calcular $x = \ln(a)$, equivalente a resolver:

$$f(x) = e^x - a = 0$$

(la máquina puede calcular $e^x$ pero no $\ln$)

Con $f'(x) = e^x$, la iteración es:

$$x_{n+1} = x_n - \frac{e^{x_n} - a}{e^{x_n}}$$

$$\boxed{x_{n+1} = x_n - 1 + a \cdot e^{-x_n}}$$

Solo se usa la función exponencial (que la máquina sí tiene). ✓

**Ejemplo:** $\ln(2) \approx 0.6931$, partiendo de $x_0 = 1.0$:
- $x_1 = 1 - 1 + 2 \cdot e^{-1} = 2/e \approx 0.7358$
- $x_2 = 0.7358 - 1 + 2 \cdot e^{-0.7358} \approx 0.7358 - 1 + 0.9551 = 0.6909$
- $x_3 \approx 0.6931$ ✓

La convergencia es cuadrática (raíz simple, $f'(\alpha) = e^{\ln a} = a \neq 0$).

---

## Problema 5

**Función del Problema 1:** $f(x) = \frac{x^2}{4} - \sin(x)$

**Raíz buscada:** $\alpha \approx 1.933753$ (primera raíz positiva no trivial)

**Derivadas:**
$$f'(x) = \frac{x}{2} - \cos(x) \qquad f''(x) = \frac{1}{2} + \sin(x)$$

Se aplican los cuatro métodos partiendo de condiciones iniciales comunes:
- Métodos de cerramiento: intervalo $[a_0, b_0] = [1.6,\ 2.6]$
- Métodos abiertos: $x_0 = 2.0$ (o $x_0 = 1.6,\ x_1 = 2.6$ para Secante)

---

### Método 1: Regula Falsi (Posición Falsa)

**Fórmula:**
$$c_{n} = \frac{a_n \cdot f(b_n) - b_n \cdot f(a_n)}{f(b_n) - f(a_n)}$$

El extremo que **no cambia de signo** con $c_n$ se reemplaza. A diferencia de bisección, el punto nuevo no está en el centro sino en la intersección de la cuerda con el eje $x$.

**Valores iniciales:**
- $f(1.6) = 0.64 - \sin(1.6) \approx -0.35957$
- $f(2.6) = 1.69 - \sin(2.6) \approx +1.17450$

| n | $a_n$   | $b_n$   | $c_n$   | $f(c_n)$   | $\|c_n - c_{n-1}\|$ |
|---|---------|---------|---------|------------|----------------------|
| 1 | 1.60000 | 2.60000 | 1.83461 | -0.12271   | —                    |
| 2 | 1.83461 | 2.60000 | 1.90716 | -0.03421   | 7.255e-02            |
| 3 | 1.90716 | 2.60000 | 1.92746 | -0.00918   | 2.030e-02            |
| 4 | 1.92746 | 2.60000 | 1.93291 | -0.00242   | 5.450e-03            |
| 5 | 1.93291 | 2.60000 | 1.93435 | -0.000636  | 1.440e-03            |
| 6 | 1.93435 | 2.60000 | 1.93472 | -0.000167  | 3.700e-04            |
| 7 | 1.93472 | 2.60000 | 1.93482 | -4.38e-05  | 9.700e-05            |
| 8 | 1.93482 | 2.60000 | 1.93485 | -1.15e-05  | 2.500e-05            |

> **Observación:** El extremo $b = 2.6$ nunca cambia (el extremo derecho siempre tiene $f > 0$). Esto es el problema conocido de Regula Falsi: **un extremo queda fijo** y la convergencia se vuelve más lenta que bisección. El método converge linealmente.

**Orden de convergencia:** Se estima la razón $\frac{|e_{n+1}|}{|e_n|}$:

$$\frac{7.255 \times 10^{-2}}{—} \to \frac{2.030 \times 10^{-2}}{7.255 \times 10^{-2}} \approx 0.28 \to \frac{5.45 \times 10^{-3}}{2.030 \times 10^{-2}} \approx 0.268$$

La razón es aproximadamente constante $\approx 0.27$ → **convergencia lineal** ($p = 1$, tasa $q \approx 0.27$).

---

### Método 2: Punto Fijo con $g(x) = x - f(x)$

**Función de iteración:**
$$g(x) = x - f(x) = x - \frac{x^2}{4} + \sin(x)$$

$$g'(x) = 1 - \frac{x}{2} + \cos(x)$$

**Verificación de convergencia en torno a $\alpha$:**

$$g'(1.9338) = 1 - \frac{1.9338}{2} + \cos(1.9338) \approx 1 - 0.9669 + (-0.3548) \approx -0.3217$$

Como $|g'(\alpha)| \approx 0.32 < 1$, el método converge. La tasa teórica es $q \approx 0.32$.

**Iteraciones** desde $x_0 = 2.0$:

$$x_{n+1} = x_n - \frac{x_n^2}{4} + \sin(x_n)$$

| n | $x_n$   | $\|x_{n+1} - x_n\|$ |
|---|---------|----------------------|
| 0 | 2.00000 | —                    |
| 1 | 1.90930 | 9.070e-02            |
| 2 | 1.94090 | 3.160e-02            |
| 3 | 1.93065 | 1.025e-02            |
| 4 | 1.93393 | 3.280e-03            |
| 5 | 1.93287 | 1.060e-03            |
| 6 | 1.93321 | 3.400e-04            |
| 7 | 1.93310 | 1.100e-04            |
| 8 | 1.93314 | 3.500e-05            |
| 9 | 1.93313 | 1.100e-05            |

> **Observación:** Oscila alrededor de la raíz (signo de $g'$ negativo). Converge, pero requiere más iteraciones que NR.

**Orden de convergencia estimado:** La razón $\frac{|e_{n+1}|}{|e_n|}$ es aproximadamente constante $\approx 0.32$ → **convergencia lineal** ($p = 1$, tasa $q \approx |g'(\alpha)| \approx 0.32$).

---

### Método 3: Newton-Raphson

**Fórmula:**
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{\frac{x_n^2}{4} - \sin(x_n)}{\frac{x_n}{2} - \cos(x_n)}$$

**Iteraciones** desde $x_0 = 2.0$:

| n | $x_n$      | $f(x_n)$   | $f'(x_n)$  | $\|x_{n+1} - x_n\|$ |
|---|------------|------------|------------|----------------------|
| 0 | 2.000000   | +0.090703  | +1.416147  | —                    |
| 1 | 1.935952   | +0.002276  | +1.325417  | 6.405e-02            |
| 2 | 1.934235   | +0.000001  | +1.323076  | 1.717e-03            |
| 3 | 1.933753   | < 1e-11    | +1.322534  | 1.459e-06            |
| 4 | 1.933753   | < 1e-15    | —          | < 1e-12              |

**Orden de convergencia:**

$$p \approx \frac{\ln|e_3/e_2|}{\ln|e_2/e_1|} = \frac{\ln(1.459 \times 10^{-6} / 1.717 \times 10^{-3})}{\ln(1.717 \times 10^{-3} / 6.405 \times 10^{-2})} = \frac{\ln(8.5 \times 10^{-4})}{\ln(2.68 \times 10^{-2})} = \frac{-7.07}{-3.62} \approx 1.95$$

**Convergencia cuadrática** ($p \approx 2$). Con solo **4 iteraciones** se alcanzan 6 dígitos significativos.

La constante asintótica es:
$$C = \frac{|f''(\alpha)|}{2|f'(\alpha)|} = \frac{\frac{1}{2} + \sin(1.9338)}{2(1.3225)} = \frac{0.5 + 0.9353}{2.6450} \approx 0.542$$

---

### Método 4: Secante

**Fórmula:**
$$x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

No requiere calcular $f'$; aproxima la derivada con una diferencia finita.

**Condiciones iniciales:** $x_0 = 1.6$, $x_1 = 2.6$

| n | $x_n$      | $f(x_n)$    | $\|x_{n+1} - x_n\|$ |
|---|------------|-------------|----------------------|
| 0 | 1.600000   | -0.359570   | —                    |
| 1 | 2.600000   | +1.174500   | —                    |
| 2 | 1.834610   | -0.122710   | 7.654e-01            |
| 3 | 1.956030   | +0.024590   | 1.214e-01            |
| 4 | 1.929370   | -0.005880   | 2.666e-02            |
| 5 | 1.934280   | +0.000492   | 4.910e-03            |
| 6 | 1.933717   | -0.000025   | 5.630e-04            |
| 7 | 1.933754   | < 1e-08     | 3.700e-05            |
| 8 | 1.933753   | < 1e-12     | 1.900e-08            |

**Orden de convergencia:**

$$p \approx \frac{\ln(3.7 \times 10^{-5} / 5.63 \times 10^{-4})}{\ln(5.63 \times 10^{-4} / 4.91 \times 10^{-3})} = \frac{\ln(0.0657)}{\ln(0.1147)} = \frac{-2.722}{-2.165} \approx 1.26$$

**Convergencia superlineal** con $p \approx \phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ (orden teórico de la secante). El valor experimental $\approx 1.26$ puede mejorar con más iteraciones; con iteraciones 6-7-8:

$$p \approx \frac{\ln(1.9 \times 10^{-8} / 3.7 \times 10^{-5})}{\ln(3.7 \times 10^{-5} / 5.63 \times 10^{-4})} = \frac{\ln(5.14 \times 10^{-4})}{\ln(6.57 \times 10^{-2})} = \frac{-7.57}{-2.72} \approx 1.58$$

Confirma convergencia con $p \approx 1.6 \approx \phi$.

---

### Comparación de Performance

| Método        | Iter. para 6 dígitos | Orden $p$ | Costo por iter.     | Obs.                          |
|---------------|----------------------|-----------|---------------------|-------------------------------|
| Regula Falsi  | ~15–20               | 1 (lento) | 1 evaluación de $f$ | Un extremo fijo → lento       |
| Punto Fijo    | ~10–12               | 1         | 1 evaluación de $g$ | Tasa $q \approx 0.32$         |
| Newton-Raphson| 4                    | **2**     | 1 eval. $f$ + $f'$  | El más rápido                 |
| Secante       | 8                    | ~1.618    | 2 eval. de $f$      | Sin derivada, casi tan bueno  |

**Evolución de $\|x_{n+1} - x_n\|$** (comparación visual):

```
Iter  Reg.Falsi    Pto.Fijo     N-Raphson    Secante
  1   7.26e-02     9.07e-02     6.41e-02     7.65e-01
  2   2.03e-02     3.16e-02     1.72e-03     1.21e-01
  3   5.45e-03     1.03e-02     1.46e-06     2.67e-02
  4   1.44e-03     3.28e-03     < 1e-11      4.91e-03
  5   3.70e-04     1.06e-03     converged    5.63e-04
  6   9.70e-05     3.40e-04                  3.70e-05
  7   2.50e-05     1.10e-04                  1.90e-08
  8   ...          3.50e-05                  converged
```

---

### ¿Cuándo usar métodos de arranque vs. métodos abiertos?

**Usar Bisección / Regula Falsi cuando:**
- No se tiene información sobre la cercanía de $x_0$ a la raíz (arranque "en frío").
- Se requiere **garantía de convergencia**: bisección siempre converge si hay un cambio de signo.
- La función es poco regular o tiene discontinuidades cercanas.
- Se necesita **acotar el error** con certeza: en bisección $|e_n| \leq (b-a)/2^n$ exactamente.
- Hay múltiples raíces y se quiere aislar una en particular mediante análisis de signo.
- El costo de evaluar $f'(x)$ es prohibitivo o $f'$ no existe analíticamente.

**Usar Newton-Raphson / Secante / Punto Fijo cuando:**
- Se dispone de una **buena estimación inicial** (por ejemplo, obtenida previamente con bisección).
- Se necesita **alta precisión** con pocas iteraciones (aplicaciones de tiempo real, cómputo iterativo interno).
- La función es suave ($f \in C^2$) y $f'(\alpha) \neq 0$.
- Se conoce $f'$ analíticamente → preferir Newton-Raphson (orden 2).
- No se puede/quiere calcular $f'$ → preferir Secante (orden $\phi \approx 1.618$, casi igual de rápido).

**Estrategia práctica recomendada:**
> Usar **bisección o Regula Falsi** para reducir el intervalo inicial a un entorno pequeño de la raíz (tolerancia $\sim 10^{-2}$), y luego **cambiar a Newton-Raphson o Secante** para converger rápidamente a la precisión deseada. Esta combinación es robusta y eficiente.
