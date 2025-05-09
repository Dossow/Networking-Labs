# Proyecto: Automatización de redes Cisco con Python y Docker.

## 📚 Descripción
Este proyecto automatiza la recolección de información de una red Cisco simulada en GNS3, conectándose a dispositivos vía SSH/Telnet usando Python y generando un inventario de red actualizado en CSV/JSON o diagramas visuales.

## 🎯 Objetivo
- Automatizar la documentación de la topología de red.
- Parsear la información de dispositivos vecinos, interfaces IP, VLANs y protocolos de enrutamiento.
- Presentar los resultados de forma clara y exportable.

## 🛠️ Tecnologías Utilizadas
- Python 
- Docker
- Git
- GNS3 Server 

## 🖥️ Requisitos de la topología (GNS3)
- 4 dispositivos Cisco (routers y/o switches).
- Acceso vía SSH/Telnet habilitado.


## ⚙️ ¿Como descargo el proyecto?

1. Clonar el repositorio.
   
   ```bash
   git clone https://github.com/Dossow/Networking-Labs.git
   cd inventario-red-cisco
   ```

2. 🐳 Construye la imagen docker

```bash
docker build -t inventario-red .
```
3. 🐳 Ejecuta el contenedor

```bash
docker run --rm -v $(pwd)/scripts:/app Networking-Labs python connect_devices.py
```
- Los outputs del parseo son guardados en el directorio ```/reports ```

  ## 🔐 Variables de entorno

```bash
R1 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.1",
    "username": "cisco",
    "password": "cisco123",
    "secret": "cisco123",
}
```

## ✨ Funcionalidades

Conexión automática a múltiples dispositivos y recolección de datos de:

- Vecinos CDP/LLDP.
- Uptime.
- Estado de interfaces IP.
- Configuración de VLANs y routing dinámico.
- Reporte en formatos CSV, JSON o diagramas de red.
