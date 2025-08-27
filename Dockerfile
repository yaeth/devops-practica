# Imagen base de Python 3.9
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos 
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
