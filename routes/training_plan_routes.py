from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.training_plan_service import (
    create_training_plan,
    get_all_training_plans,
    get_training_plan_by_id,
    update_training_plan,
    delete_training_plan,
    add_routine_to_training_plan
)

training_plan_bp = Blueprint("training_plan_routes", __name__)

@training_plan_bp.route("/training-plans", methods=["POST"])
@jwt_required()
def create_training_plan_route():
    data = request.get_json()
    current_user = get_jwt_identity()
    current_user_id = current_user["user_id"]
    response, status_code = create_training_plan(data, current_user_id)
    return jsonify(response), status_code


@training_plan_bp.route("/training-plans", methods=["GET"])
@jwt_required()
def get_all_training_plans_route():
    response, status_code = get_all_training_plans()
    return jsonify(response), status_code


@training_plan_bp.route("/training-plans/<int:plan_id>", methods=["GET"])
@jwt_required()
def get_training_plan_route(plan_id):
    response, status_code = get_training_plan_by_id(plan_id)
    return jsonify(response), status_code


@training_plan_bp.route("/training-plans/<int:plan_id>", methods=["PUT"])
@jwt_required()
def update_training_plan_route(plan_id):
    data = request.get_json()
    response, status_code = update_training_plan(plan_id, data)
    return jsonify(response), status_code


@training_plan_bp.route("/training-plans/<int:plan_id>", methods=["DELETE"])
@jwt_required()
def delete_training_plan_route(plan_id):
    response, status_code = delete_training_plan(plan_id)
    return jsonify(response), status_code


@training_plan_bp.route("/training-plans/<int:plan_id>/routines", methods=["POST"])
@jwt_required()
def add_routine_to_training_plan_route(plan_id):
    data = request.get_json()
    routine_id = data.get("routine_id")

    if not routine_id:
        return jsonify({"error": "Routine ID is required"}), 400

    response, status_code = add_routine_to_training_plan(plan_id, routine_id)
    return jsonify(response), status_code
