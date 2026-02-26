# Flowchart - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/flowchart.html

Los diagramas de flujo se componen de **nodos** (formas geometricas) y **enlaces** (flechas o lineas).

## Sintaxis Basica

```mermaid
flowchart LR
    A[Inicio] --> B{Decision}
    B -->|Si| C[Hacer algo]
    B -->|No| D[Hacer otra cosa]
    C --> E[Fin]
    D --> E
```

## Direcciones del Diagrama

| Codigo | Direccion |
|--------|-----------|
| `TB` o `TD` | De arriba hacia abajo (Top to Bottom) |
| `BT` | De abajo hacia arriba (Bottom to Top) |
| `LR` | De izquierda a derecha (Left to Right) |
| `RL` | De derecha a izquierda (Right to Left) |

## Formas de Nodos

```mermaid
flowchart TD
    A[Rectangulo]
    B(Rectangulo redondeado)
    C([Estadio])
    D[[Subrutina]]
    E[(Base de datos)]
    F((Circulo))
    G>Asimetrico]
    H{Rombo}
    I{{Hexagono}}
    J[/Paralelogramo/]
    K[\Paralelogramo alt\]
    L[/Trapecio\]
    M[\Trapecio alt/]
    N(((Doble circulo)))
```

## Nueva Sintaxis de Formas (v11.3.0+)

```mermaid
flowchart LR
    A@{ shape: rect, label: "Proceso" }
    B@{ shape: diamond, label: "Decision" }
    C@{ shape: stadium, label: "Terminal" }
    D@{ shape: cylinder, label: "Base de datos" }
    E@{ shape: circle, label: "Inicio" }
```

### Lista Completa de Formas Nuevas

| Nombre Semantico | Nombre Corto | Descripcion | Alias |
|------------------|--------------|-------------|-------|
| Process | `rect` | Proceso estandar | `proc`, `process`, `rectangle` |
| Event | `rounded` | Evento | `event` |
| Terminal Point | `stadium` | Punto terminal | `pill`, `terminal` |
| Decision | `diam` | Decision | `decision`, `diamond`, `question` |
| Prepare Conditional | `hex` | Preparacion | `hexagon`, `prepare` |
| Database | `cyl` | Base de datos | `cylinder`, `database`, `db` |
| Start | `circle` | Inicio | `circ` |
| Document | `doc` | Documento | `document` |
| Multi-Document | `docs` | Multiples documentos | `documents`, `stacked-document` |
| Cloud | `cloud` | Nube | `cloud` |
| Delay | `delay` | Retraso | `half-rounded-rectangle` |
| Extract | `tri` | Triangulo | `extract`, `triangle` |
| Manual Input | `sl-rect` | Entrada manual | `manual-input`, `sloped-rectangle` |
| Display | `curv-trap` | Display | `curved-trapezoid`, `display` |
| Fork/Join | `fork` | Fork o Join | `join` |
| Collate | `hourglass` | Collate | `collate` |
| Comment | `brace` | Comentario | `brace-l`, `comment` |
| Lightning Bolt | `bolt` | Comunicacion | `com-link`, `lightning-bolt` |

## Tipos de Enlaces

```mermaid
flowchart LR
    A --> B
    A --- C
    A -.- D
    A -.-> E
    A ==> F
    A --texto--> G
    A -.texto.-> H
    A ==texto==> I
```

| Sintaxis | Descripcion |
|----------|-------------|
| `-->` | Flecha solida |
| `---` | Linea solida sin flecha |
| `-.-` | Linea punteada sin flecha |
| `-.->` | Flecha punteada |
| `==>` | Flecha gruesa |
| `--texto-->` | Flecha con texto |
| `--o` | Flecha con circulo |
| `--x` | Flecha con X |
| `<-->` | Flecha bidireccional |

## Longitud de Enlaces

Agrega mas guiones para aumentar la longitud:

| Longitud | 1 | 2 | 3 |
|----------|---|---|---|
| Normal | `---` | `----` | `-----` |
| Con flecha | `-->` | `--->` | `---->` |
| Grueso | `===` | `====` | `=====` |
| Grueso con flecha | `==>` | `===>` | `====>` |
| Punteado | `-.-` | `-..-` | `-...-` |
| Punteado con flecha | `-.->` | `-..->` | `-...->` |

## Subgrafos

```mermaid
flowchart TB
    subgraph uno[Primer Grupo]
        A --> B
    end
    subgraph dos[Segundo Grupo]
        C --> D
    end
    B --> C
```

### Direccion en Subgrafos

```mermaid
flowchart LR
    subgraph TOP
        direction TB
        A --> B
    end
    subgraph BOTTOM
        direction LR
        C --> D
    end
    TOP --> BOTTOM
```

## Estilos

### Definir Clases

```mermaid
flowchart LR
    A:::clase1 --> B:::clase2
    classDef clase1 fill:#f9f,stroke:#333,stroke-width:2px
    classDef clase2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff
```

### Estilo Inline

```mermaid
flowchart LR
    A --> B
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,color:white
```

### Clase Default

```mermaid
flowchart LR
    A --> B --> C
    classDef default fill:#f9f,stroke:#333,stroke-width:4px
```

## Enlaces con IDs y Animaciones (v11.10.0+)

```mermaid
flowchart LR
    e1@A --> B
    e1@{ animate: true }
```

### Tipos de Animacion

```mermaid
flowchart LR
    e1@A --> B
    e1@{ animation: fast }
```

## Iconos e Imagenes (v11.3.0+)

### Iconos

```mermaid
flowchart TD
    A@{ icon: "fa:home", label: "Inicio" }
```

### Imagenes

```mermaid
flowchart TD
    A@{ img: "https://example.com/image.png", label: "Imagen", h: 60 }
```

## Markdown en Nodos

```mermaid
flowchart LR
    A["`**Texto en negrita**`"]
    B["`*Texto en italica*`"]
    C["`Linea 1
    Linea 2`"]
```

## Interaccion (Click Events)

```mermaid
flowchart LR
    A --> B --> C
    click A "https://www.github.com" "Ir a GitHub"
    click B callback "Tooltip"
```

## Comentarios

```mermaid
flowchart LR
    %% Este es un comentario
    A --> B
```

## Caracteres Especiales

Para usar caracteres especiales, envuelvelos en comillas:

```mermaid
flowchart LR
    A["Texto con (parentesis)"] --> B["Texto con {llaves}"]
```

### Codigos de Entidad

```mermaid
flowchart LR
    A["#quot;comillas#quot;"] --> B["#35;hashtag"]
```

## Configuracion

### Frontmatter YAML

```mermaid
---
config:
  look: handDrawn
  theme: forest
---
flowchart LR
    A --> B --> C
```

### Algoritmo de Layout

```mermaid
---
config:
  layout: elk
---
flowchart LR
    A --> B --> C
```

**Layouts disponibles:**
- `dagre` (default)
- `elk` (mas opciones avanzadas)

### Configuracion ELK

```yaml
---
config:
  layout: elk
  elk:
    mergeEdges: true
    nodePlacementStrategy: LINEAR_SEGMENTS
---
```
