import pytest
from app import create_app, db
from models.user_model import User
from flask import json
from werkzeug.security import generate_password_hash


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()

        test_user = User(
            name="Test",
            last_name="User",
            dni="00000000X",
            email="unique@example.com",
            password=generate_password_hash("password123"),
            role="admin",
        )
        db.session.add(test_user)
        db.session.commit()

        yield app.test_client()

        db.session.remove()
        db.drop_all()


@pytest.fixture
def auth_headers(client):
    login_data = {"email": "unique@example.com", "password": "password123"}
    response = client.post(
        "/api/users/login", data=json.dumps(login_data), content_type="application/json"
    )
    token = response.get_json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def setup_users(client):
    """
    Create default users for testing and provide their authentication headers.
    """
    with client.application.app_context():
        admin_user = User(
            name="Admin",
            last_name="User",
            dni="00000001A",
            email="admin@example.com",
            password=generate_password_hash("adminpassword"),
            role="admin",
        )
        trainer_user = User(
            name="Trainer",
            last_name="User",
            dni="00000002B",
            email="trainer@example.com",
            password=generate_password_hash("trainerpassword"),
            role="trainer",
        )
        regular_user = User(
            name="Regular",
            last_name="User",
            dni="00000003C",
            email="regular@example.com",
            password=generate_password_hash("userpassword"),
            role="user",
        )
        db.session.add_all([admin_user, trainer_user, regular_user])
        db.session.commit()

        from flask_jwt_extended import create_access_token

        admin_token = create_access_token(identity={"user_id": admin_user.id, "role": admin_user.role})
        trainer_token = create_access_token(identity={"user_id": trainer_user.id, "role": trainer_user.role})
        regular_token = create_access_token(identity={"user_id": regular_user.id, "role": regular_user.role})

        return {
            "admin_headers": {"Authorization": f"Bearer {admin_token}"},
            "trainer_headers": {"Authorization": f"Bearer {trainer_token}"},
            "regular_headers": {"Authorization": f"Bearer {regular_token}"},
        }