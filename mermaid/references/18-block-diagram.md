# Block Diagram (Diagrama de Bloques) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/block.html

Los diagramas de bloques permiten crear layouts estructurados con bloques anidados, ideal para arquitecturas, diagramas de sistema y estructuras organizacionales.

## Sintaxis Basica

```mermaid
block-beta
    A["Bloque A"]
    B["Bloque B"]
    C["Bloque C"]
```

## Estructura General

```
block-beta
    columns N
    bloque["Texto"]
    bloque:N  %% Ocupa N columnas
    block:nombre
        %% bloques anidados
    end
```

## Columnas

### Definir Columnas

```mermaid
block-beta
    columns 3
    A B C
    D E F
```

### Bloques que Ocupan Multiples Columnas

```mermaid
block-beta
    columns 3
    A:3
    B C D
    E:2 F
```

## Formas de Bloques

### Diferentes Formas

```mermaid
block-beta
    columns 4
    A["Cuadrado"]
    B("Redondeado")
    C(("Circulo"))
    D{"Rombo"}
```

```mermaid
block-beta
    columns 4
    E[/"Paralelogramo"/]
    F[\"Paralelo Alt"\]
    G[/"Trapecio"\]
    H(["Estadio"])
```

### Tabla de Formas

| Sintaxis | Forma |
|----------|-------|
| `["texto"]` | Rectangulo |
| `("texto")` | Redondeado |
| `(("texto"))` | Circulo |
| `{"texto"}` | Rombo |
| `[/"texto"/]` | Paralelogramo |
| `[\"texto"\]` | Paralelogramo alt |
| `[/"texto"\]` | Trapecio |
| `(["texto"])` | Estadio |
| `[["texto"]]` | Subrutina |
| `[("texto")]` | Cilindro |
| `{{"texto"}}` | Hexagono |

## Bloques Anidados

### Bloque Contenedor

```mermaid
block-beta
    columns 2
    block:grupo1
        A B
    end
    C
```

### Multiples Niveles

```mermaid
block-beta
    columns 3
    block:outer:2
        columns 2
        A B
        block:inner:2
            C D
        end
    end
    E
```

## Conexiones

### Conexiones Basicas

```mermaid
block-beta
    columns 3
    A --> B --> C
```

### Conexiones con Etiquetas

```mermaid
block-beta
    columns 2
    A -- "flujo" --> B
    C -- "datos" --> D
```

### Tipos de Flechas

```mermaid
block-beta
    columns 2
    A --> B
    C --- D
    E -.- F
    G ==> H
```

## Espacios

### Espacio en Blanco

```mermaid
block-beta
    columns 3
    A space B
    space C space
```

### Espacio que Ocupa Columnas

```mermaid
block-beta
    columns 4
    A space:2 B
    C D E F
```

## Estilos

### Clases de Estilo

```mermaid
block-beta
    columns 2
    A:::importante
    B:::normal
    
    classDef importante fill:#f96,stroke:#333
    classDef normal fill:#9f9,stroke:#333
```

### Estilo por Bloque

```mermaid
block-beta
    columns 2
    A["Destacado"]
    B["Normal"]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
```

## Ejemplos por Categoria

### Arquitectura de Sistema

```mermaid
block-beta
    columns 3
    
    block:frontend:3
        columns 3
        WebApp["Web App"] MobileApp["Mobile App"] AdminPanel["Admin Panel"]
    end
    
    block:api:3
        columns 1
        Gateway["API Gateway"]
    end
    
    block:services:3
        columns 3
        AuthService["Auth"] UserService["Users"] OrderService["Orders"]
    end
    
    block:data:3
        columns 2
        PostgreSQL[("PostgreSQL")] Redis[("Redis")]
    end
    
    frontend --> api
    api --> services
    services --> data
```

### Flujo de CI/CD

```mermaid
block-beta
    columns 5
    
    Code["Codigo"] --> Build["Build"] --> Test["Test"] --> Stage["Staging"] --> Prod["Produccion"]
    
    block:tools:5
        columns 5
        Git["Git"] Docker["Docker"] Jest["Jest"] K8s["K8s Dev"] K8sProd["K8s Prod"]
    end
```

### Organizacion de Equipo

```mermaid
block-beta
    columns 5
    
    block:leadership:5
        CEO["CEO"]
    end
    
    block:directors:5
        columns 3
        CTO["CTO"] CFO["CFO"] COO["COO"]
    end
    
    block:teams:5
        columns 5
        Dev["Desarrollo"] QA["QA"] Finance["Finanzas"] Ops["Operaciones"] HR["RRHH"]
    end
```

### Stack Tecnologico

```mermaid
block-beta
    columns 4
    
    block:presentation:4
        columns 4
        React["React"] Vue["Vue"] Angular["Angular"] Svelte["Svelte"]
    end
    
    block:api:4
        columns 3
        Node["Node.js"] Python["Python"] Go["Go"]
    end
    
    block:data:4
        columns 4
        Postgres[("PostgreSQL")] Mongo[("MongoDB")] Redis[("Redis")] Elastic[("Elasticsearch")]
    end
    
    block:infra:4
        columns 3
        Docker["Docker"] K8s["Kubernetes"] AWS["AWS"]
    end
```

### Proceso de Desarrollo

```mermaid
block-beta
    columns 6
    
    Plan["Planificacion"]:1
    Code["Desarrollo"]:1
    Review["Code Review"]:1
    Test["Testing"]:1
    Deploy["Deploy"]:1
    Monitor["Monitoreo"]:1
    
    block:details:6
        columns 6
        Jira["Jira"] Git["Git/GitHub"] PR["Pull Request"] Jest["Jest/Cypress"] ArgoCD["ArgoCD"] Datadog["Datadog"]
    end
```

### Arquitectura de Microservicios

```mermaid
block-beta
    columns 5
    
    block:clients:5
        columns 3
        Web["Web"] Mobile["Mobile"] IoT["IoT"]
    end
    
    block:gateway:5
        columns 1
        Kong["Kong API Gateway"]
    end
    
    block:services:5
        columns 5
        Users["Users"] Products["Products"] Orders["Orders"] Payments["Payments"] Notifications["Notifications"]
    end
    
    block:messaging:5
        columns 1
        Kafka["Apache Kafka"]
    end
    
    block:databases:5
        columns 5
        UsersDB[("Users DB")] ProductsDB[("Products DB")] OrdersDB[("Orders DB")] PaymentsDB[("Payments DB")] space
    end
```

### Dashboard de Metricas

```mermaid
block-beta
    columns 4
    
    block:header:4
        columns 1
        Title["Dashboard de Metricas"]
    end
    
    block:kpis:4
        columns 4
        Revenue["Revenue\n$1.2M"] Users["Usuarios\n50K"] Conversion["Conversion\n3.5%"] NPS["NPS\n72"]
    end
    
    block:charts:4
        columns 2
        Chart1["Ventas Mensuales"] Chart2["Trafico por Canal"]
    end
    
    block:tables:4
        columns 2
        Table1["Top Productos"] Table2["Ultimas Transacciones"]
    end
```

### Red de Computadoras

```mermaid
block-beta
    columns 5
    
    block:internet:5
        columns 1
        Internet(("Internet"))
    end
    
    block:perimeter:5
        columns 3
        Firewall{"Firewall"} space:2
    end
    
    block:dmz:5
        columns 2
        WebServer["Web Server"] MailServer["Mail Server"]
    end
    
    block:internal:5
        columns 4
        AppServer1["App Server 1"] AppServer2["App Server 2"] DBPrimary[("DB Primary")] DBReplica[("DB Replica")]
    end
```

## Configuracion

### Tema

```mermaid
%%{init: {'theme': 'forest'}}%%
block-beta
    columns 3
    A B C
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
block-beta
    columns 3
    A B C
    D E F
```

## Opciones de Configuracion

| Opcion | Descripcion |
|--------|-------------|
| `padding` | Espaciado interno |
| `margin` | Margen externo |

## Comparacion con Flowchart

| Caracteristica | Block Diagram | Flowchart |
|---------------|---------------|-----------|
| Layout | Grid-based | Graph-based |
| Columnas | Explicitas | Automatico |
| Anidamiento | Nativo | Subgrafos |
| Conexiones | Simples | Multiples tipos |
| Uso principal | Arquitectura, layouts | Flujos, procesos |

## Tips y Mejores Practicas

1. **Definir columnas primero**: Establecer estructura base con `columns N`
2. **Usar bloques anidados**: Para agrupar componentes relacionados
3. **Spans para enfasis**: Usar `:N` para bloques importantes
4. **Espacios para layout**: Usar `space` para alineacion
5. **Formas con proposito**: Diferentes formas para diferentes tipos de componentes
6. **Estilos consistentes**: Usar clases para categorizar

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Arquitecturas | Diagramas de sistema |
| Layouts | Estructuras de UI |
| Organizacion | Organigramas |
| Dashboards | Mockups de paneles |
| Redes | Topologias de red |
| Stacks | Pilas tecnologicas |
