from flask import Flask, request, render_template_string
import os
import sqlite3

app = Flask(__name__)

# Уязвимость: хардкод секрета
SECRET_KEY = "hardcoded_secret_12345"

# Уязвимость: SQL инъекция
@app.route('/user')
def get_user():
    name = request.args.get('name', '')
    conn = sqlite3.connect('/tmp/users.db')
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor = conn.execute(query)
    return str(cursor.fetchall())

# Уязвимость: SSTI
@app.route('/welcome')
def welcome():
    name = request.args.get('name', 'Guest')
    template = f"<h1>Welcome, {name}!</h1>"
    return render_template_string(template)

# Уязвимость: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    result = os.system(f"ping -c 1 {host}")
    return f"Ping result: {result}"

@app.route('/')
def index():
    return """
    <h1>Vulnerable Test Application</h1>
    <ul>
        <li><a href="/user?name=admin">SQL Injection</a></li>
        <li><a href="/welcome?name={{7*7}}">SSTI</a></li>
        <li><a href="/ping?host=127.0.0.1">Command Injection</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
