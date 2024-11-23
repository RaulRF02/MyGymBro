from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.exercise_service import (
    create_exercise,
    get_all_exercises,
    get_exercise_by_id,
    update_exercise,
    delete_exercise
)

exercise_bp = Blueprint("exercise_routes", __name__)

# Helper function to check if the user is trainer or admin
def trainer_or_admin_required(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt_identity()
        if claims["role"] not in ["trainer", "admin"]:
            return jsonify({"error": "Trainer or admin access required"}), 403
        return fn(*args, **kwargs)

    wrapper.__name__ = fn.__name__
    return wrapper


@exercise_bp.route("/exercises", methods=["POST"])
@trainer_or_admin_required
def create_exercise_route():
    data = request.get_json()
    return jsonify(create_exercise(data))


@exercise_bp.route("/exercises", methods=["GET"])
@jwt_required()
def get_all_exercises_route():
    return jsonify(get_all_exercises())


@exercise_bp.route("/exercises/<int:exercise_id>", methods=["GET"])
@jwt_required()
def get_exercise_route(exercise_id):
    return jsonify(get_exercise_by_id(exercise_id))


@exercise_bp.route("/exercises/<int:exercise_id>", methods=["PUT"])
@trainer_or_admin_required
def update_exercise_route(exercise_id):
    data = request.get_json()
    return jsonify(update_exercise(exercise_id, data))


@exercise_bp.route("/exercises/<int:exercise_id>", methods=["DELETE"])
@trainer_or_admin_required
def delete_exercise_route(exercise_id):
    return jsonify(delete_exercise(exercise_id))
