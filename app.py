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

    from models.exercise_model import Exercise
    from models.routine_model import Routine
    from models.routine_exercise import RoutineExercise
    from models.training_plan_model import TrainingPlan
    from models.progress_model import Progress

    # Register blueprints
    register_blueprints(app)

    return app
