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

def test_get_profile(client, auth_headers):
    response = client.get("/api/users/profile", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert "name" in data
    assert "email" in data


def test_add_admin_success(client, auth_headers, setup_users):
    with client.application.app_context():
        regular_user = User.query.filter_by(email="regular@example.com").first()
        assert regular_user is not None, "Regular user was not created during setup."

    response = client.put(
        f"/api/users/add_admin/{regular_user.id}",
        headers=auth_headers,
    )
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "User role updated to admin successfully."

def test_remove_admin_success(client, auth_headers, setup_users):
    response = client.put("/api/users/remove_admin/2", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "User role updated to trainer successfully."


def test_add_trainer_success(client, auth_headers, setup_users):
    response = client.put("/api/users/add_trainer/3", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "User role updated to trainer successfully."


def test_remove_trainer_success(client, auth_headers, setup_users):
    response = client.put("/api/users/remove_trainer/2", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "User role updated to user successfully."
