from app import db
from models.enums import ExerciseTypeEnum, CountTypeEnum

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each exercise
    name = db.Column(db.String(100), nullable=False)  # Descriptive name of the exercise
    description = db.Column(db.Text, nullable=True)  # Brief description and benefits of the exercise
    category = db.Column(ExerciseTypeEnum)  # General category of the exercise

    # Type of exercise count
    count_type = db.Column(CountTypeEnum, nullable=False)  # Indicates if the exercise is by reps or time
    count_value = db.Column(db.Integer,
                            nullable=True)  # Number of repetitions or time duration, depending on count_type

    # Associated equipment
    equipment_required = db.Column(db.Boolean, default=False)  # Indicates if equipment is necessary
    equipment_optional = db.Column(db.Boolean, default=False)  # Indicates if equipment is optional
    equipment_list = db.Column(db.String(200),
                               nullable=True)  # List of required equipment (e.g., "dumbbells, resistance bands")

    # Execution details
    recommended_series = db.Column(db.Integer, nullable=True)  # Suggested number of series
    suggested_weight = db.Column(db.Float, nullable=True)  # Recommended weight for the exercise, if applicable
    rest_time = db.Column(db.Integer, nullable=True)  # Rest time between series in seconds

    # Additional info and tips
    visual_demo = db.Column(db.String(200), nullable=True)  # Link to video or image demonstration (optional)
    execution_tips = db.Column(db.Text, nullable=True)  # Tips for proper form and avoiding injury

    def __repr__(self):
        return f'<Exercise {self.name} - Category: {self.category}>'
