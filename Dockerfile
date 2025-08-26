# Imagen base
From python:3.9-slim

# Crear directorio de trabajo 
WORKDIR /app

# Copiar archivo principal
COPY app.py .

# Ejecutar aplicaciones
CMD ["python",  "app.py"]
