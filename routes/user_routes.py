from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user_model import User
from extensions import db

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='scrypt')
    new_user = User(
        name=data['name'],
        last_name=data['last_name'],
        dni=data['dni'],
        email=data['email'],
        password=hashed_password,
        role=data.get('role', 'user')  # Default role is 'user'
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
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def user_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        'name': user.name,
        'last_name': user.last_name,
        'email': user.email,
        'role': user.role
    }), 200

