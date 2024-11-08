import pytest
from flask import json


def test_create_exercise(client, auth_headers):
    exercise_data = {
        "name": "Push-up",
        "count_type": "repetitions",
        "count_value": 15,
        "category": "strength",
    }
    response = client.post(
        "/api/exercises",
        data=json.dumps(exercise_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Exercise created successfully!"


def test_get_all_exercises(client, auth_headers):
    response = client.get("/api/exercises", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
