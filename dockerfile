# Usa una imagen base con Python
FROM python:3.12

# Crea los directorios necesarios dentro del contenedor
RUN mkdir /script /reports

# Copia el script Python a /script
COPY networklabs.py /script/

# Copia el archivo reports.csv si existe (opcional)
# COPY reports/reports.csv /reports/

# Establece el directorio de trabajo
WORKDIR /script

# Instala dependencias si tienes un requirements.txt (opcional)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "/dev/null"]

RUN apt-get update && apt-get install -y \
    nmap \
    vim \
    iputils-ping \
    iproute2 \
    net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

    
# Comando por defecto para ejecutar el script (ajusta el nombre del script)
CMD ["python", "networklabs.py"]