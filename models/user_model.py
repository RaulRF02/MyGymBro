from app import db
from models.enums import UserRoleEnum, TrainingGoalEnum
from datetime import date


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)  # ID único del usuario
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(UserRoleEnum, nullable=False, default="user")

    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    height = db.Column(db.Float)  # Centimeters
    initial_weight = db.Column(db.Float)  # Inital weigh in Kg
    training_goal = db.Column(TrainingGoalEnum)
    subscription_status = db.Column(db.Boolean, default=False)

    # Relación con otros modelos (a implementar en el futuro)
    # plans = db.relationship('TrainingPlan', backref='user', lazy=True)
    # routines = db.relationship('Routine', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} - {self.email}>"
