from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    secret = os.environ.get('APP_SECRET', 'Секрет не найден')
    return f"<h1>Web-Application Running!</h1>Секретное значение из Secret Manager: <b>{secret}</b>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)