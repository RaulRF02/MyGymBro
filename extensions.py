from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
def get_scoped_session():
    return scoped_session(sessionmaker(bind=db.engine))
jwt = JWTManager()
