#coding: utf-8
__author__ = 'chris.zhang'
from flask import Flask, request, make_response, redirect, abort, render_template
from flask import url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap



app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    print(url_for('index', _external=True))
    return render_template('index.html')

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