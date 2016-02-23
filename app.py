from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for
from flask import flash
from flask import Flask
from flask import session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import sql, Column, String, Integer

# import models
from flask_bootstrap import Bootstrap
from config import SQLALCHEMY_DATABASE_URI
from flask_login import UserMixin
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

app = Flask(__name__)
bootstrap = Bootstrap(app)
# init db
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = "super secret key"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.session_protection = 'String'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


class User(UserMixin, db.Model):
    __tablename__ = 't_user'
    id = Column(Integer(), primary_key=True)
    name = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))

    def __repr__(self):
        return u'<User, {0}, {1}, {2}, {3}>'.format(self.id, self.name, self.email, self.password)


def test():
    # user2 = User(name='user2', password='user2123', email='user2@1.com')
    # db.session.add(user2)
    # db.session.commit()
    chris = User.query.filter(User.name == 'chris.zhang', User.password == '1234').first()
    chris2 = User.query.get('1')
    print(chris2)


@app.route('/login_success')
def login_success():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        return render_template('user.html', username=user.name, message='登陆成功！')
    else:
        return render_template('user.html', message='获取Session失败！')


@app.route('/', methods=['GET', 'POST'])
def index():
    user_id = session.get('user_id')
    user = None
    print(79)
    print(user_id)
    if user_id:
        # user = User.query.filter(User.id == user_id).first()
        # flash(message='user_info: ' + str(user_id))
        return redirect(url_for('login_success'))

    return render_template('index.html', user_id=user_id, user=user)


@app.route('/register', methods=['POST'])
def register():
    name = request.form['username']
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
    return render_template('user.html', username=name, message='注册成功！'),


@app.route('/login', methods=['POST', 'GET'])
def login():
    # email = request.form['email']
    password = request.form['password']
    name = request.form['username']
    user_form = request.form.to_dict()
    name = user_form['username']
    password = user_form['password']
    remember_me = False
    try:
        remember_me = user_form['remember_me']
    except:
        remember_me = False
    print(user_form)
    # remember_me = request.form['remember_me']

    print(51)
    user = User.query.filter(User.name == name, User.password == password).first()
    print(user)
    print(109)
    print(remember_me)
    print(111)
    if user:
        login_user(user, remember=remember_me)
        response = make_response(redirect(url_for('login_success')))
        # response.set_cookie('user_id', str(user.id))
        # session['user_id'] = user.id
        # print('session: ', session)
        return response
    else:
        return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
    # test()
