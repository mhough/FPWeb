from flask import Flask, render_template, Response, request, redirect
from flask.ext.login import (
  LoginManager,
  login_required,
  login_user,
  current_user,
  logout_user,
  )
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID

OPENID_STORE = '/tmp/oid.store'

dbapp = Flask('DB_APP')
dbapp.secret_key = "I'm a fucking secret!"
dbapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


db = SQLAlchemy(dbapp)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    name = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(12))

    def __init__(self, name, fullname, email, password):
        self.name = name
        self.fullname = fullname
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.email)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        assert self.id is not None
        return unicode(self.id)


oidapp = Flask('OID_APP')
oid = OpenID(oidapp, OPENID_STORE)


loapp = Flask('LOGIN_APP')
login_manager = LoginManager()
login_manager.setup_app(loapp)

#login_manager.login_view = "login"


@login_manager.user_loader
def load_user(uid):
  try:
    uid = int(uid)
  except ValueError:
    return None
  return User.query.filter_by(id=uid).first()


@app.route("/login", methods=["GET", "POST"])
@oid.loginhandler
def login():
  if request.method == 'GET':
    if current_user.is_anonymous():
      return render_template(
        'login.html',
        next=oid.get_next_url(),
        error=oid.fetch_error()
        )
    return redirect('/logout')

  open_id = request.form.get('openid')
  if open_id:
    return oid.try_login(open_id, ask_for=['email', 'fullname', 'nickname'])

  username = request.form['user']
  pw = request.form['pasw']
  user = User.query.filter_by(name=username, password=pw).first()

  if user:
    login_user(user)
    return redirect(oid.get_next_url() or '/')
  return redirect('/Bah')


@app.route("/logout", methods=["GET", "POST"])
def logout():
  if not current_user.is_anonymous():
    if request.method == 'GET':
      return render_template('logout.html')
    logout_user()
  return redirect('/login')


@oid.after_login
def after_login(response):
  email_address = response.email
  if not email_address:
    flash('Invalid login. Please try again.')
    return redirect('/login')

  user = User.query.filter_by(email=email_address).first()
  if not user:
      nickname = response.nickname or email_address.split('@', 1)[0]
      user = User(
        name=nickname,
        fullname=response.fullname,
        email=email_address,
        password="",
        )
      db.session.add(user)
      db.session.commit()

  login_user(user)
  return redirect(oid.get_next_url() or '/')


