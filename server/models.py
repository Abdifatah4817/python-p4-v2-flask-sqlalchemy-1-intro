from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# metadata object (optional, can be used for naming conventions)
metadata = MetaData()

# create the SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define the Pet model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
