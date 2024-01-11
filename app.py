from flask import Flask
from flask_healthz import HealthError, healthz
import os
from dotenv import load_dotenv

load_dotenv()

required_env_vars = [
    'MY_SECRET',
    'NAME',
    'TEAM'
]

missing_vars = [var for var in required_env_vars if var not in os.getenv(var, '')]

if missing_vars:
    raise HealthError(f'Missing required environment variables: {', '.join(missing_vars)}')

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
    NAME = os.getenv('NAME')
    TEAM = os.getenv('TEAM')
    MY_SECRET = os.getenv('MY_SECRET')

    return f"""<xmp>
              Welcome to {NAME}
              I will discuss with {TEAM} using my secret: {MY_SECRET}.
              </xmp>"""

if __name__ == '__main__':
    app.run()
