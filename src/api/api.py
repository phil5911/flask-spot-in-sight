from flask import Blueprint, jsonify, request
from src.config.database import db
from src.model.Task import Task

api_bp = Blueprint("api", __name__)

# Liste de tâches en mémoire
# task_list = []

# Récupérer toutes les tâches
@api_bp.route('/task', methods=['GET'])
def get_task():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@api_bp.route("/task/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id : int):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tâche non trouvée.'}),404
    return jsonify(task.to_dict()),200


# Créer une nouvelle tâche
@api_bp.route("/task", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'objet vide.'}),400
    new_task: Task = Task(
        title=data.get("title"),
        description=data.get("description"),
        completed=data.get("completed", False)
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@api_bp.route("/task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    # 1. rechercher la task dans la bdd
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tâche non trouvée.'}),404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "task deleted"}), 200

@api_bp.route("/task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    # 1. recuperer la data
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tâche non trouvée.'}), 404
    data = request.get_json()
    task.title = data.get("title")
    task.description = data.get("description")
    task.completed = data.get("completed")
    db.session.commit()
    return jsonify(task.to_dict()), 200






