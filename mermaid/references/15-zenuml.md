# ZenUML (Diagramas de Secuencia) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/zenuml.html

ZenUML es una sintaxis alternativa para crear diagramas de secuencia con un estilo mas cercano a codigo de programacion.

## Sintaxis Basica

```mermaid
zenuml
    Alice->Bob: Hello
    Bob->Alice: Hi!
```

## Comparacion con Sequence Diagram

| sequenceDiagram | zenuml |
|-----------------|--------|
| `A->>B: msg` | `A->B: msg` |
| `A-->>B: msg` | `A->B: msg` (async) |
| `activate A` | Automatico con bloques |
| Sintaxis declarativa | Sintaxis imperativa |

## Participantes

### Declaracion Implicita

```mermaid
zenuml
    Client->Server: request
    Server->Database: query
    Database->Server: result
    Server->Client: response
```

### Declaracion Explicita

```mermaid
zenuml
    @Actor Client
    @Server API
    @Database DB

    Client->API: request
    API->DB: query
    DB->API: result
    API->Client: response
```

### Tipos de Participantes

```mermaid
zenuml
    @Actor User
    @Boundary WebApp
    @Control Controller
    @Entity Database
    @Database DB2

    User->WebApp: click
    WebApp->Controller: handle
    Controller->Database: query
    Controller->DB2: query
```

| Tipo | Descripcion | Icono |
|------|-------------|-------|
| `@Actor` | Usuario/persona | Figura humana |
| `@Boundary` | Interfaz de sistema | Linea con circulo |
| `@Control` | Controlador/logica | Circulo con flecha |
| `@Entity` | Entidad de datos | Circulo subrayado |
| `@Database` | Base de datos | Cilindro |

## Mensajes

### Mensaje Simple

```mermaid
zenuml
    A->B: mensaje
```

### Mensaje con Retorno

```mermaid
zenuml
    A->B: request
    return response
```

### Mensaje Asincrono

```mermaid
zenuml
    A->B: async message
    B->C: process
```

### Self-Message

```mermaid
zenuml
    A->A: self call
```

## Bloques de Activacion

Los bloques `{}` crean activaciones automaticas:

```mermaid
zenuml
    Client->Server: request {
        Server->Database: query {
            Database->Database: process
        }
        return data
    }
    return response
```

## Estructuras de Control

### If/Else

```mermaid
zenuml
    Client->Server: login(user, pass) {
        if (valid) {
            return token
        } else {
            return error
        }
    }
```

### If/Else If/Else

```mermaid
zenuml
    User->System: getStatus {
        if (isAdmin) {
            return fullAccess
        } else if (isMember) {
            return limitedAccess
        } else {
            return guestAccess
        }
    }
```

### While Loop

```mermaid
zenuml
    Client->Server: pollStatus {
        while (processing) {
            Server->Worker: checkProgress
            Worker->Server: status
        }
        return complete
    }
```

### For Each / Loop

```mermaid
zenuml
    API->DB: getUsers {
        forEach (user in users) {
            DB->Cache: cache(user)
        }
        return users
    }
```

### Try/Catch/Finally

```mermaid
zenuml
    Client->API: request {
        try {
            API->DB: query
            return data
        } catch (error) {
            API->Logger: logError
            return errorResponse
        } finally {
            API->Metrics: recordRequest
        }
    }
```

### Par (Paralelo)

```mermaid
zenuml
    Client->Orchestrator: request {
        par {
            Orchestrator->ServiceA: callA
            Orchestrator->ServiceB: callB
            Orchestrator->ServiceC: callC
        }
        return aggregatedResult
    }
```

### Opt (Opcional)

```mermaid
zenuml
    User->System: action {
        opt (needsConfirmation) {
            System->User: confirm?
            User->System: yes
        }
        return success
    }
```

### Break

```mermaid
zenuml
    Client->Server: process {
        loop (items) {
            Server->Validator: validate
            if (invalid) {
                break
            }
            Server->Processor: process
        }
    }
```

## Comentarios y Notas

### Comentarios

```mermaid
zenuml
    // Este es un comentario
    A->B: message

    /* Comentario
       multilinea */
    B->C: another
```

### Notas

```mermaid
zenuml
    A->B: request
    @note left of A: Nota a la izquierda
    B->A: response
    @note right of B: Nota a la derecha
    @note over A,B: Nota sobre ambos
```

## Ejemplos Completos

### Autenticacion OAuth

```mermaid
zenuml
    @Actor User
    @Boundary App
    @Control AuthServer
    @Database UserDB

    User->App: login {
        App->AuthServer: authorize {
            AuthServer->UserDB: validateCredentials {
                if (valid) {
                    return user
                } else {
                    return null
                }
            }
            if (user != null) {
                AuthServer->AuthServer: generateToken
                return token
            } else {
                return error
            }
        }
        if (token) {
            App->App: saveSession
            return dashboard
        } else {
            return loginError
        }
    }
```

### API REST con Cache

```mermaid
zenuml
    @Actor Client
    @Boundary Gateway
    @Control API
    @Database Cache
    @Database DB

    Client->Gateway: GET /users/123 {
        Gateway->API: getUser(123) {
            API->Cache: get(user:123) {
                if (exists) {
                    return cachedUser
                }
            }
            if (cachedUser == null) {
                API->DB: SELECT * FROM users WHERE id=123
                DB->API: userData
                API->Cache: set(user:123, userData)
            }
            return user
        }
        return response
    }
```

### Proceso de Checkout

```mermaid
zenuml
    @Actor Customer
    @Boundary WebStore
    @Control OrderService
    @Control PaymentService
    @Control InventoryService
    @Database OrderDB

    Customer->WebStore: checkout(cart) {
        WebStore->InventoryService: checkAvailability(items) {
            forEach (item in items) {
                InventoryService->InventoryService: validateStock
            }
            if (allAvailable) {
                return true
            } else {
                return unavailableItems
            }
        }

        if (available) {
            WebStore->PaymentService: processPayment(amount) {
                try {
                    PaymentService->PaymentService: validateCard
                    PaymentService->PaymentService: charge
                    return transactionId
                } catch (error) {
                    return paymentError
                }
            }

            if (paymentSuccess) {
                WebStore->OrderService: createOrder(cart, transactionId) {
                    OrderService->OrderDB: INSERT order
                    par {
                        OrderService->InventoryService: reserveItems
                        OrderService->OrderService: sendConfirmationEmail
                    }
                    return orderId
                }
                return orderConfirmation
            } else {
                return paymentFailed
            }
        } else {
            return itemsUnavailable
        }
    }
```

### Microservicios con Saga

```mermaid
zenuml
    @Boundary API
    @Control Saga
    @Control OrderSvc
    @Control PaymentSvc
    @Control ShippingSvc

    API->Saga: startSaga(order) {
        try {
            Saga->OrderSvc: createOrder {
                return orderId
            }

            Saga->PaymentSvc: processPayment(orderId) {
                if (success) {
                    return paymentId
                } else {
                    throw PaymentError
                }
            }

            Saga->ShippingSvc: scheduleShipping(orderId) {
                return trackingId
            }

            return sagaComplete
        } catch (error) {
            // Compensating transactions
            Saga->ShippingSvc: cancelShipping
            Saga->PaymentSvc: refundPayment
            Saga->OrderSvc: cancelOrder
            return sagaFailed
        }
    }
```

## Configuracion

### Tema

```mermaid
%%{init: {'theme': 'forest'}}%%
zenuml
    A->B: message
    B->A: response
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
zenuml
    A->B: message
    B->A: response
```

## Comparacion: ZenUML vs sequenceDiagram

### sequenceDiagram

```mermaid
sequenceDiagram
    participant A as Client
    participant B as Server

    A->>B: request
    activate B
    B->>B: process
    B-->>A: response
    deactivate B
```

### ZenUML equivalente

```mermaid
zenuml
    @Client A
    @Server B

    A->B: request {
        B->B: process
        return response
    }
```

## Ventajas de ZenUML

| Ventaja | Descripcion |
|---------|-------------|
| Sintaxis familiar | Similar a lenguajes de programacion |
| Activacion automatica | Bloques `{}` manejan activaciones |
| Estructuras de control | if/else, while, try/catch nativos |
| Menos verboso | Requiere menos lineas de codigo |
| Legible | Facil de leer como pseudocodigo |

## Tips y Mejores Practicas

1. **Usar bloques**: Las llaves `{}` clarifican el alcance
2. **Participantes tipados**: Usar `@Actor`, `@Database`, etc.
3. **Estructuras de control**: Aprovechar if/else, loops nativos
4. **Comentarios**: Documentar logica compleja
5. **Nombres descriptivos**: Mensajes que expliquen la accion
6. **Return explicitos**: Usar `return` para respuestas
7. **Manejo de errores**: Usar try/catch para flujos de error
