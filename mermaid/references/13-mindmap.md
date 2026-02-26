# Mindmap (Mapa Mental) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/mindmap.html

Los mapas mentales organizan informacion en una estructura jerarquica visual, partiendo de un concepto central y ramificandose en ideas relacionadas.

## Sintaxis Basica

La indentacion define la jerarquia:

```mermaid
mindmap
    root((Tema Central))
        Rama 1
            Subrama 1.1
            Subrama 1.2
        Rama 2
            Subrama 2.1
        Rama 3
```

## Estructura General

```
mindmap
    root[Forma](Texto)
        Hijo 1
            Nieto 1
        Hijo 2
```

La **indentacion** (espacios o tabs) determina el nivel jerarquico.

## Formas de Nodos

### Formas Disponibles

```mermaid
mindmap
    root((Formas de Nodos))
        Default
        Cuadrado[Cuadrado]
        Redondeado(Redondeado)
        Circulo((Circulo))
        Bang))Bang((
        Nube)Nube(
        Hexagono{{Hexagono}}
```

### Tabla de Formas

| Sintaxis | Forma | Uso Tipico |
|----------|-------|------------|
| `texto` | Default (rectangulo) | Nodos generales |
| `[texto]` | Cuadrado | Tareas, items |
| `(texto)` | Redondeado | Procesos, pasos |
| `((texto))` | Circulo | Nodo central, inicio |
| `))texto((` | Bang/Explosion | Enfasis, alerta |
| `)texto(` | Nube | Ideas, conceptos |
| `{{texto}}` | Hexagono | Decisiones |

## Nodo Raiz

El nodo raiz es el concepto central:

### Circulo (Comun para raiz)

```mermaid
mindmap
    root((Mi Idea Central))
        Concepto 1
        Concepto 2
```

### Otras Formas de Raiz

```mermaid
mindmap
    root[Proyecto]
        Fase 1
        Fase 2
```

```mermaid
mindmap
    root)Cloud Project(
        Infraestructura
        Aplicaciones
```

## Jerarquias

### Multiples Niveles

```mermaid
mindmap
    root((Empresa))
        Departamento 1
            Equipo A
                Miembro 1
                Miembro 2
            Equipo B
        Departamento 2
            Equipo C
            Equipo D
                Miembro 3
```

### Ramas Paralelas

```mermaid
mindmap
    root((Centro))
        Norte
            NE
            NO
        Sur
            SE
            SO
        Este
        Oeste
```

## Iconos

### Sintaxis de Iconos

```mermaid
mindmap
    root((Proyecto))
        ::icon(fa fa-book)
        Documentacion
            Guias
            APIs
        Desarrollo
            ::icon(fa fa-code)
            Frontend
            Backend
```

### Iconos Font Awesome

```mermaid
mindmap
    root((Tech Stack))
        Frontend
            ::icon(fa fa-desktop)
            React
            Vue
        Backend
            ::icon(fa fa-server)
            Node.js
            Python
        Database
            ::icon(fa fa-database)
            PostgreSQL
            MongoDB
```

**Nota**: Los iconos requieren que Font Awesome este cargado en la pagina.

## Markdown en Nodos

### Texto con Formato

```mermaid
mindmap
    root((Mindmap))
        Texto **negrita**
        Texto *italica*
        Texto normal
```

### Multiples Lineas

```mermaid
mindmap
    root((Ideas))
        Primera linea
        Segunda linea
        Tercera linea
```

## Clases y Estilos

### Aplicar Clases

```mermaid
mindmap
    root((Central))
        Importante:::destacado
        Normal
        Urgente:::urgente

    classDef destacado fill:#f9f,stroke:#333,stroke-width:2px
    classDef urgente fill:#f00,color:#fff
```

## Ejemplos por Categoria

### Planificacion de Proyecto

```mermaid
mindmap
    root((Proyecto Web))
        Planificacion
            Requisitos
            Cronograma
            Presupuesto
        Diseno
            UX Research
            Wireframes
            Mockups
            Prototipo
        Desarrollo
            Frontend
                HTML/CSS
                JavaScript
                React
            Backend
                API REST
                Base de datos
                Autenticacion
        Testing
            Unitarios
            Integracion
            E2E
        Despliegue
            CI/CD
            Hosting
            Monitoreo
```

### Estructura de Curso

```mermaid
mindmap
    root((Curso JavaScript))
        Fundamentos
            Variables
            Tipos de datos
            Operadores
            Control de flujo
        Funciones
            Declaracion
            Arrow functions
            Callbacks
            Closures
        Objetos
            Propiedades
            Metodos
            Prototipos
            Clases
        Asincronia
            Callbacks
            Promesas
            Async/Await
        DOM
            Seleccion
            Eventos
            Manipulacion
```

### Brainstorming

```mermaid
mindmap
    root))Nuevas Features((
        Usuarios
            Perfil mejorado
            Preferencias
            Notificaciones
        Contenido
            Editor WYSIWYG
            Markdown
            Media embebida
        Social
            Comentarios
            Likes
            Compartir
        Monetizacion
            Suscripciones
            Anuncios
            Premium
```

### Resolucion de Problemas

```mermaid
mindmap
    root((Bug en Produccion))
        Sintomas
            Error 500
            Timeout
            Datos incorrectos
        Posibles Causas
            Base de datos
                Conexion
                Query lenta
            Codigo
                Null pointer
                Race condition
            Infraestructura
                Memoria
                CPU
        Diagnostico
            Logs
            Metricas
            Tracing
        Solucion
            Hotfix
            Rollback
            Escalado
```

### Organizacion Personal

```mermaid
mindmap
    root((Mi Semana))
        Lunes
            Reuniones
            Planificacion
        Martes
            Desarrollo
            Code Review
        Miercoles
            Desarrollo
            Testing
        Jueves
            Documentacion
            Meetings
        Viernes
            Retrospectiva
            Aprendizaje
```

### Stack Tecnologico

```mermaid
mindmap
    root((Full Stack))
        Frontend
            React
                Hooks
                Context
                Redux
            Estilos
                CSS Modules
                Tailwind
                Styled Components
        Backend
            Node.js
                Express
                Fastify
            Python
                FastAPI
                Django
        Database
            SQL
                PostgreSQL
                MySQL
            NoSQL
                MongoDB
                Redis
        DevOps
            Containers
                Docker
                Kubernetes
            CI/CD
                GitHub Actions
                Jenkins
            Cloud
                AWS
                GCP
```

### Analisis FODA

```mermaid
mindmap
    root((Analisis FODA))
        Fortalezas
            Equipo experimentado
            Tecnologia moderna
            Buena reputacion
        Oportunidades
            Mercado en crecimiento
            Nuevas tecnologias
            Expansion regional
        Debilidades
            Recursos limitados
            Falta de marketing
            Deuda tecnica
        Amenazas
            Competencia fuerte
            Cambios regulatorios
            Crisis economica
```

## Configuracion

### Tema Default

```mermaid
mindmap
    root((Default))
        Nodo 1
        Nodo 2
```

### Tema Forest

```mermaid
%%{init: {'theme': 'forest'}}%%
mindmap
    root((Forest))
        Nodo 1
        Nodo 2
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
mindmap
    root((Dark))
        Nodo 1
        Nodo 2
```

### Personalizacion

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ff6b6b', 'primaryTextColor': '#fff'}}}%%
mindmap
    root((Personalizado))
        Nodo 1
        Nodo 2
```

## Opciones de Configuracion

| Opcion | Descripcion |
|--------|-------------|
| `maxTextWidth` | Ancho maximo del texto |
| `curve` | Tipo de curva para las ramas |

## Tips y Mejores Practicas

1. **Concepto central claro**: El root debe ser el tema principal
2. **Jerarquia logica**: Organizar de general a especifico
3. **Balance visual**: Distribuir ramas uniformemente
4. **Textos concisos**: Palabras clave, no oraciones largas
5. **Usar formas con proposito**: Diferentes formas para diferentes tipos de nodos
6. **Limitar profundidad**: Maximo 4-5 niveles para legibilidad
7. **Colores consistentes**: Usar clases para categorizar

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Brainstorming | Generar y organizar ideas |
| Notas de estudio | Resumir temas complejos |
| Planificacion | Estructurar proyectos |
| Presentaciones | Visualizar conceptos |
| Documentacion | Mostrar estructuras |
| Toma de decisiones | Evaluar opciones |
