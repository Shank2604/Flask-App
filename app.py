from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='/var/log/app.log',
    level=logging.INFO
)

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return "Welcome to DevOps CI/CD Project!"

@app.route('/health')
def health():
    return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
