from flask import Flask, request

from app.database import task

app = Flask(__name__)


@app.get('/tasks')
def get_all_tasks():
    out = {}
    response = task.scan()
    out['tasks'] = response
    return out


@app.get('/tasks/<int:task_id>')
def get_single_task(task_id):
    out = {}
    status = 404
    response = task.scan_single(task_id)
    if response:
        out['task'] = response[0]
        status = 200
    else:
        out['status'] = 'error'
    return out, status


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
