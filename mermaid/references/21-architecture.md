# Architecture Diagram (Diagrama de Arquitectura) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/architecture.html

Los diagramas de arquitectura visualizan la infraestructura de sistemas, incluyendo servicios cloud, redes y componentes de infraestructura con iconos representativos.

## Sintaxis Basica

```mermaid
architecture-beta
    group api[API Layer]

    service db(database)[Database] in api
    service server(server)[Server] in api

    db:L -- R:server
```

## Estructura General

```
architecture-beta
    group nombre[Etiqueta]
    service id(tipo)[Etiqueta] in grupo
    servicio1:posicion -- posicion:servicio2
```

## Grupos

Los grupos agrupan servicios relacionados:

```mermaid
architecture-beta
    group frontend[Frontend]
    group backend[Backend]
    group data[Data Layer]

    service web(internet)[Web App] in frontend
    service api(server)[API] in backend
    service db(database)[Database] in data

    web:R -- L:api
    api:R -- L:db
```

### Grupos Anidados

```mermaid
architecture-beta
    group cloud[Cloud Provider]
        group vpc[VPC]
            service app(server)[App Server]
            service db(database)[Database]
        end
    end
```

## Servicios

### Tipos de Servicios (Iconos)

```mermaid
architecture-beta
    group icons[Tipos de Iconos]

    service s1(server)[Server] in icons
    service s2(database)[Database] in icons
    service s3(disk)[Disk] in icons
    service s4(internet)[Internet] in icons
    service s5(cloud)[Cloud] in icons
```

### Tabla de Tipos

| Tipo | Icono | Uso |
|------|-------|-----|
| `server` | Servidor | Servidores, aplicaciones |
| `database` | Base de datos | Bases de datos |
| `disk` | Disco | Almacenamiento |
| `internet` | Globo | Internet, redes externas |
| `cloud` | Nube | Servicios cloud |

### Servicios Fuera de Grupos

```mermaid
architecture-beta
    service users(internet)[Users]
    
    group app[Application]
        service web(server)[Web]
    end

    users:R -- L:web
```

## Conexiones

### Direcciones

Las conexiones usan posiciones: `T` (top), `B` (bottom), `L` (left), `R` (right)

```mermaid
architecture-beta
    group demo[Conexiones]
    
    service a(server)[A] in demo
    service b(server)[B] in demo
    service c(server)[C] in demo
    service d(server)[D] in demo

    a:R -- L:b
    a:B -- T:c
    b:B -- T:d
```

### Sintaxis de Conexion

```
servicio1:posicion -- posicion:servicio2
```

## Ejemplos de Arquitecturas

### Aplicacion Web Basica

```mermaid
architecture-beta
    service users(internet)[Users]

    group app[Application]
        service lb(cloud)[Load Balancer]
        service web1(server)[Web Server 1]
        service web2(server)[Web Server 2]
        service db(database)[PostgreSQL]
    end

    users:R -- L:lb
    lb:R -- L:web1
    lb:R -- L:web2
    web1:B -- T:db
    web2:B -- T:db
```

### Microservicios

```mermaid
architecture-beta
    service client(internet)[Clients]

    group gateway[API Gateway]
        service gw(cloud)[Gateway]
    end

    group services[Microservices]
        service auth(server)[Auth Service]
        service users(server)[User Service]
        service orders(server)[Order Service]
        service products(server)[Product Service]
    end

    group data[Data Layer]
        service authdb(database)[Auth DB]
        service userdb(database)[User DB]
        service orderdb(database)[Order DB]
        service productdb(database)[Product DB]
    end

    client:R -- L:gw
    gw:R -- L:auth
    gw:R -- L:users
    gw:R -- L:orders
    gw:R -- L:products
    auth:B -- T:authdb
    users:B -- T:userdb
    orders:B -- T:orderdb
    products:B -- T:productdb
```

### Cloud Architecture

```mermaid
architecture-beta
    service internet(internet)[Internet]

    group aws[AWS Cloud]
        group public[Public Subnet]
            service alb(cloud)[ALB]
            service nat(cloud)[NAT Gateway]
        end

        group private[Private Subnet]
            service app1(server)[App Server 1]
            service app2(server)[App Server 2]
        end

        group data[Data Subnet]
            service rds(database)[RDS Primary]
            service rdsrep(database)[RDS Replica]
            service redis(database)[ElastiCache]
        end
    end

    internet:R -- L:alb
    alb:R -- L:app1
    alb:R -- L:app2
    app1:B -- T:rds
    app2:B -- T:rds
    app1:B -- T:redis
    rds:R -- L:rdsrep
```

### Container Architecture

```mermaid
architecture-beta
    service registry(cloud)[Container Registry]

    group k8s[Kubernetes Cluster]
        group ingress[Ingress]
            service nginx(cloud)[Nginx Ingress]
        end

        group workloads[Workloads]
            service pod1(server)[Pod 1]
            service pod2(server)[Pod 2]
            service pod3(server)[Pod 3]
        end

        group storage[Persistent Storage]
            service pv(disk)[PV]
        end
    end

    group external[External]
        service db(database)[External DB]
    end

    registry:R -- L:pod1
    registry:R -- L:pod2
    registry:R -- L:pod3
    nginx:R -- L:pod1
    nginx:R -- L:pod2
    nginx:R -- L:pod3
    pod1:B -- T:pv
    pod1:R -- L:db
```

### Event-Driven Architecture

```mermaid
architecture-beta
    group producers[Producers]
        service web(server)[Web App]
        service mobile(server)[Mobile App]
        service iot(server)[IoT Devices]
    end

    group messaging[Message Broker]
        service kafka(cloud)[Kafka]
    end

    group consumers[Consumers]
        service analytics(server)[Analytics]
        service notifications(server)[Notifications]
        service storage(server)[Storage Service]
    end

    group data[Data Stores]
        service warehouse(database)[Data Warehouse]
        service cache(database)[Redis Cache]
    end

    web:R -- L:kafka
    mobile:R -- L:kafka
    iot:R -- L:kafka
    kafka:R -- L:analytics
    kafka:R -- L:notifications
    kafka:R -- L:storage
    analytics:B -- T:warehouse
    storage:B -- T:cache
```

### CI/CD Pipeline

```mermaid
architecture-beta
    service dev(server)[Developer]

    group cicd[CI/CD]
        service git(cloud)[GitHub]
        service ci(server)[Jenkins]
        service registry(cloud)[Docker Registry]
    end

    group environments[Environments]
        service dev_env(server)[Development]
        service stage(server)[Staging]
        service prod(server)[Production]
    end

    dev:R -- L:git
    git:R -- L:ci
    ci:R -- L:registry
    registry:R -- L:dev_env
    registry:R -- L:stage
    registry:R -- L:prod
```

### Data Pipeline

```mermaid
architecture-beta
    group sources[Data Sources]
        service api(server)[APIs]
        service db_source(database)[Databases]
        service files(disk)[File Storage]
    end

    group ingestion[Ingestion]
        service kafka(cloud)[Kafka]
        service spark(server)[Spark Streaming]
    end

    group processing[Processing]
        service batch(server)[Batch Processing]
        service ml(server)[ML Pipeline]
    end

    group storage[Storage]
        service lake(disk)[Data Lake]
        service warehouse(database)[Data Warehouse]
    end

    group consumption[Consumption]
        service bi(server)[BI Tools]
        service api_out(server)[Data API]
    end

    api:R -- L:kafka
    db_source:R -- L:kafka
    files:R -- L:kafka
    kafka:R -- L:spark
    spark:R -- L:lake
    lake:R -- L:batch
    batch:R -- L:warehouse
    lake:R -- L:ml
    warehouse:R -- L:bi
    warehouse:R -- L:api_out
```

## Configuracion

### Tema

```mermaid
%%{init: {'theme': 'forest'}}%%
architecture-beta
    group demo[Demo]
    service s1(server)[Server] in demo
    service s2(database)[Database] in demo
    s1:R -- L:s2
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
architecture-beta
    group demo[Demo]
    service s1(server)[Server] in demo
    service s2(database)[Database] in demo
    s1:R -- L:s2
```

## Posiciones de Conexion

| Posicion | Descripcion |
|----------|-------------|
| `T` | Top (arriba) |
| `B` | Bottom (abajo) |
| `L` | Left (izquierda) |
| `R` | Right (derecha) |

## Mejores Practicas

1. **Agrupar logicamente**: Usar grupos para capas o zonas
2. **Direccion consistente**: Flujo general de izquierda a derecha o arriba a abajo
3. **Etiquetas claras**: Nombres descriptivos para servicios
4. **Tipos apropiados**: Usar iconos que representen el servicio
5. **Conexiones minimas**: Evitar demasiadas lineas cruzadas
6. **Niveles de detalle**: Ajustar detalle segun audiencia

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Cloud Architecture | Infraestructura en la nube |
| Network Topology | Topologia de red |
| Microservices | Arquitectura de microservicios |
| Data Flow | Flujo de datos |
| Deployment | Arquitectura de despliegue |
| Security | Zonas de seguridad |

## Limitaciones

- Conjunto limitado de iconos
- Esta en version beta
- Sin soporte para iconos personalizados
- Layout automatico puede no ser optimo para diagramas complejos

## Notas

- `architecture-beta` indica version beta
- Los iconos son genericos, no especificos de proveedores cloud
- Para arquitecturas cloud especificas (AWS, Azure, GCP), considerar herramientas especializadas
