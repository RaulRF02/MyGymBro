from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.routine_service import (
    create_routine,
    get_all_routines,
    get_routine_by_id,
    update_routine,
    delete_routine,
    add_exercise_to_routine
)

routine_bp = Blueprint("routine_routes", __name__)

# Helper function to ensure only admins can access certain endpoints
def admin_required(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt_identity()
        if claims["role"] != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)

    wrapper.__name__ = fn.__name__
    return wrapper


@routine_bp.route("/routines", methods=["POST"])
@admin_required
def create_routine_route():
    data = request.get_json()
    return jsonify(create_routine(data))


@routine_bp.route("/routines", methods=["GET"])
@jwt_required()
def get_all_routines_route():
    return jsonify(get_all_routines())


@routine_bp.route("/routines/<int:routine_id>", methods=["GET"])
@jwt_required()
def get_routine_route(routine_id):
    return jsonify(get_routine_by_id(routine_id))


@routine_bp.route("/routines/<int:routine_id>", methods=["PUT"])
@admin_required
def update_routine_route(routine_id):
    data = request.get_json()
    return jsonify(update_routine(routine_id, data))


@routine_bp.route("/routines/<int:routine_id>", methods=["DELETE"])
@admin_required
def delete_routine_route(routine_id):
    return jsonify(delete_routine(routine_id))

@routine_bp.route("/routines/<int:routine_id>/exercises", methods=["POST"])
@admin_required
def add_exercise_to_routine_route(routine_id):
    exercise_data = request.get_json()
    return jsonify(add_exercise_to_routine(routine_id, exercise_data))
