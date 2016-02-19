from playhouse.pool import PooledPostgresqlExtDatabase
from peewee import *

db = PostgresqlDatabase(
    'qblogdb',  # Required by Peewee.
    user='webflask',  # Will be passed directly to psycopg2.
    password='webflask',  # Ditto.
    host='121.42.149.46',  # Ditto.

)

db2 = PooledPostgresqlExtDatabase(
    'qblogdb',
    max_connections=20,
    stale_timeout= 300,
    user = 'webflask',
    password='webflask',
    host='121.42.149.46',
)

class BaseModel(Model):
    class Meta:
        database = db2