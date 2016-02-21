import base
from peewee import IntegerField, CharField


class T_USER(base.BaseModel):
    id = IntegerField(10)
    name = CharField(128)
    email = CharField(128)
    phone = CharField(128)
    password = CharField(128)

# elsa = T_USER.get(T_USER.name == 'elsa')
# print(elsa.password)