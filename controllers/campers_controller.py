from models.camper import Camper, CamperType
from db.database import db


def create_camper(name:str , age:int, email:str, phone:str=None) -> Camper:
    """
    Create a new camper with the provided details.
    
    :param name: Name of the camper
    :param age: Age of the camper (must be between 8 and 18)
    :param email: Email address of the camper
    :param phone: Optional phone number of the camper
    :return: The created Camper object
    """
    new_camper = Camper(name=name, age=age, email=email, phone=phone)
    db.session.add(new_camper)
    db.session.commit()
    return new_camper


def get_camper_by_id(camper_id: int) -> CamperType | None:
    """
    Retrieve a camper by their ID.
    
    :param camper_id: ID of the camper to retrieve
    :return: Camper object if found, None otherwise
    """
    camper = Camper.query.get(camper_id)
    if camper:
        return CamperType(id=camper.id, name=camper.name, age=camper.age, email=camper.email, phone=camper.phone)
    return None

def get_all_campers() -> list[CamperType]:
    """
    Retrieve all campers.
    
    :return: List of CamperType objects representing all campers
    """
    campers = Camper.query.all() #SELECT * FROM campers
    return [CamperType(id=camper.id, name=camper.name, age=camper.age, email=camper.email, phone=camper.phone) for camper in campers]

def update_camper(camper_id: int, name: str = None, age: int = None, email: str = None, phone: str = None) -> Camper | None:
    """
    Update an existing camper's details.
    
    :param camper_id: ID of the camper to update
    :param name: New name for the camper (optional)
    :param age: New age for the camper (optional)
    :param email: New email for the camper (optional)
    :param phone: New phone number for the camper (optional)
    :return: Updated Camper object if successful, None if camper not found
    """
    camper = Camper.query.get(camper_id)
    if not camper:
        return None
    
    if name:
        camper.name = name
    if age:
        camper.age = age
    if email:
        camper.email = email
    if phone:
        camper.phone = phone
    
    db.session.commit()# UPDATE campers SET ... WHERE id = campers_id
    return camper 
def delete_camper(camper_id: int) -> bool:
    """Delete a camper by their ID.
    :param camper_id: ID of the camper to delete
    :return: True if deletion was successful, False if camper not found
    """
    camper = Camper.query.get(camper_id)
    if not camper:
        return False
    
    db.session.delete(camper) # DELETE FROM campers WHERE id = camper_id
    db.session.commit()
    return True