from flask import Flask
from flask_healthz import HealthError, healthz

app = Flask(__name__)

app.register_blueprint(healthz, url_prefix='/healthz')

def liveness():
    return 'OK', 200

def readiness():
    return 'OK', 200

app.add_url_rule('/healthz/liveness', 'liveness', view_func=lambda: liveness())
app.add_url_rule('/healthz/readiness', 'readiness', view_func=lambda: readiness())

@app.route('/')
def hello_world():
    return 'Hello DevOps Team!'

if __name__ == '__main__':
    app.run()
