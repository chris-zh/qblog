__author__ = 'chris.zhang'
from flask import Flask, request, make_response, redirect, abort, render_template
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def get_user(name):
    return render_template('user.html', name = name)


if __name__ == '__main__':
    app.run(debug=True)