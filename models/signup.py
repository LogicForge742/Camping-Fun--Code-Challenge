from db.database import db
from dataclasses import dataclass

@dataclass
class SignupType:
    id: int
    time: int
    camper_id: int
    activity_id: int


class Signup(db.Model):
    __tablename__ = 'signups'

    # Columns must be indented INSIDE the class
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable=False)
    camper_id = db.Column(db.Integer, db.ForeignKey('campers.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)

    # Relationships
    camper = db.relationship('Camper', back_populates='signups')
    activity = db.relationship('Activity', back_populates='signups')

    __table_args__ = (
        db.CheckConstraint('time >= 0 AND time <= 23', name='check_time_range'),
    )

    def __init__(self, time, camper_id, activity_id):
        errors = []
        if not isinstance(time, int) or not (0 <= time <= 23):
            errors.append("Time must be an integer between 0 and 23.")

        if errors:
            raise ValueError(errors)

        self.time = time
        self.camper_id = camper_id
        self.activity_id = activity_id
