from models.training_plan_model import TrainingPlan
from models.routine_model import Routine
from extensions import db
from logging_config import logger
from datetime import datetime


def create_training_plan(data, current_user_id):
    # Validar campos requeridos
    if not data.get("name") or not data.get("objective"):
        return {"error": "Name and objective are required"}, 400

    # Validar fechas si se envían
    start_date = None
    estimated_end_date = None
    if data.get("start_date"):
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
    if data.get("estimated_end_date"):
        estimated_end_date = datetime.strptime(data["estimated_end_date"], "%Y-%m-%d").date()

    # Crear un nuevo plan de entrenamiento
    new_plan = TrainingPlan(
        name=data["name"],
        description=data.get("description", ""),
        objective=data["objective"],
        duration=data["duration"],
        weekly_frequency=data["weekly_frequency"],
        difficulty_level=data["difficulty_level"],
        assigned_to=data.get("assigned_to"),
        created_by=current_user_id,
        start_date=start_date,
        estimated_end_date=estimated_end_date,
        status=data.get("status", "active"),
        trainer_notes=data.get("trainer_notes", ""),
    )
    db.session.add(new_plan)
    db.session.commit()
    logger.info(f"Training plan '{new_plan.name}' created successfully")
    return {"message": "Training plan created successfully!", "training_plan_id": new_plan.id}, 201


def get_all_training_plans():
    plans = TrainingPlan.query.all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "objective": p.objective,
            "description": p.description,
            "duration": p.duration,
            "weekly_frequency": p.weekly_frequency,
            "difficulty_level": p.difficulty_level,
            "assigned_to": p.assigned_to,
            "created_by": p.created_by,
            "routines": [
                {
                    "id": r.id,
                    "name": r.name,
                    "objective": r.objective,
                    "difficulty_level": r.difficulty_level,
                }
                for r in p.routines
            ],
        }
        for p in plans
    ], 200



def get_training_plan_by_id(plan_id):
    plan = TrainingPlan.query.get_or_404(plan_id)
    return {
        "id": plan.id,
        "name": plan.name,
        "objective": plan.objective,
        "description": plan.description,
        "duration": plan.duration,
        "weekly_frequency": plan.weekly_frequency,
        "difficulty_level": plan.difficulty_level,
        "assigned_to": plan.assigned_to,
        "created_by": plan.created_by,
        "routines": [
            {
                "id": r.id,
                "name": r.name,
                "objective": r.objective,
                "difficulty_level": r.difficulty_level,
                "weekly_frequency": r.weekly_frequency,
            }
            for r in plan.routines
        ],
        "status": plan.status,
        "start_date": plan.start_date,
        "estimated_end_date": plan.estimated_end_date,
        "trainer_notes": plan.trainer_notes,
    }, 200



def update_training_plan(plan_id, data):
    plan = TrainingPlan.query.get_or_404(plan_id)
    plan.name = data.get("name", plan.name)
    plan.description = data.get("description", plan.description)
    plan.objective = data.get("objective", plan.objective)
    plan.duration = data.get("duration", plan.duration)
    db.session.commit()
    logger.info(f"Training plan '{plan.name}' updated successfully")
    return {"message": "Training plan updated successfully!"}, 200


def delete_training_plan(plan_id):
    plan = TrainingPlan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
    logger.info(f"Training plan '{plan.name}' deleted successfully")
    return {"message": "Training plan deleted successfully!"}, 200

def add_routine_to_training_plan(plan_id, routine_id):
    # Obtener el plan de entrenamiento
    training_plan = TrainingPlan.query.get_or_404(plan_id)

    # Obtener la rutina
    routine = Routine.query.get_or_404(routine_id)

    # Validar si la rutina ya está asociada al plan
    if routine in training_plan.routines:
        return {"error": "Routine is already part of the training plan"}, 400

    # Añadir la rutina al plan
    training_plan.routines.append(routine)
    db.session.commit()

    return {
        "message": f"Routine '{routine.name}' added to training plan '{training_plan.name}' successfully!"
    }, 201