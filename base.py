from peewee import Model
import qdb


class BaseModel(Model):
    class Meta:
        database = qdb.qblogdb
