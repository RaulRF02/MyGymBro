import pytest
from flask import json


def test_create_routine(client, auth_headers):
    routine_data = {"name": "Leg Day", "objective": "muscle_gain"}
    response = client.post(
        "/api/routines",
        data=json.dumps(routine_data),
        headers=auth_headers,
        content_type="application/json",
    )
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Routine created successfully!"


def test_get_all_routines(client, auth_headers):
    response = client.get("/api/routines", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
