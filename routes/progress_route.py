from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.progress_model import Progress
from app import db

progress_bp = Blueprint("progress_routes", __name__)


@progress_bp.route("/progress", methods=["POST"])
@jwt_required()
def create_progress_record():
    data = request.get_json()
    current_user = get_jwt_identity()
    current_user_id = current_user["user_id"]

    # Validate required fields
    if not data.get("exercise_id") or not data.get("routine_id"):
        return jsonify({"error": "Exercise ID and Routine ID are required"}), 400

    # Create new progress record
    new_progress = Progress(
        # user_id=current_user_id,
        record_date=data.get("record_date"),  # or default to today's date
        exercise_id=data["exercise_id"],
        routine_id=data["routine_id"],
        training_plan_id=data.get("training_plan_id"),
        series_completed=data.get("series_completed", 0),
        repetitions_per_series=data.get("repetitions_per_series", 0),
        time_per_series=data.get("time_per_series", 0),
        weight_used=data.get("weight_used", 0),
        user_notes=data.get("user_notes", ""),
        trainer_notes=data.get("trainer_notes", ""),
        exercise_status=data.get("exercise_status", "completed"),
        perceived_effort=data.get("perceived_effort", 5),
    )
    db.session.add(new_progress)
    db.session.commit()
    return jsonify({"message": "Progress record created successfully!"}), 201


@progress_bp.route("/progress", methods=["GET"])
@jwt_required()
def get_all_progress():
    user_id = get_jwt_identity()["id"]
    progress_records = Progress.query.filter_by(user_id=user_id).all()
    result = [
        {
            "id": p.id,
            "record_date": p.record_date,
            "exercise_id": p.exercise_id,
            "routine_id": p.routine_id,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "user_notes": p.user_notes,
        }
        for p in progress_records
    ]
    return jsonify(result), 200


@progress_bp.route("/progress/exercise/<int:exercise_id>", methods=["GET"])
@jwt_required()
def get_progress_by_exercise(exercise_id):
    user_id = get_jwt_identity()["id"]
    progress_records = Progress.query.filter_by(
        user_id=user_id, exercise_id=exercise_id
    ).all()
    result = [
        {
            "id": p.id,
            "record_date": p.record_date,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "user_notes": p.user_notes,
            "perceived_effort": p.perceived_effort,
        }
        for p in progress_records
    ]
    return jsonify(result), 200


@progress_bp.route("/progress/routine/<int:routine_id>", methods=["GET"])
@jwt_required()
def get_progress_by_routine(routine_id):
    user_id = get_jwt_identity()["id"]
    progress_records = Progress.query.filter_by(
        user_id=user_id, routine_id=routine_id
    ).all()
    result = [
        {
            "id": p.id,
            "record_date": p.record_date,
            "exercise_id": p.exercise_id,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "user_notes": p.user_notes,
            "exercise_status": p.exercise_status,
        }
        for p in progress_records
    ]
    return jsonify(result), 200
