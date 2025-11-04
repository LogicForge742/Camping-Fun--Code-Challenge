#  Camping Fun API

A RESTful Flask API for managing **Campers**, **Activities**, and **Signups** in a summer camp.  
This project is built with **Flask**, **SQLAlchemy**, and **PostgreSQL**, and includes full CRUD functionality.

---

## Features

-  Manage **Campers** (Create, Read, Update, Delete)
-  Manage **Activities** (Create, Read, Update, Delete)
-  Register **Signups** linking Campers to Activities
-  Database migrations using **Flask-Migrate**
-  Input validation and error handling
- Easy to extend and integrate with a frontend

---

##  Tech Stack

- **Backend Framework:** Flask
- **Database ORM:** SQLAlchemy
- **Migrations:** Flask-Migrate
- **Database:** PostgreSQL
- **Language:** Python 3.10+
- **Environment:** Virtualenv (`env/` or `venv/`)

---

##  Installation & Setup

### 1️ Clone the repository
```bash
git@github.com:LogicForge742/Camping-Fun--Code-Challenge.git

2️⃣ Create a virtual environment
python3 -m venv env
source env/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Initialize the database
flask db init
flask db migrate -m "initial models"
flask db upgrade

flask --app app run --debug
