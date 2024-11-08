from app import db


class RoutineExercise(db.Model):
    __tablename__ = "routine_exercises"

    routine_id = db.Column(
        db.Integer, db.ForeignKey("routines.id"), primary_key=True
    )  # FK to Routine
    exercise_id = db.Column(
        db.Integer, db.ForeignKey("exercises.id"), primary_key=True
    )  # FK to Exercise
    series = db.Column(
        db.Integer, nullable=True
    )  # Number of series for this exercise in the routine
    repetitions = db.Column(
        db.Integer, nullable=True
    )  # Number of repetitions for this exercise
    time = db.Column(
        db.Float, nullable=True
    )  # Duration in seconds or minutes, if applicable
    weight = db.Column(db.Float, nullable=True)  # Suggested weight for the exercise

    def __repr__(self):
        return f"<RoutineExercise - Routine {self.routine_id} - Exercise {self.exercise_id}>"
