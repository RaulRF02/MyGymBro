from models.exercise_model import Exercise
from extensions import db
from logging_config import logger


def create_exercise(data):
    # Validar campos requeridos
    if not data.get("name") or not data.get("count_type"):
        return {"error": "Name and count type are required"}, 400

    # Crear nuevo ejercicio
    new_exercise = Exercise(
        name=data["name"],
        description=data.get("description", ""),
        category=data.get("category", "strength"),
        count_type=data["count_type"],
        count_value=data.get("count_value", 0),
        equipment_required=data.get("equipment_required", False),
        equipment_optional=data.get("equipment_optional", False),
        equipment_list=data.get("equipment_list", ""),
        recommended_series=data.get("recommended_series", 3),
        suggested_weight=data.get("suggested_weight", 0),
        rest_time=data.get("rest_time", 60),
        execution_tips=data.get("execution_tips", ""),
    )
    db.session.add(new_exercise)
    db.session.commit()
    logger.info(f"Exercise '{new_exercise.name}' created successfully")
    return {"message": "Exercise created successfully!"}, 201


def get_all_exercises():
    exercises = Exercise.query.all()
    return [
        {
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "count_type": e.count_type,
            "count_value": e.count_value,
            "equipment_required": e.equipment_required,
        }
        for e in exercises
    ], 200


def get_exercise_by_id(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    return {
        "id": exercise.id,
        "name": exercise.name,
        "description": exercise.description,
        "category": exercise.category,
        "count_type": exercise.count_type,
        "count_value": exercise.count_value,
        "equipment_required": exercise.equipment_required,
        "equipment_list": exercise.equipment_list,
        "recommended_series": exercise.recommended_series,
        "suggested_weight": exercise.suggested_weight,
        "rest_time": exercise.rest_time,
        "execution_tips": exercise.execution_tips,
    }, 200


def update_exercise(exercise_id, data):
    exercise = Exercise.query.get_or_404(exercise_id)
    exercise.name = data.get("name", exercise.name)
    exercise.description = data.get("description", exercise.description)
    exercise.category = data.get("category", exercise.category)
    exercise.count_type = data.get("count_type", exercise.count_type)
    exercise.count_value = data.get("count_value", exercise.count_value)
    exercise.equipment_required = data.get("equipment_required", exercise.equipment_required)
    exercise.equipment_optional = data.get("equipment_optional", exercise.equipment_optional)
    exercise.equipment_list = data.get("equipment_list", exercise.equipment_list)
    exercise.recommended_series = data.get("recommended_series", exercise.recommended_series)
    exercise.suggested_weight = data.get("suggested_weight", exercise.suggested_weight)
    exercise.rest_time = data.get("rest_time", exercise.rest_time)
    exercise.execution_tips = data.get("execution_tips", exercise.execution_tips)
    db.session.commit()
    logger.info(f"Exercise '{exercise.name}' updated successfully")
    return {"message": "Exercise updated successfully!"}, 200


def delete_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    logger.info(f"Exercise '{exercise.name}' deleted successfully")
    return {"message": "Exercise deleted successfully!"}, 200
