# Entity Relationship Diagram (ERD) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/entityRelationshipDiagram.html

Los diagramas ER describen entidades y sus relaciones en bases de datos.

## Sintaxis Basica

```mermaid
erDiagram
    CLIENTE ||--o{ PEDIDO : realiza
    PEDIDO ||--|{ LINEA_PEDIDO : contiene
    PRODUCTO ||--o{ LINEA_PEDIDO : incluido_en
```

## Estructura de una Declaracion

```
PRIMERA_ENTIDAD [relacion] SEGUNDA_ENTIDAD : etiqueta
```

## Entidades con Atributos

```mermaid
erDiagram
    CLIENTE {
        int id PK
        string nombre
        string email UK
        date fecha_registro
    }
    
    PEDIDO {
        int id PK
        int cliente_id FK
        date fecha
        decimal total
    }
    
    CLIENTE ||--o{ PEDIDO : realiza
```

## Sintaxis de Atributos

```
ENTIDAD {
    tipo nombre [clave] ["comentario"]
}
```

### Tipos de Claves

| Clave | Descripcion |
|-------|-------------|
| `PK` | Primary Key |
| `FK` | Foreign Key |
| `UK` | Unique Key |

### Multiples Claves

```mermaid
erDiagram
    PRODUCTO {
        int id PK
        string sku UK
        int categoria_id FK
        string nombre
    }
```

### Comentarios en Atributos

```mermaid
erDiagram
    USUARIO {
        int id PK "Identificador unico"
        string email UK "Email del usuario"
        string password "Contrasena encriptada"
    }
```

## Cardinalidades

### Tabla de Cardinalidades

| Valor Izq | Valor Der | Significado |
|-----------|-----------|-------------|
| `\|o` | `o\|` | Cero o uno |
| `\|\|` | `\|\|` | Exactamente uno |
| `}o` | `o{` | Cero o mas |
| `}\|` | `\|{` | Uno o mas |

### Alias de Cardinalidades

| Valor | Alias | Significado |
|-------|-------|-------------|
| `\|o` / `o\|` | `one or zero`, `zero or one` | Cero o uno |
| `}\|` / `\|{` | `one or more`, `one or many`, `many(1)`, `1+` | Uno o mas |
| `}o` / `o{` | `zero or more`, `zero or many`, `many(0)`, `0+` | Cero o mas |
| `\|\|` | `only one`, `1` | Exactamente uno |

## Tipos de Relaciones

### Identificadora (Linea Solida)

```mermaid
erDiagram
    PERSONA ||--o{ CONDUCTOR_NOMBRADO : es
    CARRO ||--o{ CONDUCTOR_NOMBRADO : permite
```

### No Identificadora (Linea Punteada)

```mermaid
erDiagram
    PERSONA }|..|{ CARRO : conduce
```

| Valor | Alias | Significado |
|-------|-------|-------------|
| `--` | `to` | Identificadora |
| `..` | `optionally to` | No identificadora |

## Alias de Entidades

```mermaid
erDiagram
    p[Persona] {
        string nombre
    }
    c[Carro] {
        string modelo
    }
    p ||--o{ c : posee
```

## Texto Unicode

```mermaid
erDiagram
    PERSONA {
        string nombre "nombre completo"
    }
```

## Markdown en Texto

```mermaid
erDiagram
    CLIENTE["**Cliente**"] {
        int id
        string nombre
    }
```

## Direccion del Diagrama

```mermaid
erDiagram
    direction LR
    A ||--o{ B : tiene
    B ||--o{ C : contiene
```

**Direcciones disponibles:**
- `TB` - Top to Bottom (default)
- `BT` - Bottom to Top
- `LR` - Left to Right
- `RL` - Right to Left

## Estilos

### Estilo Individual

```mermaid
erDiagram
    CLIENTE {
        int id
    }
    PEDIDO {
        int id
    }
    CLIENTE ||--o{ PEDIDO : realiza
    
    style CLIENTE fill:#f9f,stroke:#333,stroke-width:2px
```

### Clases de Estilo

```mermaid
erDiagram
    CLIENTE:::importante {
        int id
    }
    PEDIDO {
        int id
    }
    CLIENTE ||--o{ PEDIDO : realiza
    
    classDef importante fill:#f00,color:#fff
```

### Clase Default

```mermaid
erDiagram
    classDef default fill:#f9f,stroke:#333,stroke-width:4px
    
    ENTIDAD1 {
        int id
    }
    ENTIDAD2 {
        int id
    }
```

## Configuracion de Layout

### Usando ELK

```mermaid
---
config:
  layout: elk
---
erDiagram
    CLIENTE ||--o{ PEDIDO : realiza
    PEDIDO ||--|{ LINEA_PEDIDO : contiene
```

## Ejemplo Completo: E-commerce

```mermaid
erDiagram
    CLIENTE {
        int id PK
        string nombre
        string email UK
        string telefono
        date fecha_registro
    }
    
    DIRECCION {
        int id PK
        int cliente_id FK
        string calle
        string ciudad
        string codigo_postal
        string pais
    }
    
    PEDIDO {
        int id PK
        int cliente_id FK
        int direccion_id FK
        date fecha
        string estado
        decimal total
    }
    
    LINEA_PEDIDO {
        int id PK
        int pedido_id FK
        int producto_id FK
        int cantidad
        decimal precio_unitario
    }
    
    PRODUCTO {
        int id PK
        int categoria_id FK
        string nombre
        string descripcion
        decimal precio
        int stock
    }
    
    CATEGORIA {
        int id PK
        string nombre
        string descripcion
    }
    
    CLIENTE ||--o{ DIRECCION : tiene
    CLIENTE ||--o{ PEDIDO : realiza
    DIRECCION ||--o{ PEDIDO : envia_a
    PEDIDO ||--|{ LINEA_PEDIDO : contiene
    PRODUCTO ||--o{ LINEA_PEDIDO : incluido_en
    CATEGORIA ||--o{ PRODUCTO : agrupa
```

## Ejemplo: Sistema de Blog

```mermaid
erDiagram
    USUARIO {
        int id PK
        string username UK
        string email UK
        string password
        date creado_en
    }
    
    POST {
        int id PK
        int autor_id FK
        string titulo
        text contenido
        date publicado_en
        boolean publicado
    }
    
    COMENTARIO {
        int id PK
        int post_id FK
        int usuario_id FK
        text contenido
        date creado_en
    }
    
    ETIQUETA {
        int id PK
        string nombre UK
    }
    
    POST_ETIQUETA {
        int post_id PK,FK
        int etiqueta_id PK,FK
    }
    
    USUARIO ||--o{ POST : escribe
    USUARIO ||--o{ COMENTARIO : comenta
    POST ||--o{ COMENTARIO : tiene
    POST ||--o{ POST_ETIQUETA : tiene
    ETIQUETA ||--o{ POST_ETIQUETA : aplica_a
```
