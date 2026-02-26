# State Diagram - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/stateDiagram.html

Un diagrama de estados describe el comportamiento de sistemas mostrando estados y transiciones.

## Sintaxis Basica

```mermaid
stateDiagram-v2
    [*] --> Inactivo
    Inactivo --> Activo : activar
    Activo --> Inactivo : desactivar
    Activo --> [*] : terminar
```

## Estados

### Declaracion Simple

```mermaid
stateDiagram-v2
    estado1
```

### Con Keyword State

```mermaid
stateDiagram-v2
    state "Estado de espera" as espera
```

### Con Descripcion (Dos Puntos)

```mermaid
stateDiagram-v2
    estado1 : Este es el estado 1
```

## Transiciones

```mermaid
stateDiagram-v2
    s1 --> s2
```

### Transiciones con Texto

```mermaid
stateDiagram-v2
    s1 --> s2 : Una transicion
```

## Inicio y Fin

```mermaid
stateDiagram-v2
    [*] --> s1
    s1 --> [*]
```

- `[*]` al inicio de una flecha = Estado inicial
- `[*]` al final de una flecha = Estado final

## Estados Compuestos

```mermaid
stateDiagram-v2
    [*] --> Primero
    
    state Primero {
        [*] --> segundo
        segundo --> tercero
        tercero --> [*]
    }
    
    Primero --> Ultimo
    Ultimo --> [*]
```

### Estados Anidados

```mermaid
stateDiagram-v2
    [*] --> Externo
    
    state Externo {
        [*] --> Interno
        state Interno {
            [*] --> profundo
            profundo --> [*]
        }
        Interno --> [*]
    }
    Externo --> [*]
```

### Transiciones entre Estados Compuestos

```mermaid
stateDiagram-v2
    state Primero {
        estado1
    }
    state Segundo {
        estado2
    }
    
    Primero --> Segundo
```

## Choice (Eleccion)

```mermaid
stateDiagram-v2
    state verificar <<choice>>
    
    [*] --> Validando
    Validando --> verificar
    verificar --> Exito : si es valido
    verificar --> Error : si no es valido
    Exito --> [*]
    Error --> [*]
```

## Fork/Join

```mermaid
stateDiagram-v2
    state fork_state <<fork>>
    state join_state <<join>>
    
    [*] --> fork_state
    fork_state --> Estado1
    fork_state --> Estado2
    fork_state --> Estado3
    Estado1 --> join_state
    Estado2 --> join_state
    Estado3 --> join_state
    join_state --> [*]
```

## Notas

```mermaid
stateDiagram-v2
    [*] --> Activo
    Activo --> Inactivo
    
    note right of Activo
        Este es el estado activo
        del sistema
    end note
    
    note left of Inactivo : Nota corta
```

## Concurrencia

```mermaid
stateDiagram-v2
    [*] --> Activo
    
    state Activo {
        [*] --> A1
        A1 --> A2
        A2 --> [*]
        --
        [*] --> B1
        B1 --> B2
        B2 --> [*]
    }
    
    Activo --> [*]
```

## Direccion del Diagrama

```mermaid
stateDiagram-v2
    direction LR
    [*] --> A --> B --> [*]
```

**Direcciones disponibles:**
- `TB` - Top to Bottom (default)
- `LR` - Left to Right
- `RL` - Right to Left
- `BT` - Bottom to Top

## Comentarios

```mermaid
stateDiagram-v2
    %% Este es un comentario
    [*] --> Activo
```

## Estilos con classDef

### Definir Estilos

```mermaid
stateDiagram-v2
    classDef movimiento font-style:italic
    classDef error fill:#f00,color:white,font-weight:bold
```

### Aplicar Estilos con class

```mermaid
stateDiagram-v2
    [*] --> Moviendo
    Moviendo --> Crash
    
    classDef movimiento font-style:italic
    classDef error fill:#f00,color:white
    
    class Moviendo movimiento
    class Crash error
```

### Aplicar Estilos con :::

```mermaid
stateDiagram-v2
    [*] --> Activo:::estiloVerde
    Activo --> [*]
    
    classDef estiloVerde fill:#0f0
```

## Espacios en Nombres de Estados

```mermaid
stateDiagram-v2
    state "Mi estado con espacios" as yswsii
    [*] --> yswsii
    yswsii --> OtroEstado
```

## Ejemplo Completo: Proceso de Pedido

```mermaid
stateDiagram-v2
    [*] --> Pendiente
    
    state Pendiente {
        [*] --> EnCarrito
        EnCarrito --> Confirmado : confirmar
    }
    
    Pendiente --> Procesando : pagar
    
    state Procesando {
        [*] --> Validando
        Validando --> Preparando : valido
        Validando --> Cancelado : invalido
        Preparando --> Enviando
        Enviando --> [*]
    }
    
    state verificar <<choice>>
    Procesando --> verificar
    verificar --> Entregado : exitoso
    verificar --> Fallido : fallido
    
    Entregado --> [*]
    Fallido --> Pendiente : reintentar
    
    note right of Procesando
        Este estado maneja
        todo el proceso de envio
    end note
```

## Ejemplo: Maquina de Estados de Semaforo

```mermaid
stateDiagram-v2
    direction LR
    
    [*] --> Verde
    Verde --> Amarillo : timeout
    Amarillo --> Rojo : timeout
    Rojo --> Verde : timeout
    
    classDef verde fill:#0f0
    classDef amarillo fill:#ff0
    classDef rojo fill:#f00,color:#fff
    
    class Verde verde
    class Amarillo amarillo
    class Rojo rojo
```

## Limitaciones

- classDef no se puede aplicar a estados inicial/final `[*]`
- classDef no se puede aplicar dentro de estados compuestos
