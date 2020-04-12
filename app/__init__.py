from flask_sqlalchemy import SQLAlchemy
from manage import app


db = SQLAlchemy(app)
db.create_all()