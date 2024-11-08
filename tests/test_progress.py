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
