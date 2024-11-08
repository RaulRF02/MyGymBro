from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.exercise_model import Exercise
from app import db
from models.enums import ExerciseTypeEnum, CountTypeEnum

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
def create_exercise():
    data = request.get_json()

    # Validate required fields
    if not data.get("name") or not data.get("count_type"):
        return jsonify({"error": "Name and count type are required"}), 400

    # Create new exercise
    new_exercise = Exercise(
        name=data["name"],
        description=data.get("description", ""),
        category=data.get("category", "strength"),
        count_type=data["count_type"],
        count_value=data.get("count_value", 0),
        equipment_required=data.get("equipment_required", False),
        equipment_optional=data.get("equipment_optional", False),
        equipment_list=data.get("equipment_list", ""),
        recommended_series=data.get("recommended_series", 3),
        suggested_weight=data.get("suggested_weight", 0),
        rest_time=data.get("rest_time", 60),
        execution_tips=data.get("execution_tips", ""),
    )
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify({"message": "Exercise created successfully!"}), 201


@exercise_bp.route("/exercises", methods=["GET"])
@jwt_required()
def get_all_exercises():
    exercises = Exercise.query.all()
    result = [
        {
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "count_type": e.count_type,
            "count_value": e.count_value,
            "equipment_required": e.equipment_required,
        }
        for e in exercises
    ]
    return jsonify(result), 200


@exercise_bp.route("/exercises/<int:exercise_id>", methods=["GET"])
@jwt_required()
def get_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    return (
        jsonify(
            {
                "id": exercise.id,
                "name": exercise.name,
                "description": exercise.description,
                "category": exercise.category,
                "count_type": exercise.count_type,
                "count_value": exercise.count_value,
                "equipment_required": exercise.equipment_required,
                "equipment_list": exercise.equipment_list,
                "recommended_series": exercise.recommended_series,
                "suggested_weight": exercise.suggested_weight,
                "rest_time": exercise.rest_time,
                "execution_tips": exercise.execution_tips,
            }
        ),
        200,
    )


@exercise_bp.route("/exercises/<int:exercise_id>", methods=["PUT"])
@trainer_or_admin_required
def update_exercise(exercise_id):
    data = request.get_json()
    exercise = Exercise.query.get_or_404(exercise_id)

    # Update exercise details
    exercise.name = data.get("name", exercise.name)
    exercise.description = data.get("description", exercise.description)
    exercise.category = data.get("category", exercise.category)
    exercise.count_type = data.get("count_type", exercise.count_type)
    exercise.count_value = data.get("count_value", exercise.count_value)
    exercise.equipment_required = data.get(
        "equipment_required", exercise.equipment_required
    )
    exercise.equipment_optional = data.get(
        "equipment_optional", exercise.equipment_optional
    )
    exercise.equipment_list = data.get("equipment_list", exercise.equipment_list)
    exercise.recommended_series = data.get(
        "recommended_series", exercise.recommended_series
    )
    exercise.suggested_weight = data.get("suggested_weight", exercise.suggested_weight)
    exercise.rest_time = data.get("rest_time", exercise.rest_time)
    exercise.execution_tips = data.get("execution_tips", exercise.execution_tips)

    db.session.commit()
    return jsonify({"message": "Exercise updated successfully!"}), 200


@exercise_bp.route("/exercises/<int:exercise_id>", methods=["DELETE"])
@jwt_required()
def delete_exercise(exercise_id):
    claims = get_jwt_identity()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    exercise = Exercise.query.get_or_404(exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message": "Exercise deleted successfully!"}), 200
