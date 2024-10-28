from app import db
from sqlalchemy import ForeignKey
from datetime import datetime


class Progress(db.Model):
    __tablename__ = 'progress_records'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each progress record
    record_date = db.Column(db.Date, default=datetime.utcnow)  # Date of the progress record

    # Relationships with other models
    exercise_id = db.Column(db.Integer, ForeignKey('exercises.id'),
                            nullable=False)  # Exercise performed in this session
    routine_id = db.Column(db.Integer, ForeignKey('routines.id'),
                           nullable=False)  # Routine to which the exercise belongs
    training_plan_id = db.Column(db.Integer, ForeignKey('training_plans.id'),
                                 nullable=True)  # (Optional) Associated training plan

    # Exercise details
    series_completed = db.Column(db.Integer, nullable=True)  # Number of series completed in the session
    repetitions_per_series = db.Column(db.Integer, nullable=True)  # Repetitions per series, if applicable
    time_per_series = db.Column(db.Float, nullable=True)  # Time per series in seconds or minutes, if applicable
    weight_used = db.Column(db.Float, nullable=True)  # Weight used in the exercise, if applicable

    # Additional notes and comments
    user_notes = db.Column(db.Text, nullable=True)  # Comments from the user about the session
    trainer_notes = db.Column(db.Text, nullable=True)  # Comments from the trainer, if applicable

    # Status and effort level
    exercise_status = db.Column(db.String(20), nullable=False,
                                default="completed")  # Status: completed, paused, modified
    perceived_effort = db.Column(db.Integer, nullable=True)  # Optional: user's perceived effort level (1 to 10)

    def __repr__(self):
        return f'<Progress Record for Exercise {self.exercise_id} on {self.record_date}>'
