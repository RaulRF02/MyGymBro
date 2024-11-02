from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user_model import User
from extensions import db

user_bp = Blueprint('user_routes', __name__)


@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Validate required fields
    if not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password are required.'}), 400

    # Check for existing email
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists.'}), 409

    # Hash password and create new user with default role 'user'
    hashed_password = generate_password_hash(data['password'], method='scrypt')
    new_user = User(
        name=data['name'],
        last_name=data['last_name'],
        dni=data['dni'],
        email=data['email'],
        password=hashed_password,
        role='user'
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201


@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create a JWT token for the user
    access_token = create_access_token(identity={"user_id": user.id, "role": user.role})
    return jsonify({'access_token': access_token}), 200

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def user_profile():
    identity = get_jwt_identity()
    user_id = identity["user_id"]
    user = User.query.get(user_id)
    return jsonify({
        'name': user.name,
        'last_name': user.last_name,
        'email': user.email,
        'role': user.role
    }), 200


@user_bp.route('/profile/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_profile(user_id):
    claims = get_jwt_identity()
    if claims['role'] not in ['admin', 'trainer'] and claims['id'] != user_id:
        return jsonify({"error": "You do not have permission to view this profile."}), 403

    user = User.query.get_or_404(user_id)

    user_data = {
        "email": user.email,
        "last_name": user.last_name,
        "name": user.name,
        "dni": user.dni,
        "birth_date": user.birth_date,
        "gender": user.gender,
        "height": user.height,
        "initial_weight": user.initial_weight,
        "training_goal": user.training_goal,
        "subscription_status": user.subscription_status,
        "role": user.role
    }

    return jsonify(user_data), 200


def admin_required(fn):
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt_identity()
        if claims['role'] != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    wrapper.__name__ = fn.__name__
    return wrapper

@user_bp.route('/add_admin/<int:user_id>', methods=['PUT'])
@admin_required
def add_admin_role(user_id):
    user = User.query.get_or_404(user_id)
    if user.role == 'admin':
        return jsonify({'message': 'User is already an admin.'}), 200

    user.role = 'admin'
    db.session.commit()
    return jsonify({'message': 'Admin role granted successfully.'}), 200

@user_bp.route('/remove_admin/<int:user_id>', methods=['PUT'])
@admin_required
def remove_admin_role(user_id):
    user = User.query.get_or_404(user_id)
    if user.role != 'admin':
        return jsonify({'error': 'User is not an admin.'}), 400

    user.role = 'trainer'
    db.session.commit()
    return jsonify({'message': 'Admin role revoked successfully.'}), 200

@user_bp.route('/add_trainer/<int:user_id>', methods=['PUT'])
@admin_required
def add_trainer_role(user_id):
    user = User.query.get_or_404(user_id)
    if user.role == 'trainer':
        return jsonify({'message': 'User is already a trainer.'}), 200

    user.role = 'trainer'
    db.session.commit()
    return jsonify({'message': 'Trainer role granted successfully.'}), 200

@user_bp.route('/remove_trainer/<int:user_id>', methods=['PUT'])
@admin_required
def remove_trainer_role(user_id):
    user = User.query.get_or_404(user_id)
    if user.role != 'trainer':
        return jsonify({'error': 'User is not a trainer.'}), 400

    user.role = 'user'
    db.session.commit()
    return jsonify({'message': 'Trainer role revoked successfully.'}), 200
