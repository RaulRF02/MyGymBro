from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.progress_service import (
    create_progress_record,
    get_all_progress,
    get_progress_by_exercise,
    get_progress_by_routine,
    get_user_progress
)

progress_bp = Blueprint("progress_routes", __name__)

@progress_bp.route("/progress", methods=["POST"])
@jwt_required()
def create_progress_route():
    data = request.get_json()
    current_user = get_jwt_identity()
    current_user_id = current_user["user_id"]
    return jsonify(create_progress_record(data, current_user_id))


@progress_bp.route("/progress", methods=["GET"])
@jwt_required()
def get_all_progress_route():
    current_user = get_jwt_identity()
    user_id = current_user["user_id"]
    return jsonify(get_all_progress(user_id))


@progress_bp.route("/progress/exercise/<int:exercise_id>", methods=["GET"])
@jwt_required()
def get_progress_by_exercise_route(exercise_id):
    current_user = get_jwt_identity()
    user_id = current_user["user_id"]
    return jsonify(get_progress_by_exercise(user_id, exercise_id))


@progress_bp.route("/progress/routine/<int:routine_id>", methods=["GET"])
@jwt_required()
def get_progress_by_routine_route(routine_id):
    current_user = get_jwt_identity()
    user_id = current_user["user_id"]
    return jsonify(get_progress_by_routine(user_id, routine_id))

@progress_bp.route("/progress/user/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user_progress_route(user_id):
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return {"error": "Access forbidden: Admin only"}, 403
    return jsonify(get_user_progress(user_id))


@progress_bp.route("/progress/my-progress", methods=["GET"])
@jwt_required()
def get_my_progress_route():
    current_user = get_jwt_identity()
    user_id = current_user["user_id"]
    return jsonify(get_all_progress(user_id))