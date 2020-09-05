from flask_sqlalchemy import SQLAlchemy
from secure import CONNECT_STRING

db = SQLAlchemy()

def setup_db(app, database_path=CONNECT_STRING):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    return db 