# Kanban Board (Tablero Kanban) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/kanban.html

Los tableros Kanban visualizan flujos de trabajo con columnas que representan etapas del proceso y tarjetas que representan items de trabajo.

## Sintaxis Basica

```mermaid
kanban
    column1[Todo]
        task1[Tarea 1]
        task2[Tarea 2]
    column2[In Progress]
        task3[Tarea 3]
    column3[Done]
        task4[Tarea 4]
```

## Estructura General

```
kanban
    columna[Titulo Columna]
        tarea[Titulo Tarea]
        tarea[Titulo Tarea]
    columna[Titulo Columna]
        tarea[Titulo Tarea]
```

## Columnas

### Multiples Columnas

```mermaid
kanban
    backlog[Backlog]
        item1[Item 1]
    todo[To Do]
        item2[Item 2]
    progress[In Progress]
        item3[Item 3]
    review[Review]
        item4[Item 4]
    done[Done]
        item5[Item 5]
```

### Columnas Vacias

```mermaid
kanban
    todo[To Do]
        task1[Tarea pendiente]
    inprogress[In Progress]
    done[Done]
```

## Tarjetas

### Tarjetas Simples

```mermaid
kanban
    backlog[Backlog]
        us1[US-001: Login de usuario]
        us2[US-002: Registro]
        us3[US-003: Recuperar password]
```

### Multiples Tarjetas por Columna

```mermaid
kanban
    todo[To Do]
        t1[Disenar mockups]
        t2[Escribir tests]
        t3[Documentar API]
        t4[Configurar CI/CD]
    doing[Doing]
        t5[Implementar login]
        t6[Crear base de datos]
```

## Ejemplos por Contexto

### Sprint Board

```mermaid
kanban
    backlog[Sprint Backlog]
        us101[US-101: Autenticacion OAuth]
        us102[US-102: Perfil de usuario]
        us103[US-103: Notificaciones push]
    todo[To Do]
        us104[US-104: Dashboard metricas]
        us105[US-105: Exportar reportes]
    inprogress[In Progress]
        us106[US-106: API de pagos]
        us107[US-107: Carrito de compras]
    review[Code Review]
        us108[US-108: Busqueda avanzada]
    testing[Testing]
        us109[US-109: Filtros de productos]
    done[Done]
        us110[US-110: Homepage redesign]
        us111[US-111: Footer actualizado]
```

### Personal Task Board

```mermaid
kanban
    ideas[Ideas]
        i1[Aprender Rust]
        i2[Curso de ML]
        i3[Blog personal]
    thisweek[Esta Semana]
        w1[Terminar proyecto X]
        w2[Reunion con cliente]
        w3[Preparar presentacion]
    today[Hoy]
        t1[Code review PR #123]
        t2[Actualizar docs]
    done[Completado]
        d1[Deploy v2.0]
        d2[Fix bug critico]
```

### Bug Tracking

```mermaid
kanban
    new[Nuevos]
        bug1[BUG-001: Login falla en Safari]
        bug2[BUG-002: Timeout en API]
        bug3[BUG-003: CSS roto en mobile]
    triaged[Triaged]
        bug4[BUG-004: Memory leak]
        bug5[BUG-005: Error 500 esporadico]
    fixing[En Reparacion]
        bug6[BUG-006: Datos duplicados]
    testing[Verificando]
        bug7[BUG-007: Encoding incorrecto]
    closed[Cerrados]
        bug8[BUG-008: Typo en UI]
        bug9[BUG-009: Link roto]
```

### Recruitment Pipeline

```mermaid
kanban
    applied[Aplicados]
        c1[Juan Perez - Frontend]
        c2[Maria Garcia - Backend]
        c3[Pedro Lopez - DevOps]
    screening[Screening]
        c4[Ana Martinez - Full Stack]
        c5[Carlos Ruiz - QA]
    interview[Entrevistas]
        c6[Laura Sanchez - Frontend]
    offer[Oferta]
        c7[Diego Torres - Backend]
    hired[Contratados]
        c8[Sofia Morales - DevOps]
```

### Content Pipeline

```mermaid
kanban
    ideas[Ideas]
        a1[Tutorial de Docker]
        a2[Guia de Git avanzado]
        a3[Intro a Kubernetes]
    writing[Escribiendo]
        a4[10 Tips de TypeScript]
        a5[React Hooks explicados]
    editing[Editando]
        a6[Patrones de diseno JS]
    review[Revision]
        a7[Testing con Jest]
    published[Publicado]
        a8[Intro a Node.js]
        a9[CSS Grid tutorial]
```

### Support Tickets

```mermaid
kanban
    new[Nuevos Tickets]
        t1[#1234: No puedo login]
        t2[#1235: Factura incorrecta]
        t3[#1236: App crashea]
    investigating[Investigando]
        t4[#1237: Datos perdidos]
    waiting[Esperando Info]
        t5[#1238: Error de pago]
    resolved[Resueltos]
        t6[#1239: Password reset]
        t7[#1240: Cuenta bloqueada]
```

### Release Planning

```mermaid
kanban
    planned[Planeado]
        f1[Feature: Dark mode]
        f2[Feature: Offline support]
        f3[Feature: Multi-language]
    development[Desarrollo]
        f4[Feature: Export PDF]
        f5[Feature: Sharing]
    staging[Staging]
        f6[Feature: Search]
    production[Produccion]
        f7[Feature: Dashboard v2]
        f8[Feature: New auth flow]
```

### Project Phases

```mermaid
kanban
    planning[Planificacion]
        p1[Definir alcance]
        p2[Estimar tiempos]
        p3[Asignar recursos]
    design[Diseno]
        d1[Wireframes]
        d2[Mockups UI]
    development[Desarrollo]
        dev1[Backend API]
        dev2[Frontend Web]
    testing[Testing]
        test1[Unit tests]
    deployment[Despliegue]
        dep1[Setup production]
```

## Configuracion

### Tema Default

```mermaid
kanban
    col1[Columna 1]
        t1[Tarea 1]
    col2[Columna 2]
        t2[Tarea 2]
```

### Tema Forest

```mermaid
%%{init: {'theme': 'forest'}}%%
kanban
    col1[Columna 1]
        t1[Tarea 1]
    col2[Columna 2]
        t2[Tarea 2]
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
kanban
    col1[Columna 1]
        t1[Tarea 1]
    col2[Columna 2]
        t2[Tarea 2]
```

## Opciones de Configuracion

| Opcion | Descripcion |
|--------|-------------|
| `padding` | Espaciado interno |
| `margin` | Margen entre elementos |

## Comparacion con Otras Herramientas

| Mermaid Kanban | Trello/Jira |
|----------------|-------------|
| Estatico | Interactivo |
| Codigo | Drag & drop |
| Versionable | Base de datos |
| Documentacion | Gestion activa |

## Mejores Practicas

### Limite de WIP

Limitar trabajo en progreso:

```mermaid
kanban
    todo[To Do]
        t1[Task 1]
        t2[Task 2]
        t3[Task 3]
    inprogress[In Progress - Max 3]
        t4[Task 4]
        t5[Task 5]
    done[Done]
        t6[Task 6]
```

### Columnas Claras

Nombres descriptivos de etapas:

```mermaid
kanban
    ready[Ready for Dev]
        t1[Especificado]
    coding[Coding]
        t2[En desarrollo]
    codereview[Code Review]
        t3[Esperando review]
    qa[QA Testing]
        t4[En testing]
    readydeploy[Ready to Deploy]
        t5[Aprobado]
    production[In Production]
        t6[Desplegado]
```

## Tips

1. **Columnas limitadas**: 4-6 columnas maximo
2. **Nombres cortos**: Titulos concisos para columnas y tarjetas
3. **Flujo izquierda-derecha**: De backlog a completado
4. **IDs en tarjetas**: Incluir identificadores cuando sea util
5. **WIP limits**: Indicar limites en nombres de columna
6. **Categorias**: Agrupar tarjetas similares

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Sprints | Visualizar trabajo del sprint |
| Personal | Organizar tareas personales |
| Bugs | Tracking de errores |
| Contenido | Pipeline de publicacion |
| Hiring | Proceso de reclutamiento |
| Releases | Planificacion de versiones |
| Soporte | Gestion de tickets |

## Limitaciones

- No soporta drag & drop (estatico)
- No tiene asignaciones de usuario nativas
- No tiene fechas/deadlines visibles
- No tiene etiquetas/labels
- Diseñado para visualizacion, no gestion activa
