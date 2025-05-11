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
- GNS3 Server
- SSH (Ver. 1.9)
- Ubuntu (Dev Env).

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
   docker build -t inventario-red-cisco .
   ```
3. 🐳 Ejecuta el contenedor

   ```bash
   docker run --network host inventario-red-cisco .
   ```
- Los outputs del parseo son guardados en el sus directorios correspondientes dentro del contenedor.

4. 🐳 Configuración necesaria dentro del contenedor

   ```bash
   nano /etc/ssh/ssh_config

   Host 10.10.10.1
       KexAlgorithms +diffie-hellman-group14-sha1
       HostKeyAlgorithms +ssh-rsa
       PubkeyAcceptedAlgorithms +ssh-rsa
    
      Host 10.10.10.2
       KexAlgorithms +diffie-hellman-group14-sha1
       HostKeyAlgorithms +ssh-rsa
       PubkeyAcceptedAlgorithms +ssh-rsa
    
      Host 10.10.10.3
       KexAlgorithms +diffie-hellman-group14-sha1
       HostKeyAlgorithms +ssh-rsa
       PubkeyAcceptedAlgorithms +ssh-rsa
    
      Host 10.10.10.4
       KexAlgorithms +diffie-hellman-group14-sha1
       HostKeyAlgorithms +ssh-rsa
       PubkeyAcceptedAlgorithms +ssh-rsa
   ```

  ## 🔐 Variables de entorno

   ```bash
   # === 3. Lista de routers ===
   routers = [
       {"host": "10.10.10.1", "alias": "R1"},
       {"host": "10.10.10.2", "alias": "R2"},
       {"host": "10.10.10.3", "alias": "R3"},
       {"host": "10.10.10.4", "alias": "R4"}
   ]

   # Credenciales comunes
   common = {
       "device_type": "cisco_ios",
       "username": "cisco",
       "password": "cisco",
       "global_delay_factor": 2
   }
   ```

## ✨ Funcionalidades

Conexión automática a múltiples dispositivos y recolección de datos de:

- Vecinos CDP/LLDP.
- Uptime.
- Estado de interfaces IP.
- Configuración de VLANs y routing dinámico.
- Reporte en formatos txt.

![topolista drawio](https://github.com/user-attachments/assets/aafc6135-8d3f-4e59-8ea3-01407ef4f49d)
