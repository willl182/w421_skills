# Class Diagram - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/classDiagram.html

El diagrama de clases es el bloque de construccion principal del modelado orientado a objetos.

## Sintaxis Basica

```mermaid
classDiagram
    class Animal {
        +String nombre
        +int edad
        +hacerSonido()
        +moverse()
    }
    
    class Perro {
        +String raza
        +ladrar()
    }
    
    Animal <|-- Perro
```

## Definir una Clase

### Forma Explicita

```mermaid
classDiagram
    class Animal
```

### Via Relacion

```mermaid
classDiagram
    Vehicle <|-- Car
```

## Etiquetas de Clase

```mermaid
classDiagram
    class Animal["Animal con espacios"]
    class Car["`Clase con **markdown**`"]
```

## Definir Miembros

### Con Dos Puntos

```mermaid
classDiagram
    class Cuenta
    Cuenta : +String propietario
    Cuenta : +BigDecimal saldo
    Cuenta : +depositar(cantidad)
    Cuenta : +retirar(cantidad)
```

### Con Llaves

```mermaid
classDiagram
    class Cuenta {
        +String propietario
        +BigDecimal saldo
        +depositar(cantidad)
        +retirar(cantidad)
    }
```

### Tipo de Retorno

```mermaid
classDiagram
    class Calculadora {
        +sumar(a, b) int
        +dividir(a, b) float
        +esValido() bool
    }
```

## Tipos Genericos

```mermaid
classDiagram
    class Lista~T~ {
        +agregar(item: T)
        +obtener(index: int) T
    }
    
    class Mapa~K, V~ {
        +put(key: K, value: V)
        +get(key: K) V
    }
```

## Visibilidad

| Simbolo | Significado |
|---------|-------------|
| `+` | Publico |
| `-` | Privado |
| `#` | Protegido |
| `~` | Package/Internal |

```mermaid
classDiagram
    class Ejemplo {
        +atributoPublico
        -atributoPrivado
        #atributoProtegido
        ~atributoPackage
    }
```

## Clasificadores

| Simbolo | Significado |
|---------|-------------|
| `*` | Abstracto |
| `$` | Estatico |

```mermaid
classDiagram
    class Utilidad {
        +String nombre$
        +calcular()* int
        +sumar()$ int
    }
```

## Tipos de Relaciones

```mermaid
classDiagram
    classA <|-- classB : Herencia
    classC *-- classD : Composicion
    classE o-- classF : Agregacion
    classG --> classH : Asociacion
    classI -- classJ : Enlace
    classK ..> classL : Dependencia
    classM ..|> classN : Realizacion
    classO .. classP : Enlace punteado
```

| Tipo | Descripcion |
|------|-------------|
| `<\|--` | Herencia |
| `*--` | Composicion |
| `o--` | Agregacion |
| `-->` | Asociacion |
| `--` | Enlace solido |
| `..>` | Dependencia |
| `..\|>` | Realizacion |
| `..` | Enlace punteado |

## Relaciones Bidireccionales

```mermaid
classDiagram
    Animal <|--|> Planta : simbiosis
```

## Etiquetas en Relaciones

```mermaid
classDiagram
    classA --> classB : etiqueta de relacion
```

## Cardinalidad/Multiplicidad

```mermaid
classDiagram
    Cliente "1" --> "*" Pedido : realiza
    Pedido "1" --> "1..*" LineaPedido : contiene
```

| Notacion | Significado |
|----------|-------------|
| `1` | Solo 1 |
| `0..1` | Cero o uno |
| `1..*` | Uno o mas |
| `*` | Muchos |
| `n` | n (donde n>1) |
| `0..n` | Cero a n |
| `1..n` | Uno a n |

## Lollipop Interfaces

```mermaid
classDiagram
    class Servicio
    class Logger
    
    Logger ()-- Servicio
```

## Namespaces

```mermaid
classDiagram
    namespace MiApp {
        class Usuario
        class Producto
    }
    namespace BaseDatos {
        class Conexion
    }
    Usuario --> Conexion
```

## Anotaciones

```mermaid
classDiagram
    class Figura {
        <<abstract>>
        +dibujar()* void
    }
    
    class Circulo {
        +radio: double
        +dibujar() void
    }
    
    class Dibujable {
        <<interface>>
        +dibujar() void
    }
    
    class Color {
        <<enumeration>>
        ROJO
        VERDE
        AZUL
    }
    
    class UsuarioService {
        <<service>>
    }
```

**Anotaciones disponibles:**
- `<<interface>>`
- `<<abstract>>`
- `<<service>>`
- `<<enumeration>>`

## Notas

```mermaid
classDiagram
    class Usuario
    note "Esta es una nota general"
    note for Usuario "Esta nota es para Usuario"
```

## Direccion del Diagrama

```mermaid
classDiagram
    direction RL
    class A
    class B
    A --> B
```

**Direcciones disponibles:**
- `TB` - Top to Bottom
- `BT` - Bottom to Top
- `LR` - Left to Right
- `RL` - Right to Left

## Comentarios

```mermaid
classDiagram
    %% Este es un comentario
    class Animal
```

## Estilos

### Estilo Individual

```mermaid
classDiagram
    class Animal
    class Perro
    
    style Animal fill:#f9f,stroke:#333,stroke-width:4px
```

### Definir Clases de Estilo

```mermaid
classDiagram
    class Animal:::estiloRosa
    class Perro:::estiloAzul
    
    classDef estiloRosa fill:#f9f,stroke:#333,stroke-width:2px
    classDef estiloAzul fill:#bbf,stroke:#f66,stroke-width:2px
```

### Operador Shorthand :::

```mermaid
classDiagram
    class Animal:::importante
    classDef importante fill:#f00,color:#fff
```

### Clase Default

```mermaid
classDiagram
    classDef default fill:#f9f,stroke:#333,stroke-width:4px
    class A
    class B
```

## Interaccion (Click)

```mermaid
classDiagram
    class Animal
    class Perro
    
    link Animal "https://www.example.com" "Tooltip"
    callback Perro "callbackFunction" "Tooltip"
```

## Configuracion

### Ocultar Caja de Miembros Vacia

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    class Animal
```

## Ejemplo Completo

```mermaid
classDiagram
    class Animal {
        <<abstract>>
        +String nombre
        +int edad
        +hacerSonido()* void
        +moverse() void
    }
    
    class Mamifero {
        +bool tienePelo
        +amamantar() void
    }
    
    class Perro {
        +String raza
        +ladrar() void
        +hacerSonido() void
    }
    
    class Gato {
        +String color
        +maullar() void
        +hacerSonido() void
    }
    
    class Mascota {
        <<interface>>
        +jugar() void
        +alimentar() void
    }
    
    Animal <|-- Mamifero
    Mamifero <|-- Perro
    Mamifero <|-- Gato
    Mascota <|.. Perro
    Mascota <|.. Gato
```
