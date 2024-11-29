import pytest
from flask import json

def test_create_routine(client, setup_users):
    routine_data = {
        "name": "Leg Day",
        "description": "Focus on legs",
        "objective": "muscle_gain",
        "type": "predefined",
        "weekly_frequency": 3,
        "difficulty_level": "intermediate",
        "start_date": "2024-01-01",
        "end_date": None
    }
    response = client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Routine created successfully!"
    assert "routine_id" in data


def test_get_all_routines(client, setup_users):
    response = client.get("/api/routines", headers=setup_users["regular_headers"])
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    for routine in data:
        assert "id" in routine
        assert "name" in routine
        assert "objective" in routine
        assert "description" in routine


def test_get_routine_by_id(client, setup_users):
    routine_data = {
        "name": "Leg Day",
        "description": "Focus on legs",
        "objective": "muscle_gain",
        "type": "predefined",
        "weekly_frequency": 3,
        "difficulty_level": "intermediate",
        "start_date": "2024-01-01",
        "end_date": None
    }
    create_response = client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    routine_id = create_response.get_json()["routine_id"]

    response = client.get(f"/api/routines/{routine_id}", headers=setup_users["regular_headers"])
    data = response.get_json()
    assert response.status_code == 200
    assert data["id"] == routine_id
    assert data["name"] == "Leg Day"
    assert data["objective"] == "muscle_gain"
    assert data["description"] == "Focus on legs"


def test_update_routine(client, setup_users):
    routine_data = {
        "name": "Leg Day",
        "description": "Focus on legs",
        "objective": "muscle_gain",
        "type": "predefined",
        "weekly_frequency": 3,
        "difficulty_level": "intermediate",
        "start_date": "2024-01-01",
        "end_date": None
    }
    create_response = client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    routine_id = create_response.get_json()["routine_id"]

    updated_data = {"name": "Updated Leg Day", "description": "Updated focus", "objective": "muscle_gain"}
    response = client.put(
        f"/api/routines/{routine_id}",
        data=json.dumps(updated_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Routine updated successfully!"


def test_delete_routine(client, setup_users):
    routine_data = {
        "name": "Leg Day",
        "description": "Focus on legs",
        "objective": "muscle_gain",
        "type": "predefined",
        "weekly_frequency": 3,
        "difficulty_level": "intermediate",
        "start_date": "2024-01-01",
        "end_date": None
    }
    create_response = client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    routine_id = create_response.get_json()["routine_id"]

    response = client.delete(f"/api/routines/{routine_id}", headers=setup_users["admin_headers"])
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Routine deleted successfully!"


def test_add_exercise_to_routine(client, setup_users):
    routine_data = {
        "name": "Leg Day",
        "description": "Focus on legs",
        "objective": "muscle_gain",
        "type": "predefined",
        "weekly_frequency": 3,
        "difficulty_level": "intermediate",
        "start_date": "2024-01-01",
        "end_date": None
    }
    create_response = client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    routine_id = create_response.get_json()["routine_id"]

    exercise_data = {"exercise_id": 1, "series": 3, "repetitions": 10, "weight": 50}
    response = client.post(
        f"/api/routines/{routine_id}/exercises",
        data=json.dumps(exercise_data),
        headers=setup_users["admin_headers"],
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Exercise added to routine successfully!"
