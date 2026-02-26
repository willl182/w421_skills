# Packet Diagram (Diagrama de Paquetes) - Mermaid

> Documentacion oficial: https://mermaid.js.org/syntax/packet.html

Los diagramas de paquetes visualizan la estructura de protocolos de red, formatos de datos y layouts de memoria a nivel de bits y bytes.

## Sintaxis Basica

```mermaid
packet-beta
    0-7: "Campo 1"
    8-15: "Campo 2"
    16-31: "Campo 3"
```

## Estructura General

```
packet-beta
    inicio-fin: "Etiqueta"
```

Donde `inicio` y `fin` son posiciones de bits (0-indexed).

## Campos de Bits

### Campo Simple

```mermaid
packet-beta
    0-7: "Byte 1"
    8-15: "Byte 2"
```

### Campo de Multiples Bits

```mermaid
packet-beta
    0-3: "Nibble 1"
    4-7: "Nibble 2"
    8-31: "Datos (24 bits)"
```

### Bits Individuales

```mermaid
packet-beta
    0: "Bit 0"
    1: "Bit 1"
    2: "Bit 2"
    3: "Bit 3"
    4-7: "Nibble"
```

## Ejemplos de Protocolos

### Header IPv4

```mermaid
packet-beta
    0-3: "Version"
    4-7: "IHL"
    8-13: "DSCP"
    14-15: "ECN"
    16-31: "Total Length"
    32-47: "Identification"
    48-50: "Flags"
    51-63: "Fragment Offset"
    64-71: "TTL"
    72-79: "Protocol"
    80-95: "Header Checksum"
    96-127: "Source IP Address"
    128-159: "Destination IP Address"
```

### Header TCP

```mermaid
packet-beta
    0-15: "Source Port"
    16-31: "Destination Port"
    32-63: "Sequence Number"
    64-95: "Acknowledgment Number"
    96-99: "Data Offset"
    100-102: "Reserved"
    103: "NS"
    104: "CWR"
    105: "ECE"
    106: "URG"
    107: "ACK"
    108: "PSH"
    109: "RST"
    110: "SYN"
    111: "FIN"
    112-127: "Window Size"
    128-143: "Checksum"
    144-159: "Urgent Pointer"
```

### Header UDP

```mermaid
packet-beta
    0-15: "Source Port"
    16-31: "Destination Port"
    32-47: "Length"
    48-63: "Checksum"
```

### Header Ethernet

```mermaid
packet-beta
    0-47: "Destination MAC Address"
    48-95: "Source MAC Address"
    96-111: "EtherType"
```

### Header ICMP

```mermaid
packet-beta
    0-7: "Type"
    8-15: "Code"
    16-31: "Checksum"
    32-63: "Rest of Header"
```

### DNS Header

```mermaid
packet-beta
    0-15: "Transaction ID"
    16: "QR"
    17-20: "Opcode"
    21: "AA"
    22: "TC"
    23: "RD"
    24: "RA"
    25-27: "Z"
    28-31: "RCODE"
    32-47: "QDCOUNT"
    48-63: "ANCOUNT"
    64-79: "NSCOUNT"
    80-95: "ARCOUNT"
```

## Formatos de Datos

### Estructura de Archivo

```mermaid
packet-beta
    0-31: "Magic Number"
    32-47: "Version Major"
    48-63: "Version Minor"
    64-127: "Timestamp"
    128-159: "File Size"
    160-191: "Checksum"
```

### Registro de Base de Datos

```mermaid
packet-beta
    0-31: "Record ID"
    32-39: "Flags"
    40-47: "Type"
    48-79: "Timestamp"
    80-111: "Payload Length"
```

### Mensaje de Protocolo

```mermaid
packet-beta
    0-7: "Version"
    8-15: "Message Type"
    16-31: "Payload Length"
    32-63: "Sequence Number"
    64-127: "Session ID"
```

## Layouts de Memoria

### Estructura de Datos

```mermaid
packet-beta
    0-31: "Pointer to Next"
    32-63: "Pointer to Data"
    64-95: "Size"
    96-103: "Flags"
    104-127: "Padding"
```

### Buffer Layout

```mermaid
packet-beta
    0-63: "Header (8 bytes)"
    64-575: "Data (64 bytes)"
    576-607: "Footer (4 bytes)"
```

### Registro de CPU

```mermaid
packet-beta
    0-7: "Flags"
    8-15: "Status"
    16-23: "Reserved"
    24-31: "Control"
    32-63: "Program Counter"
```

## Protocolos Personalizados

### Protocolo de Chat

```mermaid
packet-beta
    0-7: "Version"
    8-15: "Msg Type"
    16-31: "Msg Length"
    32-63: "User ID"
    64-95: "Timestamp"
    96-127: "Checksum"
```

### Comando IoT

```mermaid
packet-beta
    0-7: "Device Type"
    8-15: "Command"
    16-23: "Channel"
    24-31: "Value"
    32-47: "CRC"
```

### Frame de Sensor

```mermaid
packet-beta
    0-15: "Sensor ID"
    16-23: "Type"
    24-31: "Status"
    32-63: "Value (float)"
    64-95: "Timestamp"
```

## Configuracion

### Tema Default

```mermaid
packet-beta
    0-15: "Campo A"
    16-31: "Campo B"
```

### Tema Forest

```mermaid
%%{init: {'theme': 'forest'}}%%
packet-beta
    0-15: "Campo A"
    16-31: "Campo B"
```

### Tema Dark

```mermaid
%%{init: {'theme': 'dark'}}%%
packet-beta
    0-15: "Campo A"
    16-31: "Campo B"
```

## Opciones de Configuracion

```mermaid
%%{init: {
  'packet': {
    'bitsPerRow': 32,
    'bitWidth': 20,
    'rowHeight': 30
  }
}}%%
packet-beta
    0-7: "Byte 1"
    8-15: "Byte 2"
    16-23: "Byte 3"
    24-31: "Byte 4"
```

| Opcion | Descripcion | Default |
|--------|-------------|---------|
| `bitsPerRow` | Bits por fila | 32 |
| `bitWidth` | Ancho de cada bit | 20 |
| `rowHeight` | Alto de cada fila | 30 |

## Consideraciones

### Alineacion

Los campos deben estar alineados correctamente:

```mermaid
packet-beta
    0-7: "Byte 0"
    8-15: "Byte 1"
    16-23: "Byte 2"
    24-31: "Byte 3"
```

### Campos Grandes

Para campos que cruzan filas:

```mermaid
packet-beta
    0-31: "Primera Palabra"
    32-63: "Segunda Palabra"
    64-127: "Datos (64 bits)"
```

### Bits de Flags

Para bits individuales:

```mermaid
packet-beta
    0: "SYN"
    1: "ACK"
    2: "FIN"
    3: "RST"
    4-7: "Reserved"
    8-15: "Window"
```

## Casos de Uso

| Uso | Descripcion |
|-----|-------------|
| Redes | Headers de protocolos (IP, TCP, UDP, etc.) |
| Formatos de archivo | Estructuras de archivos binarios |
| Memoria | Layouts de estructuras de datos |
| Hardware | Registros de CPU, perifericos |
| Protocolos custom | Diseño de protocolos propios |
| Documentacion | Especificaciones tecnicas |

## Tips y Mejores Practicas

1. **Alinear a bytes**: Cuando sea posible, alinear campos a limites de byte
2. **Etiquetas descriptivas**: Usar nombres claros para cada campo
3. **Bits por fila**: Configurar segun el protocolo (32 bits para IPv4, etc.)
4. **Campos reservados**: Documentar campos reservados/unused
5. **Bits de flags**: Documentar significado de cada bit
6. **Orden de bytes**: Indicar endianness si es relevante

## Errores Comunes

| Error | Causa | Solucion |
|-------|-------|----------|
| Superposicion | Rangos de bits superpuestos | Verificar rangos no se solapen |
| Gaps | Bits sin asignar | Llenar con campos reservados |
| Alineacion | Campos mal alineados | Verificar limites de bytes |
| Etiquetas largas | Texto demasiado largo | Usar abreviaciones |
