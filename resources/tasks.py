from flask import request, jsonify, Blueprint
from datetime import datetime

from database import tasks

tasks_bp = Blueprint('route-tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    created_date = datetime.now().strftime("%x")  # formato fecha 5/22/2021

    data = (title, created_date)
    task_id = tasks.insert_task(data)

    if task_id:
        task = tasks.select_task_by_id(task_id)
        return jsonify({'task': task})

    return jsonify({'message': 'Internal Error'})


@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    data = tasks.select_all_tasks()

    if data:
        return jsonify({'tasks': data})
    elif data == False:
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'tasks': {}})


@tasks_bp.route('/tasks', methods=['PUT'])
def update_tasks():
    title = request.json['title']
    id_arg = request.args.get('id')

    if tasks.update_task(id_arg, (title,)):  # el title va dentro de un tuple
        task = tasks.select_task_by_id(id_arg)
        return jsonify(task)

    return jsonify({'message': 'Internal Error'})


@tasks_bp.route('/tasks', methods=['DELETE'])
def delete_tasks():
    id_arg = request.args.get('id')
    if tasks.delete_task(id_arg):
        return jsonify({'message': 'Task Deleted'})

    return jsonify({'message': 'Internal Error'})
