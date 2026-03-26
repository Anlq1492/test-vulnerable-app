FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app_flask.py .
COPY app.py .

# Создание тестовой базы данных
RUN python -c "import sqlite3; conn = sqlite3.connect('/tmp/users.db'); conn.execute('CREATE TABLE users (name text)'); conn.execute(\"INSERT INTO users VALUES ('admin')\"); conn.commit()"

EXPOSE 5000

# Убедитесь, что приложение запускается на 0.0.0.0
CMD ["python", "-c", "from app_flask import app; app.run(host='0.0.0.0', port=5000, debug=True)"]
