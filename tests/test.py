__author__ = 'chris.zhang'
from jsonschema import validate
schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
 }

# validate({"name":"hahah","price":21}, schema)
from peewee import *


db = PostgresqlDatabase(
    'qblogdb',  # Required by Peewee.
    user='webflask',  # Will be passed directly to psycopg2.
    password='webflask',  # Ditto.
    host='121.42.149.46',  # Ditto.
)

class BaseModel(Model):
    class Meta:
        database = db

class User2(BaseModel):
    username = TextField()

db.connect()
db.create_table([User2])
