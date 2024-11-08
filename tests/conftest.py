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
