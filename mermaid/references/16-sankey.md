# Sankey Diagram - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/sankey.html

Los diagramas Sankey visualizan flujos de una fuente a un destino, donde el ancho de las flechas es proporcional a la cantidad de flujo.

## Sintaxis Basica

El formato es CSV con tres columnas: origen, destino, valor.

```mermaid
sankey-beta

Origen,Destino,Valor
Fuente A,Destino X,100
Fuente A,Destino Y,50
Fuente B,Destino X,75
```

## Estructura General

```
sankey-beta

NodoOrigen,NodoDestino,ValorFlujo
```

**Nota**: `sankey-beta` indica que esta funcionalidad esta en version beta.

## Formato de Datos

### Sin Encabezado

```mermaid
sankey-beta

A,B,50
A,C,30
B,D,40
C,D,25
```

### Con Nombres Descriptivos

```mermaid
sankey-beta

Ventas,Marketing,1000
Ventas,Operaciones,500
Marketing,Publicidad,800
Marketing,Eventos,200
Operaciones,Logistica,300
Operaciones,Soporte,200
```

### Multiples Niveles

```mermaid
sankey-beta

Energia Solar,Electricidad,100
Energia Eolica,Electricidad,80
Gas Natural,Electricidad,200
Gas Natural,Calefaccion,150
Electricidad,Hogares,250
Electricidad,Industria,130
Calefaccion,Hogares,100
Calefaccion,Comercios,50
```

## Ejemplos por Categoria

### Flujo de Energia

```mermaid
sankey-beta

Petroleo,Refineria,500
Gas Natural,Procesamiento,300
Carbon,Planta Electrica,200
Energia Solar,Red Electrica,50
Energia Eolica,Red Electrica,80

Refineria,Transporte,350
Refineria,Industria,150

Procesamiento,Electricidad,150
Procesamiento,Calefaccion,150

Planta Electrica,Red Electrica,180

Red Electrica,Hogares,200
Red Electrica,Comercios,150
Red Electrica,Industria,110

Transporte,Vehiculos,350
Calefaccion,Edificios,150
```

### Presupuesto Empresarial

```mermaid
sankey-beta

Ingresos,Ventas Producto A,5000
Ingresos,Ventas Producto B,3000
Ingresos,Servicios,2000

Ventas Producto A,Costos Directos,2000
Ventas Producto A,Margen Bruto,3000
Ventas Producto B,Costos Directos,1200
Ventas Producto B,Margen Bruto,1800
Servicios,Costos Directos,500
Servicios,Margen Bruto,1500

Margen Bruto,Salarios,2500
Margen Bruto,Marketing,1000
Margen Bruto,Infraestructura,800
Margen Bruto,Utilidad Operativa,2000

Utilidad Operativa,Impuestos,400
Utilidad Operativa,Utilidad Neta,1600
```

### Conversion de Marketing

```mermaid
sankey-beta

Visitantes Web,Registro,1000
Visitantes Web,Rebote,4000

Registro,Activacion,600
Registro,Abandono,400

Activacion,Trial,500
Activacion,Inactivo,100

Trial,Conversion,200
Trial,Cancelacion,300

Conversion,Plan Basico,120
Conversion,Plan Pro,60
Conversion,Plan Enterprise,20
```

### Flujo de Usuarios

```mermaid
sankey-beta

Homepage,Productos,3000
Homepage,Blog,1500
Homepage,Contacto,500
Homepage,Salida,1000

Productos,Detalle Producto,2000
Productos,Salida,1000

Detalle Producto,Carrito,1200
Detalle Producto,Salida,800

Carrito,Checkout,800
Carrito,Abandono,400

Checkout,Compra Exitosa,600
Checkout,Error Pago,200
```

### Cadena de Suministro

```mermaid
sankey-beta

Proveedor A,Almacen Central,500
Proveedor B,Almacen Central,300
Proveedor C,Almacen Central,200

Almacen Central,Centro Distribucion Norte,400
Almacen Central,Centro Distribucion Sur,350
Almacen Central,Centro Distribucion Este,250

Centro Distribucion Norte,Tiendas,350
Centro Distribucion Norte,E-commerce,50

Centro Distribucion Sur,Tiendas,300
Centro Distribucion Sur,E-commerce,50

Centro Distribucion Este,Tiendas,200
Centro Distribucion Este,E-commerce,50
```

### Migracion de Datos

```mermaid
sankey-beta

Sistema Legacy,ETL,10000

ETL,Validados,8500
ETL,Errores,1500

Validados,Nueva BD,7500
Validados,Archivo,1000

Errores,Correccion Manual,1000
Errores,Descartados,500

Correccion Manual,Nueva BD,900
Correccion Manual,Descartados,100
```

### Embudo de Ventas

```mermaid
sankey-beta

Leads,Contactados,5000
Leads,No Contactados,3000

Contactados,Calificados,3500
Contactados,Descalificados,1500

Calificados,Propuesta,2500
Calificados,Sin Interes,1000

Propuesta,Negociacion,1800
Propuesta,Rechazada,700

Negociacion,Cerrado Ganado,1200
Negociacion,Cerrado Perdido,600
```

### Tiempo de Empleados

```mermaid
sankey-beta

Horas Laborales,Desarrollo,160
Horas Laborales,Reuniones,40
Horas Laborales,Documentacion,20
Horas Laborales,Code Review,15
Horas Laborales,Otros,5

Desarrollo,Frontend,80
Desarrollo,Backend,60
Desarrollo,Testing,20

Reuniones,Daily,10
Reuniones,Planning,15
Reuniones,1on1,10
Reuniones,Otras,5
```

## Configuracion

### Configuracion via JavaScript

```javascript
mermaid.initialize({
  sankey: {
    width: 800,
    height: 400,
    linkColor: 'gradient', // source, target, gradient, o color hex
    nodeAlignment: 'justify' // justify, center, left, right
  }
});
```

### Opciones de linkColor

| Valor | Descripcion |
|-------|-------------|
| `source` | Color del nodo origen |
| `target` | Color del nodo destino |
| `gradient` | Degradado entre origen y destino |
| `#hexcolor` | Color especifico |

### Opciones de nodeAlignment

| Valor | Descripcion |
|-------|-------------|
| `justify` | Distribucion uniforme (default) |
| `center` | Centrado |
| `left` | Alineado a la izquierda |
| `right` | Alineado a la derecha |

### Tema

```mermaid
%%{init: {'theme': 'forest'}}%%
sankey-beta

A,B,100
A,C,50
B,D,80
C,D,40
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
sankey-beta

A,B,100
A,C,50
B,D,80
C,D,40
```

## Personalizacion de Colores

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#ff6b6b',
    'secondaryColor': '#4ecdc4',
    'tertiaryColor': '#45b7d1'
  }
}}%%
sankey-beta

Fuente 1,Destino A,100
Fuente 1,Destino B,50
Fuente 2,Destino A,75
Fuente 2,Destino B,25
```

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Flujo de energia | Produccion, transformacion, consumo |
| Finanzas | Ingresos, gastos, presupuestos |
| Marketing | Embudos, conversiones, atribucion |
| Logistica | Cadenas de suministro, distribucion |
| Migraciones | Flujo de datos entre sistemas |
| Procesos | Entradas, transformaciones, salidas |

## Consideraciones

### Limitaciones

- Esta en version **beta**
- Soporte limitado de estilos personalizados
- No soporta interactividad avanzada

### Buenas Practicas

1. **Datos consistentes**: Los valores deben sumar correctamente
2. **Nombres descriptivos**: Usar etiquetas claras para nodos
3. **Jerarquia logica**: Organizar de izquierda (origen) a derecha (destino)
4. **Limitar complejidad**: Demasiados flujos reducen legibilidad
5. **Colores significativos**: Usar colores para categorizar flujos

## Tips de Formateo

1. **Una linea por flujo**: Cada conexion en su propia linea
2. **Sin espacios extra**: Mantener formato CSV limpio
3. **Valores numericos**: Solo numeros positivos para el valor
4. **Nombres sin comas**: Evitar comas en nombres de nodos

## Errores Comunes

| Error | Causa | Solucion |
|-------|-------|----------|
| Diagrama vacio | Formato incorrecto | Verificar CSV (origen,destino,valor) |
| Valores no visibles | Valores muy pequenos | Usar escala apropiada |
| Nodos desconectados | Nombres inconsistentes | Verificar ortografia exacta |
| Flujo inverso | Origen y destino invertidos | Revisar direccion logica |
