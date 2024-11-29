import pytest
from flask import json


def test_create_progress_record(client, auth_headers):
    progress_data = {
        "exercise_id": 1,
        "routine_id": 1,
        "series_completed": 3,
        "repetitions_per_series": 10,
        "weight_used": 15,
    }
    response = client.post(
        "/api/progress",
        data=json.dumps(progress_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Progress record created successfully!"


def test_get_all_progress(client, auth_headers):
    progress_data = {
        "exercise_id": 1,
        "routine_id": 1,
        "series_completed": 3,
        "repetitions_per_series": 10,
        "weight_used": 15,
    }
    client.post(
        "/api/progress",
        data=json.dumps(progress_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.get("/api/progress", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "exercise_id" in data[0]
    assert "routine_id" in data[0]


def test_get_progress_by_exercise(client, auth_headers):
    progress_data = {
        "exercise_id": 1,
        "routine_id": 1,
        "series_completed": 3,
        "repetitions_per_series": 10,
        "weight_used": 15,
    }
    client.post(
        "/api/progress",
        data=json.dumps(progress_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.get("/api/progress/exercise/1", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0

    assert data[0]["id"] == 1
    assert "repetitions_per_series" in data[0]
    assert "weight_used" in data[0]
    assert data[0]["repetitions_per_series"] == 10
    assert data[0]["weight_used"] == 15


def test_get_progress_by_routine(client, auth_headers):
    progress_data = {
        "exercise_id": 1,
        "routine_id": 1,
        "series_completed": 3,
        "repetitions_per_series": 10,
        "weight_used": 15,
    }
    client.post(
        "/api/progress",
        data=json.dumps(progress_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.get("/api/progress/routine/1", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "id" in data[0]
    assert "exercise_id" in data[0]
    assert "exercise_status" in data[0]
    assert "record_date" in data[0]
    assert data[0]["exercise_id"] == 1
    assert data[0]["exercise_status"] == "completed"


def test_get_user_progress(client, setup_users):
    progress_data = {
        "exercise_id": 1,
        "routine_id": 1,
        "series_completed": 3,
        "repetitions_per_series": 10,
        "weight_used": 15,
    }
    client.post(
        "/api/progress",
        data=json.dumps(progress_data),
        headers=setup_users["regular_headers"],
        content_type="application/json",
    )

    response = client.get("/api/progress/user/1", headers=setup_users["admin_headers"])
    assert response.status_code == 200

    response = client.get("/api/progress/user/1", headers=setup_users["regular_headers"])
    assert response.status_code == 403


def test_get_my_progress(client, auth_headers):
    progress_data = {
        "exercise_id": 1,
        "routine_id": 1,
        "series_completed": 3,
        "repetitions_per_series": 10,
        "weight_used": 15,
    }
    client.post(
        "/api/progress",
        data=json.dumps(progress_data),
        headers=auth_headers,
        content_type="application/json",
    )

    response = client.get("/api/progress/my-progress", headers=auth_headers)
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "exercise_id" in data[0]
    assert "routine_id" in data[0]
