# Proyecto: Automatización de redes Cisco con Python y Docker.

## 📚 Descripción
Este proyecto automatiza la recolección de información de una red Cisco simulada en GNS3, conectándose a dispositivos vía SSH/Telnet usando Python y generando un inventario de red actualizado en CSV/JSON o diagramas visuales.

## 🎯 Objetivo
- Automatizar la documentación de la topología de red.
- Parsear la información de dispositivos vecinos, interfaces IP, VLANs y protocolos de enrutamiento.
- Presentar los resultados de forma clara y exportable (formato csv u json).

## 🛠️ Tecnologías Utilizadas
- Python (Netmiko, TextFSM)
- Docker
- Git
- GNS3 Server 

## 🖥️ Requisitos de la topología (GNS3)
- 4 dispositivos Cisco (routers y/o switches).
- Acceso vía SSH/Telnet habilitado.

## 📂 Estructura del proyecto
Networking-Labs/ ├── docker/ │ └── Dockerfile ├── scripts/ │ ├── connect_devices.py │ ├── parse_outputs.py │ └── generate_report.py ├── requirements.txt ├── README.md └── .gitignore


## ⚙️ ¿Como descargo el proyecto?

1. Clonar el repositorio.
   
   ```bash
   git clone https://github.com/Dossow/Networking-Labs.git
   cd inventario-red-cisco
   ```

2. 🐳 Construye la imagen docker

```bash
docker build -t Networking-Labs .
```
3. 🐳 Ejecuta el contenedor

```bash
docker run --rm -v $(pwd)/scripts:/app Networking-Labs python connect_devices.py
```
- Los reportes se generaran en el directorio  ```/reports ```

  ## 🔐 Variables de entorno

```bash
SSH_USERNAME=admin
SSH_PASSWORD=cisco123
DEVICE_IPS=192.168.1.1,192.168.1.2,192.168.1.3,192.168.1.4
```

## ✨ Funcionalidades

Conexión automática a múltiples dispositivos y recolección de datos de:

- Vecinos CDP/LLDP.
- Estado de interfaces IP.
- Configuración de VLANs y routing dinámico.
- Reporte en formatos CSV, JSON o diagramas de red.
