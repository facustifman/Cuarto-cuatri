# PLAN DE ESTUDIO — PARCIAL TALLER DE PROGRAMACIÓN
### Examen: Martes 8 de Julio de 2026

> Hoy: Martes 1 de Julio. Tiempo disponible: **7 días**.
> Estrategia: foco en lo que más sale. El final de Taller siempre tiene 4 secciones:
> 1. Archivo en C | 2. Sockets | 3. Clase con operadores | 4. Pregunta teórica

---

## PRIORIDADES (de mayor a menor impacto en el examen)

| # | Tema | Peso en el final | Dificultad |
|---|---|---|---|
| 1 | Archivos en C (binarios, big-endian, bases) | ★★★★★ | Alta |
| 2 | Sockets (servidor/cliente con recv/send) | ★★★★★ | Media |
| 3 | Clases C++ (operadores, move, copia) | ★★★★★ | Media |
| 4 | Preguntas teóricas (mutex, RAII, virtual...) | ★★★★☆ | Baja |
| 5 | Templates (clases genéricas, PILA, LISTA) | ★★★☆☆ | Media |
| 6 | Threads y condition variables | ★★★☆☆ | Alta |

---

## DÍA A DÍA

### MARTES 1 JULIO (HOY, 2–3 hs)
**Tema: Orientación y conceptos teóricos fáciles**

- [ ] Leer el SUPER_RESUMEN_TALLER.md completo (una lectura rápida, 45 min)
- [ ] Memorizar las respuestas teóricas cortas:
  - ¿Qué es RAII? ¿Qué es un mutex? ¿Qué es un functor?
  - ¿Qué es una condition variable?
  - ¿Qué es code bloat?
  - ¿Por qué los templates van en el .h?
  - ¿Cuándo usar destructor virtual?
  - ¿Diferencia copy vs move constructor?

**Items:** 8 conceptos teóricos clave. Objetivo: poder explicarlos en 3 líneas c/u.

---

### MIÉRCOLES 2 JULIO (4–5 hs)
**Tema: Archivos en C — eliminar/comprimir (patrón simple)**

- [ ] Entender el patrón de 1 pasada (pos_escritura, pos_lectura)
- [ ] Practicar estos ejercicios **de memoria**, sin mirar:
  - Eliminar múltiplos de 7 de archivo de enteros de 2 bytes big-endian
  - Procesar archivo big-endian de 4 bytes triplicando impares
  - Leer base N de 3 símbolos, convertir y escribir

**Conceptos clave del día:**
- `fopen("f","r+b")`, `fread`, `fwrite`, `fseek`, `ftruncate`
- Conversión big-endian 4 bytes: `byte[0]<<24 | byte[1]<<16 | byte[2]<<8 | byte[3]`
- Conversión base N → decimal: `v = v*N + digito`
- Decimal → base N: división sucesiva + invertir

**Items:** 3 ejercicios de archivos + dominar los algoritmos de conversión.

---

### JUEVES 3 JULIO (4–5 hs)
**Tema: Archivos en C — expandir/repetir (patrón de 2 pasadas)**

- [ ] Dominar el algoritmo de backfill (el más difícil):
  1. Pasada 1: contar cuántos se repiten
  2. Reservar espacio: `fseek(f, tam_nuevo-1, SEEK_SET); fputc(0,f);`
  3. Pasada 2: mover de atrás hacia adelante
- [ ] Practicar estos ejercicios **de memoria**:
  - Repetir números múltiplos de 5 (base 7, 3 símbolos)
  - Duplicar enteros de 2 bytes múltiplos de 3
  - Duplicar palabras con 2+ vocales (archivo texto)

**Trampa frecuente:** si expandes de adelante hacia atrás, pisás datos. SIEMPRE de atrás hacia adelante.

**Items:** 3 ejercicios de backfill dominados.

---

### VIERNES 4 JULIO (4–5 hs)
**Tema: Sockets**

- [ ] Memorizar el template de servidor **de memoria** (escribirlo sin mirar)
- [ ] Practicar estas variantes:
  - Recibir paquetes terminados en `'\0'`, enviar el largo
  - Recibir palabras separadas por espacio, enviar largo de cada una; parar con 'cortar'
  - Recibir formato `"d+d+d="`, imprimir la suma; parar si suma es 0
  - Enviar 3 caracteres aleatorios, recibir respuesta, comparar; repetir o terminar
  - Recibir caracteres hasta recibir 'FIN', imprimir todo lo anterior
- [ ] Practicar template de **cliente** (con `connect()` en lugar de `bind/listen/accept`)

**Puntos clave:**
- `recv` char a char es el patrón dominante
- Siempre cerrar `client_fd` y `socket_fd`
- `INADDR_ANY` cuando no hay IP; `inet_addr(ip)` cuando sí hay
- `htons(puerto)` siempre

**Items:** 5 ejercicios de sockets practicados.

---

### SÁBADO 5 JULIO (4–5 hs)
**Tema: Clases C++ con operadores**

- [ ] Escribir **de memoria** una clase completa con:
  - Atributos privados
  - Constructor por defecto, copia y move
  - `operator++` (pre y post), `operator-`, `operator==`
  - `operator<<` y `operator>>` (con `friend`)
  - Casteo explícito (`explicit operator float()`)
- [ ] Practicar la clase PILA o LISTA con template:
  - Constructor copia y move
  - `push`, `pop`, `vacia`
  - Operadores básicos

**Conceptos clave:**
- Move: `&&`, dejar el original vacío (`otro.x = 0`)
- `friend` para `<<` y `>>`
- `explicit operator T()` para casteos
- `= delete` para prohibir copia

**Items:** 2 clases escritas de memoria (una simple, una con template).

---

### DOMINGO 6 JULIO (3–4 hs)
**Tema: Repaso de teoría + threads**

- [ ] Repasar todas las preguntas teóricas del docx:
  - RAII (con código)
  - Mutex y lock_guard (con código)
  - Condition variable productor-consumidor (con código)
  - Deadlock: qué es y cómo ocurre (con código de ejemplo)
  - Virtual methods y destructor virtual (con código)
  - Templates y por qué van en .h
  - Diferencia copy vs move
  - Smart pointers: unique_ptr, shared_ptr, weak_ptr
  - Static variables (global, local, atributo)
  - Code bloat
  - Pipeline de compilación (todas las etapas)
  - Functor
  - Especialización parcial de templates
  - `friend`
  - Acceso público/protegido/privado
- [ ] Escribir un thread con mutex (de memoria)
- [ ] Escribir productor-consumidor con condition_variable (de memoria)

**Items:** 15 respuestas teóricas + 2 ejercicios de threads.

---

### LUNES 7 JULIO — REPASO FINAL (2–3 hs)
**NO aprender cosas nuevas. Solo repasar lo que ya sabés.**

- [ ] Escribir el template de sockets sin mirar nada
- [ ] Escribir el algoritmo de backfill (expandir archivo) sin mirar
- [ ] Escribir una clase con move constructor + `operator<<` sin mirar
- [ ] Repasar 5 preguntas teóricas que menos seguridad tenés
- [ ] Dormir bien

---

## RESUMEN RÁPIDO — ¿En qué focalizar para APROBAR?

Para aprobar (no necesitás brillar, solo pasar) el foco debería ser:

### 1. ARCHIVOS EN C (30% del final aprox.)
El patrón de 2 pasadas (backfill) es LO MÁS IMPORTANTE. Sin eso, no podés resolver la mitad de los ejercicios.

### 2. SOCKETS (30% del final aprox.)
Memorizar el template de servidor de punta a punta. El loop de lógica de negocio siempre es `recv` char a char con condiciones.

### 3. CLASE CON OPERADORES (25% del final aprox.)
Move constructor + `operator<<` (con `friend`) + un operador aritmético. Si dominás eso, podés resolver cualquier variante.

### 4. PREGUNTA TEÓRICA (15% del final aprox.)
Son respuestas cortas. RAII, mutex, templates en .h, destructor virtual. Estudiá la respuesta de memoria, con código.

---

## CANTIDAD DE ITEMS POR DÍA

| Día | Items a estudiar |
|---|---|
| Martes (hoy, parcial) | 8 conceptos teóricos |
| Miércoles | 3 ejercicios archivos simples + 4 algoritmos de conversión |
| Jueves | 3 ejercicios backfill (los más difíciles) |
| Viernes | 5 ejercicios de sockets + template de memoria |
| Sábado | 2 clases C++ de memoria |
| Domingo | 15 respuestas teóricas + 2 ejercicios threads |
| Lunes | Repaso sin aprender nada nuevo |

**Total: ~37 items en 7 días. Promedio: ~5 ítems por día. Es manejable.**

---

## TIPS PARA EL EXAMEN

1. **Siempre verificar errores en sockets**: `if (fd < 0) return -1;`
2. **En archivos en C**: nunca olvidar `fclose(f)` y `ftruncate` si achicás el archivo
3. **En el move constructor**: siempre dejar el original en estado válido pero vacío
4. **En `operator<<`**: debe ser `friend` y retornar `std::ostream&`
5. **Templates**: definición siempre en el `.h`, nunca en `.cpp`
6. **`ntohl()` vs bit shifting**: ambos sirven para convertir big-endian, pero el bit shifting es multiplataforma seguro
7. **`htons()`**: convertir puerto a network byte order (siempre)
8. **Destructor virtual**: si la clase tiene herencia y polimorfismo, siempre `virtual ~Base()`
