import pytest
from flask import json


def test_create_training_plan(client, auth_headers):
    plan_data = {
        "name": "Beginner Plan",
        "objective": "weight_loss",
        "duration": 12,
        "weekly_frequency": 3,
        "difficulty_level": "beginner",
        "assigned_to": 1,
    }
    response = client.post(
        "/api/training-plans",
        data=json.dumps(plan_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Training plan created successfully!"


def test_get_all_training_plans(client, auth_headers):
    response = client.get("/api/training-plans", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_training_plan_by_id(client, auth_headers):
    plan_data = {
        "name": "Intermediate Plan",
        "objective": "muscle_gain",
        "duration": 8,
        "weekly_frequency": 4,
        "difficulty_level": "intermediate",
        "assigned_to": 1,
    }
    client.post(
        "/api/training-plans",
        data=json.dumps(plan_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.get("/api/training-plans/1", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["name"] == "Intermediate Plan"

    response = client.get("/api/training-plans/9999", headers=auth_headers)
    assert response.status_code == 404


def test_update_training_plan(client, auth_headers):
    plan_data = {
        "name": "Advanced Plan",
        "objective": "toning",
        "duration": 10,
        "weekly_frequency": 5,
        "difficulty_level": "advanced",
        "assigned_to": 1,
    }
    client.post(
        "/api/training-plans",
        data=json.dumps(plan_data),
        headers=auth_headers,
        content_type="application/json",
    )

    update_data = {"name": "Updated Plan", "duration": 15}
    response = client.put(
        "/api/training-plans/1",
        data=json.dumps(update_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Training plan updated successfully!"

    response = client.put(
        "/api/training-plans/9999",
        data=json.dumps(update_data),
        headers=auth_headers,
        content_type="application/json",
    )
    assert response.status_code == 404


def test_delete_training_plan(client, auth_headers):
    plan_data = {
        "name": "Delete Plan",
        "objective": "weight_loss",
        "duration": 6,
        "weekly_frequency": 3,
        "difficulty_level": "beginner",
        "assigned_to": 1,
    }
    client.post(
        "/api/training-plans",
        data=json.dumps(plan_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.delete("/api/training-plans/1", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Training plan deleted successfully!"

    response = client.delete("/api/training-plans/9999", headers=auth_headers)
    assert response.status_code == 404


def test_add_routine_to_training_plan(client, auth_headers):
    plan_data = {
        "name": "Routine Test Plan",
        "objective": "muscle_gain",
        "duration": 8,
        "weekly_frequency": 4,
        "difficulty_level": "intermediate",
        "assigned_to": 1,
    }
    client.post(
        "/api/training-plans",
        data=json.dumps(plan_data),
        headers=auth_headers,
        content_type="application/json",
    )

    routine_data = {"name": "Test Routine", "objective": "weight_loss", "difficulty_level": "beginner"}
    client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=auth_headers,
        content_type="application/json",
    )

    add_routine_data = {"routine_id": 1}
    response = client.post(
        "/api/training-plans/1/routines",
        data=json.dumps(add_routine_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert "Routine 'Test Routine' added" in data["message"]

    response = client.post(
        "/api/training-plans/1/routines",
        data=json.dumps(add_routine_data),
        headers=auth_headers,
        content_type="application/json",
    )
    assert response.status_code == 400

    response = client.post(
        "/api/training-plans/1/routines",
        data=json.dumps({"routine_id": 9999}),
        headers=auth_headers,
        content_type="application/json",
    )
    assert response.status_code == 404