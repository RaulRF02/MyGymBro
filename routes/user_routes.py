from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import register_user, login_user, get_user_profile, change_user_role

user_bp = Blueprint("user_routes", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response, status_code = register_user(data)
    return jsonify(response), status_code


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response, status_code = login_user(data)
    return jsonify(response), status_code


@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    identity = get_jwt_identity()
    user_id = identity["user_id"]
    response, status_code = get_user_profile(user_id)
    return jsonify(response), status_code


@user_bp.route("/profile/<int:user_id>", methods=["GET"])
@jwt_required()
def profile_by_id(user_id):
    claims = get_jwt_identity()
    if claims["role"] not in ["admin", "trainer"] and claims["user_id"] != user_id:
        return jsonify({"error": "Permission denied"}), 403
    response, status_code = get_user_profile(user_id)
    return jsonify(response), status_code


@user_bp.route("/add_admin/<int:user_id>", methods=["PUT"])
@jwt_required()
def add_admin(user_id):
    claims = get_jwt_identity()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    response, status_code = change_user_role(user_id, "admin")
    return jsonify(response), status_code


@user_bp.route("/remove_admin/<int:user_id>", methods=["PUT"])
@jwt_required()
def remove_admin(user_id):
    claims = get_jwt_identity()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    response, status_code = change_user_role(user_id, "trainer")
    return jsonify(response), status_code


@user_bp.route("/add_trainer/<int:user_id>", methods=["PUT"])
@jwt_required()
def add_trainer(user_id):
    claims = get_jwt_identity()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    response, status_code = change_user_role(user_id, "trainer")
    return jsonify(response), status_code


@user_bp.route("/remove_trainer/<int:user_id>", methods=["PUT"])
@jwt_required()
def remove_trainer(user_id):
    claims = get_jwt_identity()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    response, status_code = change_user_role(user_id, "user")
    return jsonify(response), status_code
