#from playhouse.pool import PooledPostgresqlExtDatabase
from peewee import PostgresqlDatabase, Model

qblogdb = PostgresqlDatabase(
    'qblogdb',  # Required by Peewee.
    user='webflask',  # Will be passed directly to psycopg2.
    password='webflask',  # Ditto.
    host='121.42.149.46',  # Ditto.

)


class BaseModel(Model):
    class Meta:
        database = qblogdb
