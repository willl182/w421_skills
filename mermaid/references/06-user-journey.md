# User Journey (Viaje del Usuario) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/userJourney.html

Los diagramas de User Journey describen los pasos que un usuario toma para completar una tarea, junto con su nivel de satisfaccion en cada paso.

## Sintaxis Basica

```mermaid
journey
    title Mi viaje como usuario
    section Descubrimiento
        Buscar en Google: 5: Usuario
        Visitar sitio web: 4: Usuario
    section Registro
        Completar formulario: 3: Usuario
        Verificar email: 2: Usuario
    section Uso
        Primera compra: 5: Usuario
```

## Estructura General

```
journey
    title Titulo del viaje
    section Nombre de la seccion
        Nombre de tarea: puntuacion: actores
```

## Componentes

### Titulo

```mermaid
journey
    title Experiencia de Compra Online
    section Navegacion
        Ver productos: 4: Cliente
```

### Secciones

Las secciones agrupan tareas relacionadas:

```mermaid
journey
    title Proceso de Onboarding
    section Registro
        Crear cuenta: 3: Usuario
        Verificar email: 2: Usuario
    section Configuracion
        Completar perfil: 4: Usuario
        Agregar foto: 3: Usuario
    section Uso Inicial
        Tutorial: 5: Usuario
        Primera accion: 4: Usuario
```

### Tareas

Formato: `Nombre de tarea: puntuacion: actores`

```mermaid
journey
    title Ejemplo de Tareas
    section Tareas
        Tarea simple: 5: Actor1
        Tarea con espacios: 3: Actor1, Actor2
        Otra tarea mas: 1: Actor1
```

## Sistema de Puntuacion

La puntuacion va de 1 a 5:

| Puntuacion | Significado | Color |
|------------|-------------|-------|
| 5 | Excelente / Muy satisfecho | Verde |
| 4 | Bueno / Satisfecho | Verde claro |
| 3 | Neutral / Regular | Amarillo |
| 2 | Malo / Insatisfecho | Naranja |
| 1 | Muy malo / Frustrado | Rojo |

```mermaid
journey
    title Escala de Satisfaccion
    section Ejemplos
        Excelente experiencia: 5: Usuario
        Buena experiencia: 4: Usuario
        Experiencia neutral: 3: Usuario
        Mala experiencia: 2: Usuario
        Terrible experiencia: 1: Usuario
```

## Actores

Los actores representan quienes participan en cada paso:

### Actor Unico

```mermaid
journey
    title Con un actor
    section Proceso
        Paso 1: 5: Cliente
        Paso 2: 4: Cliente
```

### Multiples Actores

Los actores se separan por comas:

```mermaid
journey
    title Con multiples actores
    section Interaccion
        Reunion inicial: 4: Cliente, Vendedor
        Presentacion: 3: Vendedor
        Negociacion: 2: Cliente, Vendedor
        Cierre de venta: 5: Cliente, Vendedor, Gerente
```

## Ejemplos Completos

### Experiencia de E-commerce

```mermaid
journey
    title Experiencia de Compra en E-commerce
    section Descubrimiento
        Buscar producto: 5: Cliente
        Ver resultados: 4: Cliente
        Filtrar opciones: 3: Cliente
    section Evaluacion
        Ver detalles del producto: 4: Cliente
        Leer resenas: 5: Cliente
        Comparar precios: 3: Cliente
    section Compra
        Agregar al carrito: 5: Cliente
        Proceso de checkout: 2: Cliente
        Ingresar datos de pago: 1: Cliente
        Confirmar compra: 4: Cliente
    section Post-compra
        Recibir confirmacion: 5: Cliente
        Seguir envio: 4: Cliente
        Recibir producto: 5: Cliente
```

### Dia de Trabajo Tipico

```mermaid
journey
    title Dia de Trabajo de un Desarrollador
    section Manana
        Despertar: 3: Yo
        Preparar cafe: 5: Yo
        Revisar emails: 2: Yo
        Daily standup: 3: Yo, Equipo
    section Trabajo Productivo
        Programar feature: 5: Yo
        Code review: 4: Yo, Colega
        Resolver bug: 2: Yo
    section Tarde
        Almuerzo: 5: Yo
        Reuniones: 1: Yo, Equipo, Cliente
        Mas programacion: 4: Yo
    section Cierre
        Commit y push: 5: Yo
        Documentar: 3: Yo
        Desconectarse: 5: Yo
```

### Onboarding de Usuario

```mermaid
journey
    title Onboarding de Nueva App
    section Descarga
        Buscar en app store: 4: Usuario
        Descargar app: 5: Usuario
        Abrir app: 5: Usuario
    section Registro
        Ver pantalla de bienvenida: 4: Usuario
        Elegir metodo de registro: 3: Usuario
        Completar formulario: 2: Usuario
        Aceptar terminos: 1: Usuario
        Verificar telefono: 2: Usuario
    section Configuracion
        Elegir preferencias: 4: Usuario
        Conectar redes sociales: 3: Usuario
        Subir foto de perfil: 4: Usuario
    section Primer Uso
        Ver tutorial: 4: Usuario
        Explorar funciones: 5: Usuario
        Realizar primera accion: 5: Usuario
```

### Proceso de Soporte Tecnico

```mermaid
journey
    title Experiencia de Soporte Tecnico
    section Problema
        Encontrar problema: 1: Cliente
        Buscar solucion online: 2: Cliente
    section Contacto
        Encontrar pagina de soporte: 3: Cliente
        Esperar en chat: 1: Cliente
        Conectar con agente: 4: Cliente, Agente
    section Resolucion
        Explicar problema: 3: Cliente, Agente
        Diagnostico: 4: Agente
        Aplicar solucion: 4: Agente
        Verificar solucion: 5: Cliente, Agente
    section Cierre
        Encuesta de satisfaccion: 3: Cliente
        Problema resuelto: 5: Cliente
```

## Configuracion

### Usando Frontmatter

```mermaid
---
config:
  theme: forest
---
journey
    title Viaje con Tema Forest
    section Ejemplo
        Tarea 1: 5: Actor
        Tarea 2: 3: Actor
```

### Usando Directivas

```mermaid
%%{init: {'theme': 'dark'}}%%
journey
    title Viaje en Modo Oscuro
    section Ejemplo
        Tarea 1: 5: Actor
        Tarea 2: 3: Actor
```

## Tips y Mejores Practicas

1. **Mantener tareas cortas**: Nombres descriptivos pero concisos
2. **Ser honesto con las puntuaciones**: Reflejar la experiencia real
3. **Agrupar logicamente**: Usar secciones para fases del proceso
4. **Limitar actores**: Demasiados actores pueden confundir
5. **Enfocarse en momentos clave**: No incluir cada micro-paso
6. **Usar para identificar pain points**: Los scores bajos revelan areas de mejora

## Casos de Uso Comunes

| Caso de Uso | Proposito |
|-------------|-----------|
| UX Research | Mapear experiencia actual del usuario |
| Product Design | Identificar areas de mejora |
| Customer Success | Entender puntos de friccion |
| Onboarding | Optimizar flujo de nuevos usuarios |
| Service Design | Disenar servicios centrados en usuario |
