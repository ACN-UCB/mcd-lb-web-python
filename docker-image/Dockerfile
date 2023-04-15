# Para construir la imagen ejecutar:
# docker build -t my_web_app:1.0.0 .
FROM python:3.9-slim-buster

RUN apt update
RUN apt install -y nano
RUN apt install -y curl

# Copiar el archivo requirements.txt
COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo app.py
COPY app.py /

EXPOSE 5000

# Ejecutamos
ENTRYPOINT ["python", "app.py"] 