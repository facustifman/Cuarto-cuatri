# Guía rápida de Markdown — apuntes básicos

Este archivo contiene ejemplos y atajos para tomar apuntes en Markdown (.md) dentro de VS Code.

---

## Encabezados

Usa el símbolo # seguido de un espacio. Hay 6 niveles:

# Título nivel 1
## Título nivel 2
### Título nivel 3

## Énfasis (negrita / cursiva)

- Cursiva: *texto* o _texto_
- Negrita: **texto** o __texto__
- Negrita + cursiva: **_texto_**

## Listas

- Lista no ordenada:
	- elemento 1
	- elemento 2

1. Lista ordenada:
	 1. item 1
	 2. item 2

## Código

- Inline: `codigo()`
- Bloque de código (fenced) con lenguaje para resaltado:

```python
def hola():
		print("hola mundo")
```

## Citas (blockquote)

> Esta es una cita.

## Enlaces e imágenes

- Enlace: [Texto visible](https://example.com)
- Imagen (local o URL): ![Alt text](./imagenes/diagrama.png)

> Consejo: crea una carpeta `imagenes/` dentro de tu carpeta de notas y guarda las capturas ahí.

## Tablas

| Columna A | Columna B |
| --- | ---: |
| izquierda | derecha alineada |

## Línea horizontal

---

## Listas de tareas (task lists)

- [x] Tarea hecha
- [ ] Tarea pendiente

## Atajos y uso en VS Code

- Guardar el archivo con extensión `.md` (por ejemplo `clase_10_3.md`).
- Vista previa: Ctrl+Shift+V (o clic derecho -> Open Preview).
- Panel dividido: Ctrl+\ para ver editor y vista previa lado a lado.
- Instalar extensiones útiles: "Markdown All in One", "Markdownlint", "Paste Image", "Foam" (si quieres notas enlazadas tipo wiki).

## Plantilla rápida para notas (pegar al inicio de una nueva nota)

```
# {{TÍTULO}}

- Fecha: YYYY-MM-DD
- Clase / Tema: 
- Tags: #materia #tema

## Resumen

## Notas

## Tareas / Pendientes
- [ ] 

```

## Buenas prácticas

- Mantén una carpeta `notas/` en el workspace para agrupar tus .md.
- Usa enlaces relativos para vincular notas: `[Ver tema anterior](../notas/tema_anterior.md)`.
- Divide notas largas en secciones y usa índices (extensión "Markdown All in One" puede generar TOC automáticamente).

---

Si querés, puedo:
- crear una carpeta `notas/` y añadir esta plantilla como `notas/template.md` en tu workspace, o
- instalar/configurar recomendaciones (si me decís qué extensiones querés activar). 

Dime cuál opción preferís y la aplico.

