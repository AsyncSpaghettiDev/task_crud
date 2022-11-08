from flask import Flask
from app.database import task

app = Flask(__name__)


@app.get('/')
def get_all_tasks():
    out = {}
    response = task.scan()
    out['task'] = response
    return out
