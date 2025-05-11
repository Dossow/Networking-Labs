RUN apt update && apt install -y \
    python3 \
    python3-pip \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    nano \
    iputils-ping \
    net-tools \
    openssh-client \
    && pip3 install --upgrade pip setuptools wheel \
    && pip3 install netmiko

# Crear carpeta para reportes
RUN mkdir /reportes

# Copiar el script al contenedor
COPY networklabs.py /root/networlabs.py

# Establecer el directorio de trabajo
WORKDIR /root

# Comando por defecto
CMD ["bash"]
