import pytest
from app import db
from models.user_model import User
from flask import json
from werkzeug.security import generate_password_hash


def test_register_user(client):
    user_data = {
        "name": "John",
        "last_name": "Doe",
        "dni": "12345678A",
        "email": "john.doe@example.com",
        "password": "securepassword123",
    }
    response = client.post(
        "/api/users/register",
        data=json.dumps(user_data),
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "User registered successfully!"


def test_register_user_existing_email(client):
    with client.application.app_context():
        existing_user = User(
            name="Jane",
            last_name="Smith",
            dni="87654321B",
            email="jane.smith@example.com",
            password=generate_password_hash("password123"),
        )
        db.session.add(existing_user)
        db.session.commit()

    user_data = {
        "name": "Jane",
        "last_name": "Doe",
        "dni": "87654321B",
        "email": "jane.smith@example.com",
        "password": "password123",
    }
    response = client.post(
        "/api/users/register",
        data=json.dumps(user_data),
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 409
    assert data["error"] == "Email already exists."


def test_login_user_success(client):
    with client.application.app_context():
        user = User(
            name="Alice",
            last_name="Wonderland",
            dni="12398765C",
            email="alice@example.com",
            password=generate_password_hash("mypassword123"),
        )
        db.session.add(user)
        db.session.commit()

    login_data = {"email": "alice@example.com", "password": "mypassword123"}
    response = client.post(
        "/api/users/login", data=json.dumps(login_data), content_type="application/json"
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "access_token" in data


def test_login_user_invalid_credentials(client):
    login_data = {"email": "nonexistent@example.com", "password": "wrongpassword"}
    response = client.post(
        "/api/users/login", data=json.dumps(login_data), content_type="application/json"
    )
    data = response.get_json()
    assert response.status_code == 401
    assert data["message"] == "Invalid email or password"
