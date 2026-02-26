# Radar Chart (Grafico de Radar) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/radar.html

Los graficos de radar (tambien conocidos como spider charts o graficos de araña) visualizan datos multivariados en un formato radial, ideal para comparar multiples variables.

## Sintaxis Basica

```mermaid
radar-beta
    title "Evaluacion de Habilidades"
    axis JavaScript, TypeScript, React, Node.js, CSS
    curve a[Juan] { 80, 70, 90, 75, 85 }
    curve b[Maria] { 70, 90, 80, 85, 70 }
```

## Estructura General

```
radar-beta
    title "Titulo"
    axis Variable1, Variable2, Variable3, ...
    curve id[Etiqueta] { valor1, valor2, valor3, ... }
```

## Componentes

### Titulo

```mermaid
radar-beta
    title "Mi Grafico Radar"
    axis A, B, C, D, E
    curve x[Serie] { 60, 70, 80, 70, 60 }
```

### Ejes (Axis)

Los ejes definen las variables a medir:

```mermaid
radar-beta
    title "Competencias Tecnicas"
    axis Frontend, Backend, DevOps, Testing, Architecture
    curve dev[Developer] { 85, 70, 60, 75, 65 }
```

### Curvas (Series de Datos)

Cada curva representa un conjunto de datos:

```mermaid
radar-beta
    title "Comparativa de Productos"
    axis Precio, Calidad, Soporte, Features, Facilidad
    curve a[Producto A] { 80, 90, 70, 85, 75 }
    curve b[Producto B] { 60, 70, 90, 75, 85 }
    curve c[Producto C] { 90, 60, 80, 65, 70 }
```

## Ejemplos por Categoria

### Evaluacion de Empleados

```mermaid
radar-beta
    title "Evaluacion de Desempeno"
    axis Comunicacion, Liderazgo, Tecnico, Trabajo en Equipo, Iniciativa, Puntualidad
    curve emp1[Empleado 1] { 85, 70, 90, 80, 75, 95 }
    curve emp2[Empleado 2] { 75, 85, 80, 90, 80, 85 }
```

### Stack Tecnologico

```mermaid
radar-beta
    title "Dominio de Tecnologias"
    axis JavaScript, Python, SQL, Docker, Kubernetes, AWS
    curve junior[Junior Dev] { 70, 50, 60, 40, 20, 30 }
    curve senior[Senior Dev] { 90, 80, 85, 75, 70, 80 }
    curve lead[Tech Lead] { 85, 75, 90, 85, 80, 90 }
```

### Analisis de Producto

```mermaid
radar-beta
    title "Analisis Competitivo"
    axis Usabilidad, Rendimiento, Seguridad, Escalabilidad, Costo, Soporte
    curve nuestro[Nuestro Producto] { 85, 75, 90, 80, 70, 85 }
    curve comp1[Competidor A] { 70, 90, 75, 85, 60, 70 }
    curve comp2[Competidor B] { 80, 70, 80, 70, 90, 60 }
```

### Framework Comparison

```mermaid
radar-beta
    title "Comparativa de Frameworks Frontend"
    axis Rendimiento, Curva Aprendizaje, Ecosistema, Documentacion, Comunidad
    curve react[React] { 85, 60, 95, 90, 95 }
    curve vue[Vue] { 80, 85, 80, 85, 80 }
    curve angular[Angular] { 75, 50, 85, 90, 75 }
    curve svelte[Svelte] { 95, 80, 60, 75, 65 }
```

### Evaluacion de Proyecto

```mermaid
radar-beta
    title "Estado del Proyecto"
    axis Scope, Tiempo, Presupuesto, Calidad, Riesgos, Recursos
    curve actual[Estado Actual] { 80, 60, 70, 85, 55, 75 }
    curve objetivo[Objetivo] { 90, 90, 85, 90, 80, 85 }
```

### Soft Skills

```mermaid
radar-beta
    title "Evaluacion de Soft Skills"
    axis Comunicacion, Empatia, Resolucion Problemas, Adaptabilidad, Creatividad, Liderazgo
    curve candidato1[Candidato A] { 85, 80, 90, 75, 70, 65 }
    curve candidato2[Candidato B] { 70, 90, 75, 85, 80, 75 }
    curve candidato3[Candidato C] { 75, 75, 85, 80, 85, 90 }
```

### Game Character Stats

```mermaid
radar-beta
    title "Estadisticas de Personaje"
    axis Fuerza, Velocidad, Inteligencia, Defensa, Magia, Suerte
    curve warrior[Guerrero] { 90, 60, 40, 85, 20, 50 }
    curve mage[Mago] { 30, 50, 95, 40, 100, 60 }
    curve rogue[Picaro] { 50, 95, 70, 35, 40, 85 }
```

### Encuesta de Clima Laboral

```mermaid
radar-beta
    title "Clima Organizacional"
    axis Ambiente, Beneficios, Crecimiento, Liderazgo, Balance, Reconocimiento
    curve dept1[Departamento A] { 80, 75, 70, 85, 65, 75 }
    curve dept2[Departamento B] { 70, 80, 85, 70, 80, 65 }
    curve dept3[Departamento C] { 85, 70, 75, 80, 75, 85 }
```

### Evaluacion de Startups

```mermaid
radar-beta
    title "Evaluacion de Inversión"
    axis Equipo, Mercado, Producto, Traccion, Finanzas, Competencia
    curve startup1[Startup A] { 85, 90, 75, 60, 50, 70 }
    curve startup2[Startup B] { 70, 75, 90, 80, 65, 60 }
```

### Assessment de Seguridad

```mermaid
radar-beta
    title "Assessment de Seguridad IT"
    axis Identidad, Red, Datos, Endpoints, Cloud, Respuesta
    curve q1[Q1 2024] { 60, 70, 55, 65, 50, 45 }
    curve q2[Q2 2024] { 75, 80, 70, 75, 65, 60 }
    curve objetivo[Objetivo] { 90, 90, 85, 90, 85, 80 }
```

## Configuracion

### Tema Default

```mermaid
radar-beta
    title "Tema Default"
    axis A, B, C, D, E
    curve x[Serie] { 70, 80, 60, 90, 75 }
```

### Tema Forest

```mermaid
%%{init: {'theme': 'forest'}}%%
radar-beta
    title "Tema Forest"
    axis A, B, C, D, E
    curve x[Serie] { 70, 80, 60, 90, 75 }
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
radar-beta
    title "Tema Dark"
    axis A, B, C, D, E
    curve x[Serie] { 70, 80, 60, 90, 75 }
    curve y[Serie 2] { 60, 70, 80, 70, 60 }
```

## Opciones de Configuracion

| Opcion | Descripcion |
|--------|-------------|
| `showLegend` | Mostrar leyenda |
| `legendTitle` | Titulo de la leyenda |

## Consideraciones

### Numero de Ejes

- **Minimo recomendado**: 3 ejes
- **Optimo**: 5-8 ejes
- **Maximo practico**: 10-12 ejes

### Escala de Valores

- Los valores tipicamente van de 0 a 100
- Mantener escala consistente entre series
- Valores similares facilitan comparacion

### Numero de Series

- 2-4 series para mejor legibilidad
- Demasiadas series dificultan la lectura
- Usar colores distinguibles

## Mejores Practicas

1. **Ejes significativos**: Variables relevantes y comparables
2. **Escala uniforme**: Misma escala para todos los ejes
3. **Etiquetas cortas**: Nombres de ejes concisos
4. **Series limitadas**: 2-4 para mejor visualizacion
5. **Valores normalizados**: Convertir a porcentajes si es necesario
6. **Orden logico**: Organizar ejes con criterio

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Evaluaciones | Desempeno, competencias |
| Comparativas | Productos, tecnologias |
| Assessments | Seguridad, madurez |
| Perfiles | Skills, caracteristicas |
| Encuestas | Resultados multidimensionales |
| Gaming | Stats de personajes |

## Interpretacion

### Fortalezas y Debilidades

- **Picos**: Indican fortalezas
- **Valles**: Indican areas de mejora
- **Area cubierta**: Indica rendimiento general

### Comparacion

- **Superposicion**: Series similares
- **Diferencias**: Areas de diferenciacion
- **Complementariedad**: Series que se complementan

## Limitaciones

- Esta en version **beta**
- Opciones de estilo limitadas
- Sin interactividad
- Maximo de ejes/series practico

## Notas

- `radar-beta` indica version beta
- Los valores deben coincidir en numero con los ejes
- Las etiquetas de curva van entre corchetes `[]`
- Los valores van entre llaves `{}`
