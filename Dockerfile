# Imagen base de Python 3.9
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de la app al contenedor
COPY app.py .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
