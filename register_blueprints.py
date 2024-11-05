from routes.user_routes import user_bp
from routes.routine_routes import routine_bp
from routes.training_plan_routes import training_plan_bp
from routes.exercise_routes import exercise_bp
from routes.progress_route import progress_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(routine_bp, url_prefix='/api')
    app.register_blueprint(training_plan_bp, url_prefix='/api')
    app.register_blueprint(exercise_bp, url_prefix='/api')
    app.register_blueprint(progress_bp, url_prefix='/api')
