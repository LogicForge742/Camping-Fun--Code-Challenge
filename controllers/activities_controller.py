from models.activity import Activity, ActivityType
from db.database import db


def create_activity(name:str, difficulty:str) -> ActivityType:
    """
    Create a new activity with the provided name and difficulty.
    :param name: Name of the activity
    :param difficulty: Difficulty level of the activity
    :return: The created Activity object
    """

    new_activity =Activity(name= name , difficulty= difficulty)
    db.session.add(new_activity)
    db.session.commit()
    return new_activity

def get_activity_by_id(activity_id: int) -> ActivityType | None:
    """
    Retrieve an activity by its ID.
    :param activity_id: ID of the activity to retrieve
    :return: Activity object if found, None otherwise
    """
    activity = Activity.query.get(activity_id)
    if activity:
        return ActivityType(id=activity.id, name=activity.name, difficulty=activity.difficulty)
    return None

def get_all_activities() -> list[ActivityType]:
    """
    Retrieve all activities.
    :return: List of ActivityType objects representing all activities
    """
    activities = Activity.query.all()  # SELECT * FROM activities
    return [ActivityType(id=activity.id, name=activity.name, difficulty=activity.difficulty) for activity in activities]


def update_activity(activity_id: int, name: str = None, difficulty: str = None) -> Activity | None:
    """
    Update an existing activity's details.
    :param activity_id: ID of the activity to update
    :param name: New name for the activity 
    :param difficulty: New difficulty for the activity 
    :return: Updated Activity object if successful, None if activity not found
    """
    activity = Activity.query.get(activity_id)
    if not activity:
        return None
    
    if name:
        activity.name = name
    if difficulty:
        activity.difficulty = difficulty
    
    db.session.commit()
    return activity

def delete_activity(activity_id: int) -> bool:
    """
    Delete an activity by its ID.
    :param activity_id: ID of the activity to delete
    :return: True if deletion was successful, False if activity not found
    """
    activity = Activity.query.get(activity_id)
    if not activity:
        return False
    
    db.session.delete(activity)
    db.session.commit()
    return True

