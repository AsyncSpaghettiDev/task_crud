from flask import Flask, request
from app.database import task

app = Flask(__name__)


@app.get('/tasks')
def get_all_tasks():
    out = {}
    response = task.scan()
    out['task'] = response
    return out


@app.post('/tasks')
def create_task():
    out = {"status": "ok"}
    tast_data = request.json
    task.insert(tast_data)
    return out, 201


@app.put('/tasks/<int:task_id>')
def update_task(task_id):
    task_data = request.json
    task.update(task_id, task_data)
    return '', 204


@app.delete('/tasks/<int:task_id>')
def delete_task(task_id):
    task.delete(task_id)
    return '', 204
