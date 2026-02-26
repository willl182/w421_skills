# Timeline (Linea de Tiempo) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/timeline.html

Las lineas de tiempo ilustran cronologias de eventos, mostrando la progresion temporal de acontecimientos.

## Sintaxis Basica

```mermaid
timeline
    title Historia de la Empresa
    2020 : Fundacion
    2021 : Primer producto
    2022 : Expansion
    2023 : Internacionalizacion
```

## Estructura General

```
timeline
    title Titulo de la linea de tiempo
    periodo : evento1 : evento2
    section Nombre de seccion
        periodo : evento
```

## Componentes

### Titulo

```mermaid
timeline
    title Mi Linea de Tiempo
    2024 : Evento
```

### Periodos y Eventos

```mermaid
timeline
    Enero : Inicio del proyecto
    Febrero : Primera fase
    Marzo : Lanzamiento
```

### Multiples Eventos por Periodo

```mermaid
timeline
    2024 Q1 : Evento 1 : Evento 2 : Evento 3
    2024 Q2 : Evento 4
    2024 Q3 : Evento 5 : Evento 6
```

## Secciones

Las secciones agrupan periodos relacionados:

```mermaid
timeline
    title Evolucion del Desarrollo Web

    section Era Estatica
        1991 : HTML
        1995 : JavaScript
        1996 : CSS

    section Era Dinamica
        1995 : PHP
        1996 : ASP
        2004 : Ruby on Rails

    section Era Moderna
        2010 : AngularJS
        2013 : React
        2014 : Vue.js
```

## Formatos de Periodo

### Anos

```mermaid
timeline
    2020 : Evento A
    2021 : Evento B
    2022 : Evento C
```

### Trimestres

```mermaid
timeline
    Q1 2024 : Planificacion
    Q2 2024 : Desarrollo
    Q3 2024 : Testing
    Q4 2024 : Lanzamiento
```

### Meses

```mermaid
timeline
    Enero : Kickoff
    Febrero : Desarrollo
    Marzo : Beta
    Abril : Release
```

### Fechas Especificas

```mermaid
timeline
    2024-01-15 : Inicio
    2024-02-28 : Milestone 1
    2024-03-31 : Milestone 2
```

### Texto Libre

```mermaid
timeline
    Fase 1 : Investigacion
    Fase 2 : Prototipo
    Fase 3 : Produccion
```

## Ejemplos por Categoria

### Historia de Tecnologia

```mermaid
timeline
    title Historia de JavaScript

    section Origenes
        1995 : Netscape crea JavaScript
              : Brendan Eich lo desarrolla en 10 dias
        1996 : Microsoft crea JScript
        1997 : ECMAScript 1

    section Evolucion
        1999 : ECMAScript 3
        2005 : AJAX revoluciona la web
        2006 : jQuery
        2009 : Node.js : ECMAScript 5

    section Era Moderna
        2010 : AngularJS
        2013 : React
        2014 : Vue.js
        2015 : ECMAScript 6 (ES2015)
        2020 : Deno
```

### Roadmap de Producto

```mermaid
timeline
    title Roadmap 2024

    section Q1
        Enero : Planificacion estrategica
               : Definicion de OKRs
        Febrero : Desarrollo MVP
        Marzo : Beta privada

    section Q2
        Abril : Beta publica
        Mayo : Iteracion basada en feedback
        Junio : Lanzamiento v1.0

    section Q3
        Julio : Features adicionales
        Agosto : Optimizacion
        Septiembre : Version 1.1

    section Q4
        Octubre : Expansion de mercado
        Noviembre : Version 2.0 planificacion
        Diciembre : Retrospectiva anual
```

### Proceso de Proyecto

```mermaid
timeline
    title Ciclo de Vida del Proyecto

    section Inicio
        Semana 1 : Kickoff meeting
                 : Definicion de alcance
        Semana 2 : Gathering de requisitos
                 : Analisis de stakeholders

    section Planificacion
        Semana 3 : Arquitectura
                 : Estimaciones
        Semana 4 : Sprint planning
                 : Setup de ambiente

    section Ejecucion
        Semana 5-8 : Desarrollo iterativo
        Semana 9-10 : Testing

    section Cierre
        Semana 11 : UAT
        Semana 12 : Go-live
                  : Handover
```

### Biografia/Historia Personal

```mermaid
timeline
    title Mi Carrera en Tech

    section Educacion
        2010 : Inicio universidad
        2014 : Graduacion CS

    section Primeros Trabajos
        2014 : Junior Developer en Startup
        2016 : Mid Developer en Agencia
        2018 : Senior Developer

    section Liderazgo
        2020 : Tech Lead
        2022 : Engineering Manager
        2024 : CTO Startup
```

### Release History

```mermaid
timeline
    title Historial de Versiones

    section Version 1.x
        v1.0 : Lanzamiento inicial
             : Features basicos
        v1.1 : Bug fixes
        v1.2 : Mejoras de performance

    section Version 2.x
        v2.0 : Rediseno completo
             : Nueva arquitectura
        v2.1 : Nuevas integraciones
        v2.2 : API publica

    section Version 3.x
        v3.0 : Mobile support
             : Offline mode
             : Real-time sync
```

### Sprint Timeline

```mermaid
timeline
    title Sprint 15 - Equipo Alpha

    section Planificacion
        Dia 1 : Sprint Planning
              : Refinement

    section Desarrollo
        Dia 2-3 : US-101 Login social
        Dia 4-5 : US-102 Dashboard
        Dia 6-7 : US-103 Notificaciones

    section QA
        Dia 8 : Testing
              : Bug fixes

    section Cierre
        Dia 9 : Code review final
        Dia 10 : Demo
                : Retrospectiva
```

### Historia de Empresa

```mermaid
timeline
    title Startup Journey

    section Idea
        2019 : Idea inicial
             : Investigacion de mercado
             : Primer prototipo

    section Fundacion
        2020 : Incorporacion legal
             : Equipo fundador
             : Seed funding

    section Crecimiento
        2021 : Serie A
             : 50 empleados
             : Expansion regional
        2022 : Serie B
             : 200 empleados
             : Internacionalizacion

    section Consolidacion
        2023 : Profitabilidad
             : Adquisicion estrategica
        2024 : IPO
```

## Configuracion

### Temas

```mermaid
%%{init: {'theme': 'forest'}}%%
timeline
    title Tema Forest
    2024 : Evento 1
    2025 : Evento 2
```

```mermaid
%%{init: {'theme': 'dark'}}%%
timeline
    title Tema Dark
    2024 : Evento 1
    2025 : Evento 2
```

### Personalizacion

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
    'cScale0': '#ff6b6b',
    'cScale1': '#4ecdc4',
    'cScale2': '#45b7d1'
}}}%%
timeline
    title Colores Personalizados

    section Rojo
        2024 : Evento A

    section Verde
        2025 : Evento B

    section Azul
        2026 : Evento C
```

## Variables de Tema

| Variable | Descripcion |
|----------|-------------|
| `cScale0` - `cScale11` | Colores de las secciones |
| `cScaleLabel0` - `cScaleLabel11` | Colores de etiquetas |

## Tips y Mejores Practicas

1. **Periodos claros**: Usar formatos de fecha consistentes
2. **Eventos concisos**: Descripciones cortas y precisas
3. **Usar secciones**: Agrupar eventos relacionados
4. **Balance visual**: No sobrecargar un periodo
5. **Orden cronologico**: Mantener secuencia temporal
6. **Multiples eventos**: Usar `:` para separar eventos del mismo periodo
7. **Titulos descriptivos**: El titulo debe indicar el tema de la timeline

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Roadmaps | Planificacion de productos |
| Historia | Cronologia de eventos pasados |
| Biografias | Trayectoria personal/profesional |
| Releases | Historial de versiones |
| Proyectos | Fases y milestones |
| Sprints | Planificacion de iteraciones |
| Onboarding | Proceso de incorporacion |
