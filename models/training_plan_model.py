from sqlalchemy.orm import relationship

from app import db
from sqlalchemy import ForeignKey
from datetime import datetime
from models.enums import DifficultyLevelEnum, TrainingGoalEnum

class TrainingPlan(db.Model):
    __tablename__ = 'training_plans'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each training plan
    name = db.Column(db.String(100), nullable=False)  # Descriptive name for the plan
    description = db.Column(db.Text, nullable=True)  # General description and purpose of the plan
    objective = db.Column(TrainingGoalEnum)  # Main goal of the plan (weight_loss, muscle_gain, toning)

    # General guidelines
    duration = db.Column(db.Integer, nullable=False)  # Total duration in weeks or months
    weekly_frequency = db.Column(db.Integer, nullable=False)  # Days per week recommended for training
    difficulty_level = db.Column(DifficultyLevelEnum)  # Difficulty level (beginner, intermediate, advanced)

    # Relationship with routines
    routines = relationship("Routine", back_populates="training_plan")
    sequence = db.Column(db.JSON, nullable=True)  # Sequence for daily routines (e.g., { "day1": "routine1_id", ... })
    additional_guidelines = db.Column(db.Text, nullable=True)  # Additional recommendations (e.g., active rest, recovery days)

    # Relationship with user and trainer
    assigned_to = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)  # User assigned to this training plan
    created_by = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)  # Trainer or admin who created the plan

    # Status and progress control
    start_date = db.Column(db.Date, nullable=True)  # Start date of the plan for the user
    estimated_end_date = db.Column(db.Date, nullable=True)  # Estimated end date
    status = db.Column(db.String(20), nullable=False, default="active")  # Status of the plan (active, completed, paused)
    progress_history = db.relationship('Progress', backref='training_plan', lazy=True)  # Progress history of the plan

    # Optional notes and adaptations
    trainer_notes = db.Column(db.Text, nullable=True)  # Notes by the trainer for each phase or stage of the plan

    def __repr__(self):
        return f'<TrainingPlan {self.name} - Objective: {self.objective}>'
