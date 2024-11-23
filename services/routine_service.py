from models.routine_model import Routine
from models.routine_exercise import RoutineExercise
from extensions import db
from logging_config import logger
from flask_jwt_extended import get_jwt_identity
from datetime import datetime


def create_routine(data):
    # Validar campos requeridos
    if not data.get("name") or not data.get("objective"):
        return {"error": "Name and objective are required"}, 400

    # Obtener el usuario autenticado
    current_user = get_jwt_identity()

    # Convertir fechas a objetos date de Python (si están presentes)
    start_date = None
    end_date = None
    if data.get("start_date"):
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
    if data.get("end_date"):
        end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()

    # Crear nueva rutina
    new_routine = Routine(
        name=data["name"],
        description=data.get("description", ""),
        objective=data["objective"],
        routine_type=data.get("type", "predefined"),
        weekly_frequency=data.get("weekly_frequency", 3),
        difficulty_level=data.get("difficulty_level", "beginner"),
        created_by=current_user["user_id"],  # Asignar el usuario actual
        assigned_to=data.get("assigned_to"),
        start_date=start_date,
        end_date=end_date
    )
    db.session.add(new_routine)
    db.session.commit()
    return {"message": "Routine created successfully!", "routine_id": new_routine.id}, 201


def get_all_routines():
    routines = Routine.query.all()
    return [
        {
            "id": r.id,
            "name": r.name,
            "objective": r.objective,
            "description": r.description,
            "weekly_frequency": r.weekly_frequency,
            "difficulty_level": r.difficulty_level if r.difficulty_level else None,
            "exercises": [
                {
                    "exercise_id": e.id,
                    "name": e.name,
                    "series": re.series,
                    "repetitions": re.repetitions,
                    "time": re.time,
                    "weight": re.weight
                }
                for e in r.exercises
                for re in RoutineExercise.query.filter_by(routine_id=r.id, exercise_id=e.id)
            ]
        }
        for r in routines
    ], 200


def get_routine_by_id(routine_id):
    routine = Routine.query.get_or_404(routine_id)
    return {
        "id": routine.id,
        "name": routine.name,
        "objective": routine.objective,
        "description": routine.description,
        "weekly_frequency": routine.weekly_frequency,
        "difficulty_level": routine.difficulty_level if routine.difficulty_level else None,
        "created_by": routine.created_by,
        "assigned_to": routine.assigned_to,
        "start_date": routine.start_date,
        "end_date": routine.end_date,
        "exercises": [
            {
                "exercise_id": e.id,
                "name": e.name,
                "series": re.series,
                "repetitions": re.repetitions,
                "time": re.time,
                "weight": re.weight
            }
            for e in routine.exercises
            for re in RoutineExercise.query.filter_by(routine_id=routine.id, exercise_id=e.id)
        ]
    }, 200




def update_routine(routine_id, data):
    routine = Routine.query.get_or_404(routine_id)
    routine.name = data.get("name", routine.name)
    routine.description = data.get("description", routine.description)
    routine.objective = data.get("objective", routine.objective)
    db.session.commit()
    logger.info(f"Routine '{routine.name}' updated successfully")
    return {"message": "Routine updated successfully!"}, 200


def delete_routine(routine_id):
    routine = Routine.query.get_or_404(routine_id)
    db.session.delete(routine)
    db.session.commit()
    logger.info(f"Routine '{routine.name}' deleted successfully")
    return {"message": "Routine deleted successfully!"}, 200

def add_exercise_to_routine(routine_id, exercise_data):
    routine = Routine.query.get_or_404(routine_id)

    exercise_id = exercise_data.get("exercise_id")
    if not exercise_id:
        return {"error": "Exercise ID is required"}, 400

    # Validar si el ejercicio ya está asignado a la rutina
    existing_assignment = RoutineExercise.query.filter_by(routine_id=routine_id, exercise_id=exercise_id).first()
    if existing_assignment:
        return {"error": "Exercise already assigned to this routine"}, 400

    # Crear la relación entre rutina y ejercicio
    new_routine_exercise = RoutineExercise(
        routine_id=routine_id,
        exercise_id=exercise_id,
        series=exercise_data.get("series", 3),
        repetitions=exercise_data.get("repetitions", 10),
        time=exercise_data.get("time"),
        weight=exercise_data.get("weight", 0)
    )
    db.session.add(new_routine_exercise)
    db.session.commit()
    return {"message": "Exercise added to routine successfully!"}, 201

