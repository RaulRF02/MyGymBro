from sqlalchemy.orm import relationship

from app import db
from models.enums import (
    RoutineTypeEnum,
    DifficultyLevelEnum,
    RoutineStatusEnum,
    TrainingGoalEnum,
)
from datetime import datetime
from models.routine_exercise import RoutineExercise


class Routine(db.Model):
    __tablename__ = "routines"

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each routine
    name = db.Column(db.String(100), nullable=False)  # Descriptive name for the routine
    description = db.Column(
        db.Text, nullable=True
    )  # Brief explanation of the routine's purpose and benefits
    objective = db.Column(TrainingGoalEnum)  # Main objective
    routine_type = db.Column(RoutineTypeEnum, default="predefined")  # Type of routine
    training_plan_id = db.Column(
        db.Integer, db.ForeignKey("training_plans.id"), nullable=True
    )  # FK a TrainingPlan (opcional)
    training_plan = relationship("TrainingPlan", back_populates="routines")
    # Exercise details
    exercises = db.relationship(
        "Exercise", secondary="routine_exercises", backref="routines"
    )  # Many-to-Many with Exercise
    series = db.Column(db.Integer, nullable=True)  # Recommended series count
    repetitions = db.Column(db.Integer, nullable=True)  # Recommended repetitions count
    recommended_weight = db.Column(db.Float, nullable=True)  # Suggested initial weight

    # Scheduling and duration
    weekly_frequency = db.Column(db.Integer, nullable=True)  # Recommended days per week
    difficulty_level = db.Column(DifficultyLevelEnum)  # Difficulty level

    # Relationship with users
    created_by = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=True
    )  # Trainer or admin who created it
    assigned_to = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=True
    )  # User assigned to this routine (for custom routines)
    current_progress = db.Column(DifficultyLevelEnum)  # Routine status

    # Date fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Creation date
    start_date = db.Column(db.Date, nullable=True)  # Start date for the user
    end_date = db.Column(db.Date, nullable=True)  # Estimated or actual end date

    # Optional notes
    notes = db.Column(
        db.Text, nullable=True
    )  # Space for trainers or users to add comments

    def __repr__(self):
        return f"<Routine {self.name} - Objective: {self.objective}>"
