from  flask import Flask
from db.database import db
from flask_migrate import Migrate
from db.config import DATABASE_URL

#an instance of Flask application
app = Flask(__name__)
#configuration for the database

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL


#enabling track modifications
db.init_app(app)

#enabling migration
migrate = Migrate(app, db)

#register the models
from models.camper import Camper
from models.activity import Activity
from models.signup import Signup

#register the controllers
from controllers.activities_controller import create_activity, get_activity_by_id, get_all_activities, update_activity, delete_activity
from controllers.campers_controller import create_camper, get_camper_by_id, get_all_campers, update_camper, delete_camper

# setup routes
@app.route('/')
def index():
    return "Welcome to the Camping Fun API!"

@app.route('/activities', methods=['POST'])
def add_activity():
    # Logic to create an activity
    return create_activity(name="Hiking", difficulty="Medium")

@app.route('/activities/<int:activity_id>', methods=['GET'])
def fetch_activity(activity_id):
    # Logic to get an activity by ID
    return get_activity_by_id(activity_id)


@app.route('/activities', methods=['GET'])
def fetch_all_activities():
    activities = get_all_activities()
    return {'activities': [activity.__dict__ for activity in activities]}


@app.route('/activities/<int:activity_id>', methods=['PUT'])
def modify_activity(activity_id):
    # Logic to update an activity
    return update_activity(activity_id, name="Updated Hiking", difficulty="Hard")


@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def remove_activity(activity_id):
    # Logic to delete an activity
    return delete_activity(activity_id)


#camper routes
@app.route('/campers', methods=['POST'])
def add_camper():
    # Logic to create a camper
    return create_camper(name="Milton ngeno", age=12, email="miltonngeno@gmail.com", phone="0706055215")

@app.route('/campers/<int:camper_id>', methods=['GET'])
def fetch_camper(camper_id):
    # Logic to get a camper by ID
    return get_camper_by_id(camper_id)

@app.route('/campers', methods=['GET'])
def fetch_all_campers():
    campers = get_all_campers()
    print(campers)
    return {'campers': [camper.__dict__ for camper in campers]}

@app.route('/campers/<int:camper_id>', methods=['PUT'])
def modify_camper(camper_id):
    # Logic to update a camper
    return update_camper(camper_id, name="Updated Milton", age=13, email="qwecha@gmail.com")


@app.route('/campers/<int:camper_id>', methods=['DELETE'])
def remove_camper(camper_id):
    # Logic to delete a camper
    return delete_camper(camper_id)
# Run the Flask application
if __name__ == '__main__':
    with app.app_context():
     app.run(debug=True)  # Run the Flask application in debug mode








