# Gantt Chart (Diagrama de Gantt) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/gantt.html

Los diagramas de Gantt ilustran cronogramas de proyectos, mostrando tareas, duraciones y dependencias.

## Sintaxis Basica

```mermaid
gantt
    title Proyecto Simple
    dateFormat YYYY-MM-DD
    
    section Fase 1
        Tarea A :a1, 2024-01-01, 5d
        Tarea B :a2, after a1, 3d
    
    section Fase 2
        Tarea C :b1, after a2, 4d
```

## Estructura General

```
gantt
    title Titulo del proyecto
    dateFormat FORMATO
    
    section Nombre de seccion
        Nombre tarea :id, fecha_inicio, duracion
```

## Configuracion de Fechas

### dateFormat

Define el formato de entrada de fechas:

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Tarea :2024-01-15, 10d
```

| Formato | Ejemplo |
|---------|---------|
| `YYYY-MM-DD` | 2024-01-15 |
| `DD-MM-YYYY` | 15-01-2024 |
| `YYYY-MM-DD HH:mm` | 2024-01-15 14:30 |

### axisFormat

Define como se muestra el eje temporal:

```mermaid
gantt
    dateFormat YYYY-MM-DD
    axisFormat %Y-%m-%d
    
    section Proyecto
        Tarea :2024-01-01, 30d
```

| Formato | Resultado | Descripcion |
|---------|-----------|-------------|
| `%Y` | 2024 | Ano completo |
| `%y` | 24 | Ano corto |
| `%m` | 01-12 | Mes |
| `%d` | 01-31 | Dia |
| `%H` | 00-23 | Hora |
| `%M` | 00-59 | Minutos |
| `%B` | January | Nombre del mes |
| `%b` | Jan | Mes abreviado |
| `%A` | Monday | Dia de la semana |
| `%a` | Mon | Dia abreviado |
| `%W` | 01-53 | Numero de semana |

### tickInterval

Define el intervalo de las marcas del eje:

```mermaid
gantt
    dateFormat YYYY-MM-DD
    tickInterval 1week
    
    section Proyecto
        Tarea :2024-01-01, 30d
```

Opciones: `1day`, `1week`, `1month`, `1year`

## Definicion de Tareas

### Sintaxis Completa

```
Nombre tarea :[estado], [id], [fecha_inicio | after id], duracion
```

### Por Fecha de Inicio

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Tareas
        Tarea 1 :t1, 2024-01-01, 5d
        Tarea 2 :t2, 2024-01-03, 3d
```

### Por Dependencia

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Tareas
        Tarea 1 :t1, 2024-01-01, 5d
        Tarea 2 :t2, after t1, 3d
        Tarea 3 :t3, after t1 t2, 2d
```

### Con Fecha de Fin

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Tareas
        Tarea :2024-01-01, 2024-01-10
```

## Estados de Tareas

### Tareas Completadas

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Estados
        Completada :done, t1, 2024-01-01, 3d
        Normal :t2, after t1, 3d
```

### Tareas Activas

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Estados
        En progreso :active, t1, 2024-01-01, 5d
        Pendiente :t2, after t1, 3d
```

### Tareas Criticas

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Estados
        Critica :crit, t1, 2024-01-01, 3d
        Normal :t2, after t1, 3d
```

### Combinacion de Estados

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Completada         :done, d1, 2024-01-01, 3d
        Activa             :active, a1, after d1, 3d
        Critica            :crit, c1, after a1, 3d
        Critica y activa   :crit, active, c2, after c1, 3d
        Pendiente          :p1, after c2, 3d
```

## Milestones (Hitos)

Los hitos son puntos de referencia sin duracion:

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Desarrollo
        Desarrollo      :t1, 2024-01-01, 10d
        Lanzamiento     :milestone, m1, after t1, 0d
        Soporte         :t2, after m1, 5d
```

## Secciones

Agrupan tareas relacionadas:

```mermaid
gantt
    title Proyecto de Software
    dateFormat YYYY-MM-DD
    
    section Planificacion
        Requisitos    :req, 2024-01-01, 5d
        Diseno        :des, after req, 5d
    
    section Desarrollo
        Backend       :bak, after des, 10d
        Frontend      :fro, after des, 10d
    
    section Testing
        QA            :qa, after bak fro, 5d
        UAT           :uat, after qa, 3d
    
    section Despliegue
        Deploy        :dep, after uat, 2d
        Go-Live       :milestone, gl, after dep, 0d
```

## Exclusion de Fechas

### Excluir Fines de Semana

```mermaid
gantt
    dateFormat YYYY-MM-DD
    excludes weekends
    
    section Proyecto
        Tarea de 10 dias :2024-01-01, 10d
```

### Excluir Fechas Especificas

```mermaid
gantt
    dateFormat YYYY-MM-DD
    excludes 2024-01-15, 2024-01-16
    
    section Proyecto
        Tarea :2024-01-10, 10d
```

### Dias Laborables

```mermaid
gantt
    dateFormat YYYY-MM-DD
    excludes weekends
    
    section Sprint 1
        Tarea 1 :2024-01-01, 5d
        Tarea 2 :2024-01-08, 5d
```

## Marcadores Verticales

Marcan fechas importantes:

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Desarrollo :t1, 2024-01-01, 20d
    
    vert Deadline :2024-01-15
    vert Review :2024-01-10
```

## Interactividad

### Click Events

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Tarea con link :t1, 2024-01-01, 5d
    
    click t1 href "https://example.com"
```

### Callback

```mermaid
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Tarea clickeable :t1, 2024-01-01, 5d
    
    click t1 call callback()
```

## Configuracion Avanzada

### Frontmatter

```mermaid
---
config:
  gantt:
    titleTopMargin: 25
    barHeight: 20
    barGap: 4
    topPadding: 50
    leftPadding: 75
    gridLineStartPadding: 35
    fontSize: 11
    numberSectionStyles: 4
---
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Tarea :2024-01-01, 10d
```

### Directivas

```mermaid
%%{init: {'gantt': {'barHeight': 30, 'fontSize': 14}}}%%
gantt
    dateFormat YYYY-MM-DD
    
    section Proyecto
        Tarea :2024-01-01, 10d
```

## Ejemplos Completos

### Proyecto de Desarrollo Web

```mermaid
gantt
    title Desarrollo de Aplicacion Web
    dateFormat YYYY-MM-DD
    excludes weekends
    
    section Analisis
        Levantamiento de requisitos  :done, req, 2024-01-01, 5d
        Documentacion de requisitos  :done, doc, after req, 3d
        Aprobacion                   :milestone, apr, after doc, 0d
    
    section Diseno
        Arquitectura del sistema     :done, arq, after apr, 4d
        Diseno de base de datos      :done, db, after apr, 3d
        Mockups UI/UX                :active, ui, after apr, 5d
    
    section Desarrollo
        Setup del proyecto           :crit, set, after arq db, 2d
        Desarrollo Backend           :crit, bak, after set, 15d
        Desarrollo Frontend          :fro, after ui, 15d
        Integracion API              :int, after bak, 5d
    
    section Testing
        Pruebas unitarias            :test1, after bak, 5d
        Pruebas de integracion       :test2, after int fro, 5d
        Pruebas de usuario           :uat, after test2, 3d
    
    section Despliegue
        Preparar ambiente            :prep, after test2, 2d
        Despliegue a produccion      :dep, after uat prep, 1d
        Go-Live                      :milestone, gl, after dep, 0d
```

### Sprint de Scrum

```mermaid
gantt
    title Sprint 15 - Equipo Alpha
    dateFormat YYYY-MM-DD
    excludes weekends
    axisFormat %d/%m
    
    section Planificacion
        Sprint Planning         :done, sp, 2024-01-08, 1d
    
    section Historia 1
        US-101 Desarrollo       :done, us101, after sp, 3d
        US-101 Testing          :done, us101t, after us101, 1d
    
    section Historia 2
        US-102 Desarrollo       :active, us102, after sp, 4d
        US-102 Testing          :us102t, after us102, 1d
    
    section Historia 3
        US-103 Desarrollo       :crit, us103, 2024-01-10, 3d
        US-103 Testing          :crit, us103t, after us103, 2d
    
    section Cierre
        Code Review             :cr, 2024-01-17, 1d
        Demo                    :demo, 2024-01-18, 1d
        Retrospectiva           :retro, after demo, 1d
        Sprint Review           :milestone, sr, after retro, 0d
```

### Lanzamiento de Producto

```mermaid
gantt
    title Lanzamiento Producto v2.0
    dateFormat YYYY-MM-DD
    
    section Pre-Lanzamiento
        Finalizar desarrollo     :done, dev, 2024-01-01, 14d
        QA Final                 :done, qa, after dev, 7d
        Beta testing             :active, beta, after qa, 10d
        Fix bugs criticos        :crit, fix, after beta, 5d
    
    section Marketing
        Preparar materiales      :mkt1, 2024-01-15, 14d
        Campana de expectativa   :mkt2, after mkt1, 7d
        Comunicado de prensa     :mkt3, 2024-02-10, 3d
    
    section Lanzamiento
        Deploy final             :dep, 2024-02-14, 1d
        Lanzamiento publico      :milestone, launch, 2024-02-15, 0d
    
    section Post-Lanzamiento
        Monitoreo                :mon, after launch, 7d
        Soporte intensivo        :sup, after launch, 14d
        Retrospectiva            :retro, 2024-03-01, 1d
```

## Opciones de Configuracion

| Opcion | Descripcion | Default |
|--------|-------------|---------|
| `titleTopMargin` | Margen superior del titulo | 25 |
| `barHeight` | Altura de las barras | 20 |
| `barGap` | Espacio entre barras | 4 |
| `topPadding` | Padding superior | 50 |
| `leftPadding` | Padding izquierdo | 75 |
| `fontSize` | Tamano de fuente | 11 |
| `sectionFontSize` | Tamano fuente secciones | 11 |
| `numberSectionStyles` | Estilos de seccion | 4 |

## Tips y Mejores Practicas

1. **Usar IDs significativos**: Facilita las dependencias
2. **Agrupar en secciones**: Mejora la legibilidad
3. **Usar milestones**: Para marcar puntos clave
4. **Excluir fines de semana**: Para proyectos laborales
5. **Marcar tareas criticas**: Identifica el camino critico
6. **Mantener actualizados los estados**: done, active, crit
