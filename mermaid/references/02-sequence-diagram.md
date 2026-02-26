# Sequence Diagram - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/sequenceDiagram.html

Un diagrama de secuencia muestra como los procesos operan entre si y en que orden.

## Sintaxis Basica

```mermaid
sequenceDiagram
    participant A as Alice
    participant B as Bob
    A->>B: Hola Bob, como estas?
    B-->>A: Bien, gracias!
    A-)B: Hasta luego!
```

## Participantes

### Definicion Implicita

```mermaid
sequenceDiagram
    Alice->>Bob: Hola
    Bob-->>Alice: Hola
```

### Definicion Explicita con Orden

```mermaid
sequenceDiagram
    participant Bob
    participant Alice
    Alice->>Bob: Hola
```

### Actores

```mermaid
sequenceDiagram
    actor A as Alice
    actor B as Bob
    A->>B: Hola
```

### Tipos de Participantes

```mermaid
sequenceDiagram
    participant P as Participante
    actor A as Actor
```

### Simbolos Especiales

```mermaid
sequenceDiagram
    participant C as Controller
    participant S as Service
    participant D as Database
```

**Simbolos disponibles usando JSON:**
- Boundary
- Control
- Entity
- Database
- Collections
- Queue

## Tipos de Flechas/Mensajes

| Tipo | Descripcion |
|------|-------------|
| `->` | Linea solida sin flecha |
| `-->` | Linea punteada sin flecha |
| `->>` | Linea solida con flecha |
| `-->>` | Linea punteada con flecha |
| `<<->>` | Flecha bidireccional solida (v11.0.0+) |
| `<<-->>` | Flecha bidireccional punteada (v11.0.0+) |
| `-x` | Linea solida con X (error) |
| `--x` | Linea punteada con X |
| `-)` | Linea solida con flecha abierta (async) |
| `--)` | Linea punteada con flecha abierta |

## Activaciones

### Sintaxis Explicita

```mermaid
sequenceDiagram
    Alice->>John: Hola
    activate John
    John-->>Alice: Hola Alice
    deactivate John
```

### Sintaxis Abreviada (+/-)

```mermaid
sequenceDiagram
    Alice->>+John: Hola
    John-->>-Alice: Hola Alice
```

### Activaciones Apiladas

```mermaid
sequenceDiagram
    Alice->>+John: Pregunta 1
    John->>+Database: Query
    Database-->>-John: Resultado
    John-->>-Alice: Respuesta
```

## Notas

```mermaid
sequenceDiagram
    Alice->>Bob: Hola
    Note right of Bob: Bob piensa
    Note left of Alice: Alice espera
    Note over Alice,Bob: Conversacion
```

## Saltos de Linea

```mermaid
sequenceDiagram
    Alice->>Bob: Linea 1<br/>Linea 2
    Note over Alice: Nota con<br/>multiples lineas
```

## Loops

```mermaid
sequenceDiagram
    Alice->>Bob: Hola
    
    loop Cada minuto
        Bob->>Bob: Pensar
    end
```

## Alternativas (Alt/Else)

```mermaid
sequenceDiagram
    Alice->>Bob: Pregunta
    
    alt Esta feliz
        Bob->>Alice: Sonrie
    else Esta triste
        Bob->>Alice: Llora
    end
```

## Opcional (Opt)

```mermaid
sequenceDiagram
    Alice->>Bob: Hola
    
    opt Tiene tiempo
        Bob->>Alice: Responde
    end
```

## Paralelo (Par)

```mermaid
sequenceDiagram
    par Alice a Bob
        Alice->>Bob: Texto 1
    and Alice a John
        Alice->>John: Texto 2
    end
```

### Par Anidado

```mermaid
sequenceDiagram
    par Grupo 1
        Alice->>Bob: msg1
        par Anidado
            Bob->>Carol: msg2
        end
    end
```

## Region Critica

```mermaid
sequenceDiagram
    critical Establecer conexion
        Service->>DB: conectar
    option Timeout
        Service->>Service: reintentar
    option Error
        Service->>Service: log error
    end
```

## Break

```mermaid
sequenceDiagram
    Consumer->>API: Request
    API->>DB: Query
    
    break No hay datos
        API->>Consumer: Error 404
    end
    
    API->>Consumer: Response
```

## Resaltado de Fondo (Rect)

```mermaid
sequenceDiagram
    rect rgb(200, 220, 255)
        Alice->>Bob: Mensaje 1
        Bob->>Alice: Respuesta 1
    end
    
    rect rgba(255, 200, 200, 0.5)
        Alice->>Bob: Mensaje 2
    end
```

## Grupos (Box)

```mermaid
sequenceDiagram
    box Equipo Frontend
        participant A as Alice
        participant B as Bob
    end
    box rgb(33,66,99) Equipo Backend
        participant C as Carlos
    end
    A->>C: Request
    C->>B: Response
```

## Creacion y Destruccion de Actores (v10.3.0+)

```mermaid
sequenceDiagram
    Alice->>Bob: Hola
    create participant Carl
    Alice->>Carl: Hola Carl
    destroy Carl
    Alice-xCarl: Adios
```

## Numeros de Secuencia

```mermaid
sequenceDiagram
    autonumber
    Alice->>John: Hola
    John->>Alice: Hola
    Alice->>John: Como estas?
```

## Menus de Actor

```mermaid
sequenceDiagram
    participant Alice
    participant John
    
    link Alice: Dashboard @ https://dashboard.example.com
    link Alice: Wiki @ https://wiki.example.com
    
    Alice->>John: Hola
```

## Comentarios

```mermaid
sequenceDiagram
    %% Este es un comentario
    Alice->>Bob: Hola
```

## Escape de Caracteres

```mermaid
sequenceDiagram
    Alice->>Bob: I #9829; you
    Bob->>Alice: Me too #59; thanks
```

## Configuracion

### Parametros Disponibles

| Parametro | Descripcion | Default |
|-----------|-------------|---------|
| `mirrorActors` | Renderiza actores arriba y abajo | false |
| `bottomMarginAdj` | Ajusta el margen inferior | 1 |
| `actorFontSize` | Tamano de fuente del actor | 14 |
| `actorFontFamily` | Familia de fuente del actor | "Open Sans" |
| `noteFontSize` | Tamano de fuente de notas | 14 |
| `noteAlign` | Alineacion del texto en notas | center |
| `messageFontSize` | Tamano de fuente de mensajes | 16 |

### Ejemplo de Configuracion

```javascript
mermaid.sequenceConfig = {
  diagramMarginX: 50,
  diagramMarginY: 10,
  boxTextMargin: 5,
  noteMargin: 10,
  messageMargin: 35,
  mirrorActors: true
};
```

## Estilos CSS

### Clases Disponibles

| Clase | Descripcion |
|-------|-------------|
| `.actor` | Estilos para la caja del actor |
| `.actor-line` | Linea vertical del actor |
| `.messageLine0` | Estilos para linea de mensaje solida |
| `.messageLine1` | Estilos para linea de mensaje punteada |
| `.messageText` | Texto en las flechas |
| `.note` | Caja de nota |
| `.noteText` | Texto en las notas |
| `.loopText` | Texto en los loops |
| `.loopLine` | Lineas en los loops |
