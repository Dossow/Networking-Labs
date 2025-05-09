import csv
import os
import time
import textfsm
from getpass import getpass
from netmiko import ConnectHandler

# Crear carpeta 'reportes' si no existe
output_dir = "reportes"
os.makedirs(output_dir, exist_ok=True)

# Ruta completa para el archivo CSV
output_file = os.path.join(output_dir, 'reports.csv')

# Definición de dispositivos
R1 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.1",
    "username": "cisco",
    "password": "cisco123",
    "secret": "cisco123",
}
R2 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.2",
    "username": "cisco",
    "password": "cisco123",
    "secret": "cisco123",
}
R3 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.3",
    "username": "cisco",
    "password": "cisco123",
    "secret": "cisco123",
}
R4 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.4",
    "username": "cisco",
    "password": "cisco123",
    "secret": "cisco123",
}

devices = [R1, R2, R3, R4]  # Corregido: R2 se repetía y R3 no estaba

# Definición de encabezados del CSV
headers = [
    "Nombre dispositivo local",
    "Plataforma de hardware",
    "Número de serie",
    "Versión del sistema operativo",
    "Uptime del dispositivo",
    "Interfaz e IP dispositivo local",
    "Nombre dispositivo vecino",
    "Plataforma dispositivo vecino",
    "IP del dispositivo vecino",
    "Interfaz local",
    "Interfaz remota",
    "VLAN database"
]

# Apertura del archivo CSV en carpeta 'reportes'
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for device in devices:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        datos_show_version = net_connect.send_command("show version", use_textfsm=True)
        datos_show_ip_interface_brief = net_connect.send_command("show ip interface brief", use_textfsm=True)
        datos_show_cdp_neighbor_detail = net_connect.send_command("show cdp neighbor detail", use_textfsm=True)
        datos_show_vlan = net_connect.send_command("show vlan", use_textfsm=True)

        hostname = net_connect.find_prompt().strip('#')

        hardware = datos_show_version[0].get("hardware", [""])[0] if datos_show_version else ""
        serial = datos_show_version[0].get("serial", [""])[0] if datos_show_version else ""
        version = datos_show_version[0].get("version", "") if datos_show_version else ""
        uptime = datos_show_version[0].get("uptime", "") if datos_show_version else ""

        interfaces_ips = [f"{intf['intf']} - {intf['ipaddr']}" for intf in datos_show_ip_interface_brief if intf.get("ipaddr")]

        for neighbor in datos_show_cdp_neighbor_detail:
            neighbor_name = neighbor.get("destination_host", "")
            neighbor_platform = neighbor.get("platform", "")
            neighbor_ip = neighbor.get("management_ip", "")
            local_port = neighbor.get("local_port", "")
            remote_port = neighbor.get("remote_port", "")

            vlan_ids = [vlan.get("vlan_id", "") for vlan in datos_show_vlan]

            writer.writerow([
                hostname,
                hardware,
                serial,
                version,
                uptime,
                "; ".join(interfaces_ips),
                neighbor_name,
                neighbor_platform,
                neighbor_ip,
                local_port,
                remote_port,
                "; ".join(vlan_ids)
            ])

        net_connect.disconnect()
