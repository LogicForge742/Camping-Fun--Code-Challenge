from db.database import db
from dataclasses import dataclass

#Dataclass for easy serialization of the Activity objects
@dataclass
class ActivityType:
    id:int
    name:str
    difficulty:str

#sqlalchemy for the activities table
class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(100), nullable=False)

    # Relationships
    signups = db.relationship('Signup', back_populates='activity')
    campers = db.relationship('Camper', secondary='signups', back_populates='activities')


def __init__(self,name,difficulty):
    errors = []
    #app level validation for the name
    if not name:
       errors.append('name is required')
    #app level validation for difficulty
    if not difficulty:
       errors.append("Activity difficulty required")
    #if validation errors are found  raise an exception
    if errors:
      raise ValueError(errors)
    # if no validation errors assign the values to instances
    self.name = name
    self.difficulty= difficulty

    
    


