from flask import Flask, jsonify
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
CORS(app)

# Set up logging
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/myapp.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('MyApp startup')

@app.route('/api/hello')
def hello():
    app.logger.info('Hello endpoint was accessed')
    return jsonify(message="Hello from Flask!")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
