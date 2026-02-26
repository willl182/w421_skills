# C4 Diagram (Diagrama C4) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/c4.html

Los diagramas C4 (Context, Containers, Components, Code) son un enfoque para visualizar la arquitectura de software en diferentes niveles de abstraccion.

## Niveles C4

| Nivel | Nombre | Proposito |
|-------|--------|-----------|
| 1 | Context | Vision general del sistema y actores externos |
| 2 | Container | Aplicaciones y almacenes de datos |
| 3 | Component | Componentes dentro de contenedores |
| 4 | Code | Diagramas de clases/codigo (usar classDiagram) |

## C4Context (Nivel 1 - Contexto)

Muestra el sistema en su entorno, con usuarios y sistemas externos.

### Sintaxis Basica

```mermaid
C4Context
    title Diagrama de Contexto - Sistema de E-commerce

    Person(cliente, "Cliente", "Usuario que compra productos")
    Person(admin, "Administrador", "Gestiona productos y pedidos")

    System(ecommerce, "Sistema E-commerce", "Permite comprar productos online")

    System_Ext(pagos, "Sistema de Pagos", "Procesa pagos con tarjeta")
    System_Ext(envios, "Sistema de Envios", "Gestiona logistica de envios")

    Rel(cliente, ecommerce, "Navega y compra")
    Rel(admin, ecommerce, "Administra")
    Rel(ecommerce, pagos, "Procesa pagos", "HTTPS/API")
    Rel(ecommerce, envios, "Solicita envios", "HTTPS/API")
```

### Elementos de Contexto

| Elemento | Sintaxis | Uso |
|----------|----------|-----|
| `Person` | `Person(id, "nombre", "descripcion")` | Usuario del sistema |
| `Person_Ext` | `Person_Ext(id, "nombre", "desc")` | Usuario externo |
| `System` | `System(id, "nombre", "descripcion")` | Sistema principal |
| `System_Ext` | `System_Ext(id, "nombre", "desc")` | Sistema externo |
| `SystemDb` | `SystemDb(id, "nombre", "desc")` | Base de datos |
| `SystemDb_Ext` | `SystemDb_Ext(id, "nombre", "desc")` | BD externa |
| `SystemQueue` | `SystemQueue(id, "nombre", "desc")` | Cola de mensajes |
| `SystemQueue_Ext` | `SystemQueue_Ext(id, "nombre")` | Cola externa |

### Ejemplo Completo de Contexto

```mermaid
C4Context
    title Sistema Bancario - Diagrama de Contexto

    Enterprise_Boundary(banco, "Banco XYZ") {
        Person(cliente, "Cliente Bancario", "Usuario con cuentas en el banco")
        Person(soporte, "Agente de Soporte", "Atiende consultas de clientes")

        System(banca, "Sistema de Banca Online", "Permite operaciones bancarias via web/app")
    }

    System_Ext(core, "Core Bancario", "Sistema legacy de operaciones")
    System_Ext(swift, "Red SWIFT", "Transferencias internacionales")
    System_Ext(email, "Sistema de Email", "Envia notificaciones")

    Rel(cliente, banca, "Usa", "HTTPS")
    Rel(soporte, banca, "Consulta informacion")
    Rel(banca, core, "Lee/Escribe", "API REST")
    Rel(banca, swift, "Envia transferencias", "SWIFT")
    Rel(banca, email, "Envia emails", "SMTP")
```

## C4Container (Nivel 2 - Contenedores)

Muestra las aplicaciones y almacenes de datos dentro del sistema.

### Sintaxis Basica

```mermaid
C4Container
    title Sistema E-commerce - Diagrama de Contenedores

    Person(cliente, "Cliente", "Compra productos")

    System_Boundary(ecommerce, "Sistema E-commerce") {
        Container(webapp, "Aplicacion Web", "React", "UI para navegacion y compra")
        Container(api, "API Backend", "Node.js/Express", "API REST para operaciones")
        ContainerDb(db, "Base de Datos", "PostgreSQL", "Almacena productos, usuarios, pedidos")
        Container(cache, "Cache", "Redis", "Cache de sesiones y productos")
    }

    System_Ext(pagos, "Gateway de Pagos", "Stripe")

    Rel(cliente, webapp, "Usa", "HTTPS")
    Rel(webapp, api, "Llama", "HTTPS/JSON")
    Rel(api, db, "Lee/Escribe", "SQL")
    Rel(api, cache, "Lee/Escribe", "Redis Protocol")
    Rel(api, pagos, "Procesa pagos", "HTTPS/API")
```

### Elementos de Container

| Elemento | Sintaxis | Uso |
|----------|----------|-----|
| `Container` | `Container(id, "nombre", "tecnologia", "desc")` | Aplicacion/servicio |
| `ContainerDb` | `ContainerDb(id, "nombre", "tech", "desc")` | Base de datos |
| `ContainerQueue` | `ContainerQueue(id, "nombre", "tech", "desc")` | Cola de mensajes |
| `Container_Ext` | `Container_Ext(id, "nombre", "tech", "desc")` | Contenedor externo |
| `Container_Boundary` | `Container_Boundary(id, "nombre") { }` | Agrupacion |

### Ejemplo con Microservicios

```mermaid
C4Container
    title Plataforma de Streaming - Contenedores

    Person(usuario, "Usuario", "Ve contenido multimedia")

    System_Boundary(streaming, "Plataforma de Streaming") {
        Container(web, "Web App", "React", "Interfaz de usuario")
        Container(mobile, "Mobile App", "React Native", "App movil")
        Container(gateway, "API Gateway", "Kong", "Punto de entrada API")

        Container(auth, "Auth Service", "Go", "Autenticacion y autorizacion")
        Container(catalog, "Catalog Service", "Python/FastAPI", "Gestion de contenido")
        Container(streaming_svc, "Streaming Service", "Rust", "Entrega de video")
        Container(recommendations, "Recommendations", "Python/ML", "Motor de recomendaciones")

        ContainerDb(users_db, "Users DB", "PostgreSQL", "Datos de usuarios")
        ContainerDb(content_db, "Content DB", "MongoDB", "Metadatos de contenido")
        ContainerDb(analytics_db, "Analytics", "ClickHouse", "Datos de uso")
        ContainerQueue(events, "Event Bus", "Kafka", "Eventos del sistema")
    }

    System_Ext(cdn, "CDN", "Cloudflare")
    System_Ext(storage, "Object Storage", "S3")

    Rel(usuario, web, "Usa", "HTTPS")
    Rel(usuario, mobile, "Usa", "HTTPS")
    Rel(web, gateway, "API calls", "HTTPS")
    Rel(mobile, gateway, "API calls", "HTTPS")
    Rel(gateway, auth, "Autentica", "gRPC")
    Rel(gateway, catalog, "Consulta", "gRPC")
    Rel(gateway, streaming_svc, "Stream", "HLS")
    Rel(streaming_svc, cdn, "Sirve", "HTTPS")
    Rel(streaming_svc, storage, "Lee", "S3 API")
    Rel(catalog, content_db, "Lee/Escribe")
    Rel(auth, users_db, "Lee/Escribe")
    Rel(recommendations, analytics_db, "Lee")
    Rel(catalog, events, "Publica")
    Rel(recommendations, events, "Consume")
```

## C4Component (Nivel 3 - Componentes)

Muestra los componentes dentro de un contenedor.

### Sintaxis Basica

```mermaid
C4Component
    title API Backend - Componentes

    Container_Boundary(api, "API Backend") {
        Component(auth, "Auth Controller", "Express Router", "Maneja autenticacion")
        Component(products, "Products Controller", "Express Router", "CRUD de productos")
        Component(orders, "Orders Controller", "Express Router", "Gestion de pedidos")

        Component(auth_svc, "Auth Service", "Service Class", "Logica de autenticacion")
        Component(product_svc, "Product Service", "Service Class", "Logica de productos")
        Component(order_svc, "Order Service", "Service Class", "Logica de pedidos")

        Component(user_repo, "User Repository", "TypeORM", "Acceso a datos de usuarios")
        Component(product_repo, "Product Repository", "TypeORM", "Acceso a datos de productos")
        Component(order_repo, "Order Repository", "TypeORM", "Acceso a datos de pedidos")
    }

    ContainerDb(db, "PostgreSQL", "Base de datos relacional")
    Container_Ext(cache, "Redis", "Cache")

    Rel(auth, auth_svc, "Usa")
    Rel(products, product_svc, "Usa")
    Rel(orders, order_svc, "Usa")

    Rel(auth_svc, user_repo, "Usa")
    Rel(product_svc, product_repo, "Usa")
    Rel(order_svc, order_repo, "Usa")

    Rel(user_repo, db, "Lee/Escribe", "SQL")
    Rel(product_repo, db, "Lee/Escribe", "SQL")
    Rel(order_repo, db, "Lee/Escribe", "SQL")
    Rel(product_svc, cache, "Lee/Escribe", "Redis")
```

### Elementos de Component

| Elemento | Sintaxis | Uso |
|----------|----------|-----|
| `Component` | `Component(id, "nombre", "tech", "desc")` | Componente |
| `ComponentDb` | `ComponentDb(id, "nombre", "tech", "desc")` | Componente de BD |
| `ComponentQueue` | `ComponentQueue(id, "nombre", "tech", "desc")` | Componente de cola |
| `Component_Ext` | `Component_Ext(id, "nombre", "tech", "desc")` | Componente externo |

## Relaciones

### Sintaxis de Relaciones

```
Rel(origen, destino, "etiqueta", "tecnologia")
Rel_U(origen, destino, "etiqueta")  // Hacia arriba
Rel_D(origen, destino, "etiqueta")  // Hacia abajo
Rel_L(origen, destino, "etiqueta")  // Hacia izquierda
Rel_R(origen, destino, "etiqueta")  // Hacia derecha
Rel_Back(origen, destino, "etiqueta")  // Relacion inversa
BiRel(a, b, "etiqueta")  // Bidireccional
```

### Ejemplo de Relaciones Direccionales

```mermaid
C4Context
    title Relaciones Direccionales

    Person(user, "Usuario")
    System(frontend, "Frontend")
    System(backend, "Backend")
    SystemDb(db, "Database")

    Rel_D(user, frontend, "Usa")
    Rel_D(frontend, backend, "API calls")
    Rel_D(backend, db, "Queries")
    Rel_Back(db, backend, "Results")
```

## Limites y Agrupaciones

### Enterprise Boundary

```mermaid
C4Context
    title Limites Empresariales

    Enterprise_Boundary(empresa, "Mi Empresa") {
        Person(empleado, "Empleado")
        System(interno, "Sistema Interno")
    }

    System_Ext(externo, "Sistema Externo")

    Rel(empleado, interno, "Usa")
    Rel(interno, externo, "Integra")
```

### System Boundary

```mermaid
C4Container
    title Limites de Sistema

    System_Boundary(sistema, "Mi Sistema") {
        Container(app, "Aplicacion", "Tech")
        ContainerDb(db, "Database", "PostgreSQL")
    }
```

### Container Boundary

```mermaid
C4Component
    title Limites de Contenedor

    Container_Boundary(api, "API Service") {
        Component(ctrl, "Controller", "Tech")
        Component(svc, "Service", "Tech")
        Component(repo, "Repository", "Tech")
    }
```

## Configuracion y Estilos

### Usando Directivas

```mermaid
%%{init: {'theme': 'dark'}}%%
C4Context
    title Diagrama con Tema Dark
    Person(user, "Usuario")
    System(sys, "Sistema")
    Rel(user, sys, "Usa")
```

### Actualizacion de Estilos

```mermaid
C4Context
    title Diagrama con Estilos Personalizados

    Person(user, "Usuario", "Descripcion")
    System(sys, "Sistema", "Descripcion")

    Rel(user, sys, "Usa")

    UpdateElementStyle(user, $fontColor="red", $bgColor="grey")
    UpdateRelStyle(user, sys, $textColor="blue", $lineColor="blue")
```

### Opciones de UpdateElementStyle

| Opcion | Descripcion |
|--------|-------------|
| `$fontColor` | Color del texto |
| `$bgColor` | Color de fondo |
| `$borderColor` | Color del borde |
| `$shadowing` | Sombra (true/false) |
| `$shape` | Forma del elemento |
| `$sprite` | Icono/sprite |
| `$techn` | Tecnologia |
| `$descr` | Descripcion |
| `$link` | URL de enlace |

### Opciones de UpdateRelStyle

| Opcion | Descripcion |
|--------|-------------|
| `$textColor` | Color del texto |
| `$lineColor` | Color de la linea |
| `$lineStyle` | Estilo de linea (dashed, dotted) |
| `$offsetX` | Desplazamiento X |
| `$offsetY` | Desplazamiento Y |

## Layout

### Direccion del Layout

```mermaid
C4Context
    title Layout Left to Right

    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")

    Person(a, "A")
    Person(b, "B")
    Person(c, "C")
    System(sys, "Sistema")

    Rel(a, sys, "")
    Rel(b, sys, "")
    Rel(c, sys, "")
```

## Ejemplos Completos

### Sistema de Microservicios Completo

```mermaid
C4Context
    title Sistema de Pedidos - Contexto

    Person(cliente, "Cliente", "Realiza pedidos online")
    Person(operador, "Operador", "Gestiona pedidos")

    Enterprise_Boundary(empresa, "E-Commerce Corp") {
        System(pedidos, "Sistema de Pedidos", "Gestiona todo el ciclo de pedidos")
    }

    System_Ext(pagos, "Stripe", "Procesamiento de pagos")
    System_Ext(envios, "FedEx API", "Logistica de envios")
    System_Ext(notif, "SendGrid", "Notificaciones email")

    Rel(cliente, pedidos, "Realiza pedidos", "HTTPS")
    Rel(operador, pedidos, "Gestiona", "HTTPS")
    Rel(pedidos, pagos, "Cobra", "API")
    Rel(pedidos, envios, "Envia", "API")
    Rel(pedidos, notif, "Notifica", "API")
```

```mermaid
C4Container
    title Sistema de Pedidos - Contenedores

    Person(cliente, "Cliente")

    System_Boundary(pedidos, "Sistema de Pedidos") {
        Container(spa, "SPA", "Vue.js", "Interfaz de usuario")
        Container(bff, "BFF", "Node.js", "Backend for Frontend")
        Container(orders, "Orders Service", "Go", "Gestion de pedidos")
        Container(inventory, "Inventory Service", "Go", "Control de inventario")
        Container(payments, "Payment Service", "Go", "Procesamiento de pagos")

        ContainerDb(orders_db, "Orders DB", "PostgreSQL", "Pedidos")
        ContainerDb(inventory_db, "Inventory DB", "PostgreSQL", "Inventario")
        ContainerQueue(events, "Message Broker", "RabbitMQ", "Eventos")
    }

    System_Ext(stripe, "Stripe")

    Rel(cliente, spa, "Usa", "HTTPS")
    Rel(spa, bff, "API", "HTTPS/GraphQL")
    Rel(bff, orders, "CRUD", "gRPC")
    Rel(bff, inventory, "Query", "gRPC")
    Rel(orders, orders_db, "R/W", "SQL")
    Rel(inventory, inventory_db, "R/W", "SQL")
    Rel(orders, events, "Publish", "AMQP")
    Rel(payments, events, "Subscribe", "AMQP")
    Rel(payments, stripe, "Charge", "HTTPS")
```

## Tips y Mejores Practicas

1. **Empezar por Context**: Siempre comenzar con el nivel mas alto
2. **Descripciones claras**: Cada elemento debe tener proposito claro
3. **Tecnologias especificas**: Indicar tecnologias en Containers y Components
4. **Limites logicos**: Usar boundaries para agrupar elementos relacionados
5. **Relaciones con etiquetas**: Describir que hace cada relacion
6. **No mezclar niveles**: Cada diagrama debe ser de un solo nivel
7. **Mantener actualizado**: Los diagramas deben reflejar el estado actual
