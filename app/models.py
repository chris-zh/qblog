__author__ = 'chris.zhang'
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from peewee import *

class User(db.BaseModel):
    id = IntegerField(10)
    name = CharField(128)
    email = CharField(128)
    password = CharField(128)





