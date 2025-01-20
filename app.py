from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from config.settings import Config
from extensions import db, jwt
from register_blueprints import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    api = Api(app)
    swagger = Swagger(
        app, config=app.config["SWAGGER"], template_file="docs/swagger.yaml"
    )

    # Crear tablas solo si no existen
    with app.app_context():
        inspect_and_create_tables(app)

    # Registrar blueprints
    register_blueprints(app)

    return app


def inspect_and_create_tables(app):
    """
    Inspecciona las tablas existentes en la base de datos
    y las crea solo si no están presentes.
    """
    from sqlalchemy import inspect

    inspector = inspect(db.engine)
    existing_tables = inspector.get_table_names()

    from models.exercise_model import Exercise
    from models.routine_model import Routine
    from models.routine_exercise import RoutineExercise
    from models.training_plan_model import TrainingPlan
    from models.progress_model import Progress

    # Lista de todas las tablas definidas en tu proyecto
    tables_to_check = [
        Exercise.__tablename__,
        Routine.__tablename__,
        RoutineExercise.__tablename__,
        TrainingPlan.__tablename__,
        Progress.__tablename__,
    ]

    # Crear tablas solo si no existen
    for table in tables_to_check:
        if table not in existing_tables:
            db.create_all()
            break
