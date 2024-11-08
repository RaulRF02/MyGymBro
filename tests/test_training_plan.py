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
