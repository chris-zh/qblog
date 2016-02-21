from flask import Flask, render_template, request, make_response, redirect, url_for,flash
# import models
from models import T_USER as User
import qdb
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
# init db
db = qdb.qblogdb


def addUser(name, email, phone, password):
    user = User(name=name, email=email, phone=phone, password=password)
    user.save()


def queryUser(name, email, phone, password):
    print(18)
    user = User.get(email=email, password=password)
    print(user)
    return user


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('signin.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['username']
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        addUser(name, email, phone, password=None)
    return render_template('user.html', username=name, message='注册成功！'),


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    print('fuckyou!')
    print('hahaha')
    print(0)
    print(request)
    print(12)
    # email = request.form['email']
    print(1)
    password = request.form['password']
    print(2)
    name = request.form['username']
    print(3)
    userdata = request.form.to_dict()
    print(4)
    print(userdata)
    # print(email)
    print(password)
    print(52)
    print(name)
    user = ''
    try:
        print(51)
        user = User.get(User.name == name and User.password == password)
        # response = make_response(redirect(url_for('login_success')))
        response = make_response(render_template('user.html', username=name, message='成功！'))
        return response
    except:
        print(56)
        return render_template('user.html', username=name, message='失败！')



if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
