import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecretkey")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    SWAGGER = {
        "title": "MyGymBro API",
        "uiversion": 3,
        "openapi": "3.0.0",
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
        "headers": [],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the token",
            }
        },
        "security": [{"Bearer": []}],
    }

    if os.environ.get('FLASK_ENV') == 'production':
        SQLALCHEMY_DATABASE_URI = "postgres://u9ivmvko2bnq84:pb8075f9c1c1b371ed245c236e06597056e0c0f54350d926674e178b5cc11c10f@cah8ha8ra8h8i7.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d3qgn51e1i6j03"
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///mygymbro.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
