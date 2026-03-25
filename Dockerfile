FROM python:3.9-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование приложения
COPY app_flask.py .
COPY app.py .

# Создание тестовой базы данных
RUN python -c "import sqlite3; conn = sqlite3.connect('/tmp/users.db'); conn.execute('CREATE TABLE users (name text)'); conn.execute(\"INSERT INTO users VALUES ('admin')\"); conn.commit()"

EXPOSE 5000

CMD ["python", "app_flask.py"]
