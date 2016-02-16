__author__ = 'chris.zhang'
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors





