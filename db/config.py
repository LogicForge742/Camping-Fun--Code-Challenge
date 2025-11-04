import os

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://campadmin:YeshuaHamashiah!@localhost:5432/CampFun')