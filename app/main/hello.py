#coding: utf-8
__author__ = 'chris.zhang'
from flask import Flask, request, make_response, redirect, abort, render_template
from flask import url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os




basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary = True)
    name = db.Column(db.String(64), unique = True)


@app.route('/')
def index():
    print(url_for('index', _external=True))
    return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/fuck/shit/bitch/<name>')
def get_user(name):
    print(url_for('get_user',name=name, _external=True))
    fuckDict = {'name':name,'password':'fuckyou!'}
    return render_template('user.html', name = name, shit = 'test', dic = fuckDict, name_list = name_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)