__author__ = 'chris.zhang'
from jsonschema import validate
schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
 }

validate({"name":"hahah","price":21}, schema)