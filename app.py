# 1. Jib Python Image sghira
FROM python:3.10-slim

# 2. Kriyye dossier dyal l-khedma
WORKDIR /app

# 3. Copier l-fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# 4. Fth Port 5000 w khddem l-App
EXPOSE 5000
CMD ["python", "app.py"]

