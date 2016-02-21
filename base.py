from peewee import Model
from peewee import IntegerField, CharField
# import qdb
from qdb import qblogdb

class BaseModel(Model):
    class Meta:
        database = qblogdb

class T_USER(BaseModel):
    id = IntegerField(10)
    name = CharField(128)
    email = CharField(128)
    phone = CharField(128)
    password = CharField(128)


elsa = T_USER(name='elsa', password='elsa123')
# elsa.save()
try:
    user = T_USER.get(T_USER.name == 'elsa')
except:
    print('不存在！')
print(user.name)
print(user.id)