import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecretkey")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    SWAGGER = {
        'title': "MyGymBro API",
        'uiversion': 3,
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
                "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
            }
        },
        "security": [{"Bearer": []}],
    }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mygymbro.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
