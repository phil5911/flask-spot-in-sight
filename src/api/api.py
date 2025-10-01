from flask import Blueprint, jsonify, request
from src.model.Task import Task

api_bp = Blueprint("api", __name__)

# Liste de tâches en mémoire
task_list = []

# Récupérer toutes les tâches
@api_bp.route('/task', methods=['GET'])
def get_task():
    return jsonify([task.to_dict() for task in task_list])

# Créer une nouvelle tâche
@api_bp.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        id=data.get("id"),
        title=data.get("title"),
        description=data.get("description")
    )
    task_list.append(new_task)
    return jsonify(new_task.to_dict()), 201

@api_bp.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # 1. Rechercher la task dans le tableau
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            return jsonify({'message': 'task delete'}), 200
        return jsonify({'message':'task no found'}), 404

@api_bp.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "No JSON data provided"}), 400

    for task in task_list:
        if task.id == task_id:
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            # Si completed est envoyé, on l'utilise ; sinon on garde l'ancien
            if 'completed' in data:
                task.completed = data['completed']

            return jsonify(task.to_dict()), 200

    # Si aucune tâche trouvée
    return jsonify({'message': 'task not found'}), 404





