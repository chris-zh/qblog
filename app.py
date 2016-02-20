from flask import Flask, render_template, request
import models
import qdb
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
# init db
db = qdb.qblogdb


def addUser(name, email, phone, password):
    user = models.T_USER(name=name, email=email, phone=phone, password=password)
    user.save()


def queryUser(name, email, phone, password):
    user = models.T_USER.get(email=email, password=password)
    print(user)


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


@app.route('/helloworld', methods=['POST', 'GET'])
def signin():
    email = request.form['email']
    password = request.form['password']



def post(request):
    if request.method == 'POST':
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True)
