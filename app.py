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


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['username']
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        addUser(name, email, phone, password=None)
    return render_template('user.html', username=name, message='注册成功！'),


if __name__ == '__main__':
    app.run(debug=True)
