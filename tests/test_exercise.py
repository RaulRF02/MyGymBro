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


def test_get_exercise_by_id(client, auth_headers):
    exercise_data = {
        "name": "Pull-up",
        "count_type": "repetitions",
        "count_value": 10,
        "category": "strength",
    }
    client.post(
        "/api/exercises",
        data=json.dumps(exercise_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.get("/api/exercises/1", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["name"] == "Pull-up"

    response = client.get("/api/exercises/9999", headers=auth_headers)
    assert response.status_code == 404


def test_update_exercise(client, auth_headers):
    exercise_data = {
        "name": "Squat",
        "count_type": "repetitions",
        "count_value": 20,
        "category": "strength",
    }
    client.post(
        "/api/exercises",
        data=json.dumps(exercise_data),
        headers=auth_headers,
        content_type="application/json",
    )

    update_data = {"name": "Squat Updated", "count_value": 25}
    response = client.put(
        "/api/exercises/1",
        data=json.dumps(update_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Exercise updated successfully!"

    response = client.put(
        "/api/exercises/9999",
        data=json.dumps(update_data),
        headers=auth_headers,
        content_type="application/json",
    )
    assert response.status_code == 404


def test_delete_exercise(client, auth_headers):
    exercise_data = {
        "name": "Deadlift",
        "count_type": "repetitions",
        "count_value": 5,
        "category": "strength",
    }
    client.post(
        "/api/exercises",
        data=json.dumps(exercise_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.delete("/api/exercises/1", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Exercise deleted successfully!"

    response = client.delete("/api/exercises/9999", headers=auth_headers)
    assert response.status_code == 404
