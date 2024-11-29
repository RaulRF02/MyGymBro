from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from models.user_model import User
from extensions import db
from logging_config import logger


def register_user(data):
    # Validar campos requeridos
    if not data.get("email") or not data.get("password"):
        return {"error": "Email and password are required."}, 400

    # Verificar si el email ya existe
    if User.query.filter_by(email=data["email"]).first():
        return {"error": "Email already exists."}, 409

    # Crear nuevo usuario con rol 'user' por defecto
    hashed_password = generate_password_hash(data["password"], method="scrypt")
    new_user = User(
        name=data["name"],
        last_name=data["last_name"],
        dni=data["dni"],
        email=data["email"],
        password=hashed_password,
        role="user",
    )
    db.session.add(new_user)
    db.session.commit()
    logger.info(f"User {data['email']} registered successfully")
    return {"message": "User registered successfully!"}, 201


def login_user(data):
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return {"message": "Invalid email or password"}, 401

    access_token = create_access_token(identity={"user_id": user.id, "role": user.role})
    logger.info(f"User {data['email']} logged in")
    return {"access_token": access_token}, 200


def get_user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return {
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
        "role": user.role,
    }, 200


def change_user_role(user_id, role):
    user = User.query.get_or_404(user_id)
    user.role = role
    db.session.commit()
    logger.info(f"User {user.email} role updated to {role}")
    return {"message": f"User role updated to {role} successfully."}, 200
