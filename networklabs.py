from netmiko import ConnectHandler
import os
from datetime import datetime
from pathlib import Path

# === 1. Forzar algoritmos SSH antiguos ===
ssh_config = """
Host *
    KexAlgorithms +diffie-hellman-group14-sha1
    HostKeyAlgorithms +ssh-rsa
    PubkeyAcceptedAlgorithms +ssh-rsa
"""

ssh_dir = Path.home() / ".ssh"
ssh_dir.mkdir(exist_ok=True)
config_path = ssh_dir / "config"

with open(config_path, "w") as f:
    f.write(ssh_config)

os.chmod(config_path, 0o600)

# === 2. Crear carpeta de reportes ===
os.makedirs("reportes", exist_ok=True)

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

# === 4. Comandos para cada router ===
comandos = {
    "show version": "version.txt",
    "show inventory": "inventario.txt",
    "show ip interface brief": "ip_interface.txt",
    "show cdp neighbors detail": "vecinos.txt",
    "show vlan brief": "vlan.txt"
}

for router in routers:
    alias = router["alias"]
    host = router["host"]
    print(f"\n🔌 Conectando a {alias} ({host})...")

    try:
        connection = ConnectHandler(**{**common, "ip": host})
        hostname = connection.send_command("show run | include hostname").split()[-1]
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        carpeta_router = f"reportes/{alias}_{fecha}"
        os.makedirs(carpeta_router, exist_ok=True)

        for cmd, archivo in comandos.items():
            print(f"  Ejecutando: {cmd}")
            salida = connection.send_command(cmd)
            with open(f"{carpeta_router}/{archivo}", "w") as f:
                f.write(f"Comando: {cmd}\nDispositivo: {hostname}\nFecha: {datetime.now()}\n\n")
                f.write(salida)

        connection.disconnect()
        print(f"✅ Reportes guardados en: {carpeta_router}")

    except Exception as e:
        print(f"❌ Error en {alias}: {e}")

