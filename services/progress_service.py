from models.progress_model import Progress
from extensions import db
from logging_config import logger


def create_progress_record(data, current_user_id):
    # Validar campos requeridos
    if not data.get("exercise_id") or not data.get("routine_id"):
        return {"error": "Exercise ID and Routine ID are required"}, 400

    # Crear un nuevo registro de progreso
    new_progress = Progress(
        user_id=current_user_id,
        record_date=data.get("record_date"),
        exercise_id=data["exercise_id"],
        routine_id=data["routine_id"],
        training_plan_id=data.get("training_plan_id"),
        series_completed=data.get("series_completed", 0),
        repetitions_per_series=data.get("repetitions_per_series", 0),
        time_per_series=data.get("time_per_series", 0),
        weight_used=data.get("weight_used", 0),
        user_notes=data.get("user_notes", ""),
        trainer_notes=data.get("trainer_notes", ""),
        exercise_status=data.get("exercise_status", "completed"),
        perceived_effort=data.get("perceived_effort", 5),
    )
    db.session.add(new_progress)
    db.session.commit()
    logger.info(f"Progress record created for user {current_user_id}")
    return {"message": "Progress record created successfully!"}, 201


def get_all_progress(user_id):
    progress_records = Progress.query.filter_by(user_id=user_id).all()
    return [
        {
            "id": p.id,
            "record_date": p.record_date,
            "exercise_id": p.exercise_id,
            "routine_id": p.routine_id,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "user_notes": p.user_notes,
        }
        for p in progress_records
    ], 200


def get_progress_by_exercise(user_id, exercise_id):
    progress_records = Progress.query.filter_by(user_id=user_id, exercise_id=exercise_id).all()
    return [
        {
            "id": p.id,
            "record_date": p.record_date,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "user_notes": p.user_notes,
            "perceived_effort": p.perceived_effort,
        }
        for p in progress_records
    ], 200


def get_progress_by_routine(user_id, routine_id):
    progress_records = Progress.query.filter_by(user_id=user_id, routine_id=routine_id).all()
    return [
        {
            "id": p.id,
            "record_date": p.record_date,
            "exercise_id": p.exercise_id,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "exercise_status": p.exercise_status,
        }
        for p in progress_records
    ], 200

def get_user_progress(user_id):
    progress_records = Progress.query.filter_by(user_id=user_id).all()
    return [
        {
            "id": p.id,
            "record_date": p.record_date,
            "exercise_id": p.exercise_id,
            "routine_id": p.routine_id,
            "series_completed": p.series_completed,
            "repetitions_per_series": p.repetitions_per_series,
            "weight_used": p.weight_used,
            "user_notes": p.user_notes,
        }
        for p in progress_records
    ], 200
