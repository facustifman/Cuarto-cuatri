# GUIA 3 - ERRORES — CB051 Modelación Numérica

---

## Problema 1

Dado: $a = 1{,}58976413794$ y $\Delta a = 0{,}5 \times 10^{-5}$

La cota de error absoluto es $\Delta a = 5 \times 10^{-6}$, lo que significa que el error afecta al sexto decimal.

Se redondea $a$ al sexto decimal:

$$a = 1{,}589764 \pm 0{,}000005$$

**Dígitos significativos:** los dígitos conocidos con certeza más el primero incierto.
El primer dígito afectado por el error es el 6º decimal (posición $10^{-6}$). La parte entera tiene 1 dígito y los decimales seguros son 5, por lo que hay **7 dígitos significativos**.

$$\boxed{a = 1{,}58976 \pm 0{,}5 \times 10^{-5} \quad \Rightarrow \quad 7 \text{ cifras significativas}}$$

---

## Problema 2

Dado: círculo de diámetro medido $D_m$ con error absoluto $\Delta D$.

El área en función del diámetro es:

$$A = \frac{\pi D^2}{4}$$

### a) Error absoluto directo (no lineal)

Se evalúa el área en los extremos del intervalo:

$$A_{max} = \frac{\pi (D_m + \Delta D)^2}{4}, \qquad A_{min} = \frac{\pi (D_m - \Delta D)^2}{4}$$

$$\Delta A^+ = A_{max} - A(D_m) = \frac{\pi}{4}\left[(D_m+\Delta D)^2 - D_m^2\right] = \frac{\pi}{4}(2D_m\,\Delta D + \Delta D^2)$$

$$\Delta A^- = A(D_m) - A_{min} = \frac{\pi}{4}(2D_m\,\Delta D - \Delta D^2)$$

Como $\Delta A^+ \neq \Delta A^-$, el intervalo **no es simétrico**.

$$A = \frac{\pi D_m^2}{4}, \qquad A \in \left[\frac{\pi(D_m-\Delta D)^2}{4},\ \frac{\pi(D_m+\Delta D)^2}{4}\right]$$

### b) Teoría lineal de errores

Se aplica propagación lineal (primer orden):

$$\Delta A = \left|\frac{\partial A}{\partial D}\right| \Delta D = \frac{\pi D_m}{2}\,\Delta D$$

El intervalo resultante es **simétrico**: $A = \frac{\pi D_m^2}{4} \pm \frac{\pi D_m}{2}\Delta D$

**Comparación:**

- Inciso a): intervalo asimétrico, más exacto pero más complejo de calcular.
- Inciso b): intervalo simétrico, más simple, válido cuando $\Delta D \ll D_m$ (error relativo pequeño).

La diferencia entre ambos es el término de segundo orden $\frac{\pi}{4}\Delta D^2$, despreciable en la aproximación lineal.

### c) Error adicional por aproximar $\pi \approx 3{,}14$

El error en $\pi$ es $\Delta\pi = |\pi - 3{,}14| \approx 0{,}00159$.

Usando propagación lineal sobre $A = \frac{\pi D^2}{4}$:

$$\Delta A_{total} = \left|\frac{\partial A}{\partial D}\right|\Delta D + \left|\frac{\partial A}{\partial \pi}\right|\Delta\pi = \frac{\pi D_m}{2}\Delta D + \frac{D_m^2}{4}\Delta\pi$$

$$\Delta A_{total} = \frac{\pi D_m}{2}\Delta D + \frac{D_m^2}{4}(0{,}00159)$$

---

## Problema 3

### a) Suma/resta: los errores absolutos se suman

Sea $w = x \pm y$, con $x = \bar{x} \pm \Delta x$ y $y = \bar{y} \pm \Delta y$.

El valor máximo posible de $w$ es $(\bar{x}+\Delta x) \pm (\bar{y}+\Delta y)$, y el mínimo $(\bar{x}-\Delta x) \pm (\bar{y}-\Delta y)$.

Por lo tanto, la cota del error absoluto de $w$ es:

$$\Delta w = \Delta x + \Delta y$$

Los errores absolutos se suman independientemente del signo de la operación. $\blacksquare$

### b) Producto/cociente: los errores relativos se suman

**Producto:** $w = x \cdot y$

Aplicando la teoría lineal:

$$\Delta w = \left|\frac{\partial w}{\partial x}\right|\Delta x + \left|\frac{\partial w}{\partial y}\right|\Delta y = |y|\,\Delta x + |x|\,\Delta y$$

Dividiendo por $|w| = |x||y|$:

$$\frac{\Delta w}{|w|} = \frac{\Delta x}{|x|} + \frac{\Delta y}{|y|} \qquad \Rightarrow \qquad \varepsilon_w = \varepsilon_x + \varepsilon_y \qquad \blacksquare$$

**Cociente:** $w = x/y$

$$\Delta w = \left|\frac{1}{y}\right|\Delta x + \left|\frac{x}{y^2}\right|\Delta y$$

Dividiendo por $|w| = |x|/|y|$:

$$\frac{\Delta w}{|w|} = \frac{\Delta x}{|x|} + \frac{\Delta y}{|y|} \qquad \Rightarrow \qquad \varepsilon_w = \varepsilon_x + \varepsilon_y \qquad \blacksquare$$

---

## Problema 4

$x = 2{,}00$, $y = 3{,}00$, $z = 4{,}00$ (valores redondeados correctamente).

Los errores absolutos de valores redondeados a centésimas son $\Delta x = \Delta y = \Delta z = 0{,}005$.

### a) $w = 3x + y - z$

**Valor central:**
$$w = 3(2{,}00) + 3{,}00 - 4{,}00 = 6{,}00 + 3{,}00 - 4{,}00 = 5{,}00$$

**Error absoluto (teoría lineal):**
$$\Delta w = \left|\frac{\partial w}{\partial x}\right|\Delta x + \left|\frac{\partial w}{\partial y}\right|\Delta y + \left|\frac{\partial w}{\partial z}\right|\Delta z = 3(0{,}005) + 1(0{,}005) + 1(0{,}005) = 0{,}025$$

$$\boxed{w = 5{,}00 \pm 0{,}025}$$

### b) $w = x \cdot \sin(y/40)$

**Valor central:**

El argumento del seno: $y/40 = 3{,}00/40 = 0{,}075$ rad

$$w = 2{,}00 \cdot \sin(0{,}075) = 2{,}00 \times 0{,}074952 \approx 0{,}14990$$

**Error absoluto (teoría lineal):**

$$\frac{\partial w}{\partial x} = \sin\!\left(\frac{y}{40}\right), \qquad \frac{\partial w}{\partial y} = \frac{x}{40}\cos\!\left(\frac{y}{40}\right)$$

$$\Delta w = \left|\sin(0{,}075)\right|(0{,}005) + \left|\frac{2{,}00}{40}\cos(0{,}075)\right|(0{,}005)$$

$$\Delta w = 0{,}074952 \times 0{,}005 + 0{,}05 \times 0{,}997187 \times 0{,}005$$

$$\Delta w = 0{,}000375 + 0{,}000249 = 0{,}000624 \approx 6{,}2 \times 10^{-4}$$

$$\boxed{w = 0{,}1499 \pm 6{,}2 \times 10^{-4}}$$

---

## Problema 5

$$w = \frac{x\,y^2}{z}, \qquad x = 2{,}0 \pm 0{,}1, \quad y = 3{,}0 \pm 0{,}2, \quad z = 1{,}0 \pm 0{,}1$$

**Valor central:**
$$w = \frac{2{,}0 \times (3{,}0)^2}{1{,}0} = \frac{18{,}0}{1{,}0} = 18{,}0$$

**Error absoluto (teoría lineal):**

$$\frac{\partial w}{\partial x} = \frac{y^2}{z} = \frac{9{,}0}{1{,}0} = 9{,}0$$

$$\frac{\partial w}{\partial y} = \frac{2xy}{z} = \frac{2 \times 2{,}0 \times 3{,}0}{1{,}0} = 12{,}0$$

$$\frac{\partial w}{\partial z} = -\frac{xy^2}{z^2} = -\frac{18{,}0}{1{,}0} = -18{,}0$$

$$\Delta w = 9{,}0 \times 0{,}1 + 12{,}0 \times 0{,}2 + 18{,}0 \times 0{,}1 = 0{,}9 + 2{,}4 + 1{,}8 = 5{,}1$$

$$\boxed{w = 18{,}0 \pm 5{,}1}$$

**Incidencia de cada variable en $\Delta w$:**

| Variable | Contribución | Porcentaje |
| --- | --- | --- |
| $x$ | $0{,}9$ | $17{,}6\%$ |
| $y$ | $2{,}4$ | $47{,}1\%$ |
| $z$ | $1{,}8$ | $35{,}3\%$ |

**La variable $y$ tiene mayor incidencia** en el error absoluto de $w$ (47%), tanto por su coeficiente $2$ en el exponente como por tener el mayor error relativo ($\varepsilon_y = 0{,}2/3{,}0 \approx 6{,}7\%$).

---

## Problema 6

La tensión de rotura a compresión:

$$f = \frac{4F}{\pi D^2}$$

Datos:

- $F = 0{,}715\,\text{MN}$, $\Delta F = 0{,}003\,\text{MN}$
- $D = 0{,}15\,\text{m}$, error relativo porcentual $= 2{,}5\%$ $\Rightarrow$ $\Delta D = 0{,}025 \times 0{,}15 = 0{,}00375\,\text{m}$
- $\pi = 3{,}1416 \pm 0{,}00005$

### a) Tensión de rotura con su error absoluto

**Valor central:**

$$f = \frac{4 \times 0{,}715}{\pi \times (0{,}15)^2} = \frac{2{,}860}{3{,}1416 \times 0{,}0225} = \frac{2{,}860}{0{,}070686} \approx 40{,}46\,\text{MN/m}^2$$

**Error absoluto (teoría lineal):**

$$\frac{\partial f}{\partial F} = \frac{4}{\pi D^2} = \frac{f}{F}$$

$$\frac{\partial f}{\partial D} = -\frac{8F}{\pi D^3} = -\frac{2f}{D}$$

$$\frac{\partial f}{\partial \pi} = -\frac{4F}{\pi^2 D^2} = -\frac{f}{\pi}$$

$$\Delta f = \left|\frac{\partial f}{\partial F}\right|\Delta F + \left|\frac{\partial f}{\partial D}\right|\Delta D + \left|\frac{\partial f}{\partial \pi}\right|\Delta\pi$$

$$\Delta f = \frac{f}{F}\,\Delta F + \frac{2f}{D}\,\Delta D + \frac{f}{\pi}\,\Delta\pi$$

$$\Delta f = f\left(\frac{\Delta F}{F} + \frac{2\,\Delta D}{D} + \frac{\Delta\pi}{\pi}\right)$$

$$\frac{\Delta F}{F} = \frac{0{,}003}{0{,}715} \approx 0{,}00420$$

$$\frac{2\,\Delta D}{D} = \frac{2 \times 0{,}00375}{0{,}15} = 0{,}050$$

$$\frac{\Delta\pi}{\pi} = \frac{0{,}00005}{3{,}1416} \approx 0{,}0000159$$

$$\Delta f = 40{,}46 \times (0{,}00420 + 0{,}050 + 0{,}0000159) \approx 40{,}46 \times 0{,}05422 \approx 2{,}19\,\text{MN/m}^2$$

$$\boxed{f = (40{,}5 \pm 2{,}2)\,\text{MN/m}^2}$$

### b) Error relativo porcentual de $f$

$$\varepsilon_f = \frac{\Delta f}{f} = \frac{\Delta F}{F} + \frac{2\,\Delta D}{D} + \frac{\Delta\pi}{\pi}$$

$$\varepsilon_f = 0{,}420\% + 5{,}000\% + 0{,}002\% \approx 5{,}42\%$$

$$\boxed{\varepsilon_f \approx 5{,}4\%}$$

La mayor contribución al error relativo proviene del diámetro $D$, que aporta el $5\%$ (el doble de su error relativo del $2{,}5\%$ por estar elevado al cuadrado).
