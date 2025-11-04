from db.database import db
from dataclasses import dataclass


@dataclass
class CamperType:
    id: int
    name: str
    age: int
    email: str
    phone: str = None

class Camper(db.Model):
    __tablename__ = 'campers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)

    # relationships
    signups = db.relationship('Signup', back_populates='camper', cascade='all, delete-orphan')
    activities = db.relationship('Activity', secondary='signups', back_populates='campers')

    #enforce database level validation
    __table_args__ = (
        db.CheckConstraint('age >= 8 AND age <= 18', name='age_check'),
        )               
                           

    def __init__(self, name, age, email, phone=None):
        #app validation 
        errors = []
        #app validation for the name 
        if not name:
            errors.append("Name is required")

         #app validation for the age
        if not isinstance(age,int) or not ('8 <=age =>18'):
            errors.append("age must be number between 8 and 18")


        if errors:
            raise ValueError(errors)

    

        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

