# Pie Chart (Grafico Circular) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/pie.html

Los graficos circulares (pie charts) representan proporciones numericas de un todo, mostrando cada categoria como una porcion del circulo.

## Sintaxis Basica

```mermaid
pie
    title Distribucion de Ventas
    "Producto A" : 42
    "Producto B" : 28
    "Producto C" : 18
    "Otros" : 12
```

## Estructura General

```
pie [showData]
    title Titulo del grafico
    "Etiqueta 1" : valor1
    "Etiqueta 2" : valor2
```

## Mostrar Valores

### Sin Valores (Default)

```mermaid
pie
    title Uso de Lenguajes
    "JavaScript" : 40
    "Python" : 30
    "Java" : 20
    "Otros" : 10
```

### Con Valores (showData)

```mermaid
pie showData
    title Uso de Lenguajes
    "JavaScript" : 40
    "Python" : 30
    "Java" : 20
    "Otros" : 10
```

## Sintaxis de Datos

### Formato Basico

```mermaid
pie
    "Categoria" : valor
```

### Reglas

- Las etiquetas van entre comillas dobles `""`
- Los valores deben ser **positivos** y **mayores a cero**
- Usar `:` para separar etiqueta del valor
- Los valores pueden ser enteros o decimales

### Valores Decimales

```mermaid
pie showData
    title Distribucion Precisa
    "Seccion A" : 42.5
    "Seccion B" : 28.3
    "Seccion C" : 29.2
```

## Titulo

### Con Titulo

```mermaid
pie
    title Mi Grafico Circular
    "A" : 50
    "B" : 50
```

### Sin Titulo

```mermaid
pie
    "A" : 50
    "B" : 50
```

## Ejemplos por Categoria

### Navegadores Web

```mermaid
pie showData
    title Cuota de Mercado de Navegadores 2024
    "Chrome" : 65
    "Safari" : 18
    "Firefox" : 8
    "Edge" : 5
    "Otros" : 4
```

### Presupuesto

```mermaid
pie showData
    title Distribucion del Presupuesto
    "Desarrollo" : 35
    "Marketing" : 25
    "Operaciones" : 20
    "Infraestructura" : 12
    "Otros" : 8
```

### Encuesta de Satisfaccion

```mermaid
pie showData
    title Resultados de Encuesta de Satisfaccion
    "Muy Satisfecho" : 45
    "Satisfecho" : 30
    "Neutral" : 15
    "Insatisfecho" : 7
    "Muy Insatisfecho" : 3
```

### Fuentes de Trafico

```mermaid
pie showData
    title Fuentes de Trafico Web
    "Busqueda Organica" : 40
    "Redes Sociales" : 25
    "Directo" : 20
    "Referidos" : 10
    "Email" : 5
```

### Composicion de Equipo

```mermaid
pie showData
    title Composicion del Equipo
    "Desarrolladores" : 8
    "QA" : 3
    "Diseno" : 2
    "Product" : 2
    "DevOps" : 1
```

## Configuracion y Temas

### Tema Default

```mermaid
pie
    title Tema Default
    "A" : 30
    "B" : 40
    "C" : 30
```

### Tema Forest

```mermaid
%%{init: {'theme': 'forest'}}%%
pie
    title Tema Forest
    "A" : 30
    "B" : 40
    "C" : 30
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
pie
    title Tema Dark
    "A" : 30
    "B" : 40
    "C" : 30
```

### Tema Neutral

```mermaid
%%{init: {'theme': 'neutral'}}%%
pie
    title Tema Neutral
    "A" : 30
    "B" : 40
    "C" : 30
```

### Personalizacion de Colores

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'pie1': '#ff6b6b', 'pie2': '#4ecdc4', 'pie3': '#45b7d1', 'pie4': '#f9ca24'}}}%%
pie showData
    title Colores Personalizados
    "Rojo" : 25
    "Verde" : 25
    "Azul" : 25
    "Amarillo" : 25
```

## Configuracion Avanzada

### Usando Frontmatter

```mermaid
---
config:
  theme: forest
  pie:
    textPosition: 0.75
---
pie showData
    title Configuracion Avanzada
    "A" : 40
    "B" : 35
    "C" : 25
```

### Opciones de Configuracion

| Opcion | Descripcion | Default |
|--------|-------------|---------|
| `textPosition` | Posicion del texto (0-1) | 0.75 |
| `useWidth` | Usar ancho maximo | undefined |

## Variables de Tema para Pie

Las variables `pie1` hasta `pie12` controlan los colores de cada seccion:

```javascript
themeVariables: {
  pie1: '#color1',
  pie2: '#color2',
  pie3: '#color3',
  // ... hasta pie12
}
```

## Ejemplos Completos

### Dashboard de Metricas

```mermaid
pie showData
    title Estado de Tickets - Sprint 10
    "Completados" : 15
    "En Progreso" : 5
    "En Review" : 3
    "Bloqueados" : 2
```

### Analisis de Costos

```mermaid
pie showData
    title Desglose de Costos Mensuales
    "Salarios" : 55000
    "Infraestructura" : 15000
    "Software/Licencias" : 8000
    "Marketing" : 12000
    "Oficina" : 5000
    "Otros" : 5000
```

### Resultados de Votacion

```mermaid
pie showData
    title Resultado de Votacion
    "Opcion A" : 342
    "Opcion B" : 256
    "Opcion C" : 189
    "Abstencion" : 45
```

### Uso de Tiempo

```mermaid
pie showData
    title Distribucion de Tiempo Diario
    "Trabajo" : 8
    "Sueno" : 7
    "Ocio" : 4
    "Comidas" : 2
    "Ejercicio" : 1
    "Transporte" : 2
```

## Limitaciones

1. **Sin valores negativos**: Todos los valores deben ser positivos
2. **Sin cero**: Los valores deben ser mayores a cero
3. **Limite de secciones**: Demasiadas secciones reducen legibilidad
4. **Sin interactividad**: No soporta click events nativamente

## Tips y Mejores Practicas

1. **Limitar secciones**: Maximo 5-7 para mejor legibilidad
2. **Usar "Otros"**: Agrupar secciones pequenas
3. **Ordenar por tamano**: De mayor a menor para mejor visualizacion
4. **Usar showData**: Cuando los valores exactos importan
5. **Etiquetas cortas**: Nombres concisos pero descriptivos
6. **Considerar alternativas**: Para muchas categorias, usar graficos de barras

## Cuando Usar Pie Charts

| Usar Cuando | Evitar Cuando |
|-------------|---------------|
| Mostrar partes de un todo | Comparar valores similares |
| Pocas categorias (2-7) | Muchas categorias |
| Proporciones significativas | Valores muy pequenos |
| Visualizacion simple | Datos temporales |
