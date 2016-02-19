# encoding:utf-8
from peewee import *
from datetime import date
from tests import db_test

db = db_test.db2


class Person(db_test.BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()



class Pet(db_test.BaseModel):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()



db.connect()

db.create_table(Person, safe=True)
uncle_bob = Person(name='Fuck Shit', birthday=date(1967, 1, 28), is_relative=True)
uncle_bob.save()
