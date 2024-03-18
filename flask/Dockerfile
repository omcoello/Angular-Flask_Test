

# Usa una imagen de Python oficial como base
FROM python:3.8.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor en /app
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Expone el puerto 5000 (puerto predeterminado para Flask) para que sea accesible desde el exterior
EXPOSE 5000

CMD ["flask", "run"]