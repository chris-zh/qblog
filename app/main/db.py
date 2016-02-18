__author__ = 'chris.zhang'
from peewee import *
from playhouse.pool import PooledPostgresqlExtDatabase


db = PostgresqlDatabase(
    'qblogdb',  # Required by Peewee.
    user='webflask',  # Will be passed directly to psycopg2.
    password='webflask',  # Ditto.
    host='121.42.149.46',  # Ditto.
)


conn = db.connect()
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField()

class Cities(BaseModel):
    name = CharField()
    location = CharField()

cities = Cities(name='Beijing')
print(cities.name)


