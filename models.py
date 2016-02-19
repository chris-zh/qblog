import base
from peewee import IntegerField, CharField


class T_USER(base.BaseModel):
    __spec__ = ''
    id = IntegerField(10)
    name = CharField(128)
    email = CharField(128)
    phone = CharField(128)
    password = CharField(128)

