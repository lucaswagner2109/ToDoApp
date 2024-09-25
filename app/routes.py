from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user

import sqlalchemy as sa

from app import app, db
from app.forms import SigninForm, SignupForm
from app.models import User

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    title = "Hello, Visitor!"
    message = "This will be an innovative ToDo WebApp using Python Flask!"
    return render_template("index.html", title = title, message = message)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    # if already signed in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # create form
    form = SigninForm()
    title = "Sign In"
    # validate input
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None:
            flash("Invalid username")
        elif not user.check_password(form.password.data):
            flash("Invalid password")
        else: # sign in
            login_user(user, remember=form.remember.data)
            return redirect(url_for("index"))
        return redirect(url_for("signin"))
    return render_template("signin.html", title=title, form=form)

@app.route("/signout")
def signout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # if already signed in redirect
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # create form
    form = SignupForm()
    title = "Sign Up"
    # validate
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('signin'))
    return render_template('signup.html', title=title, form=form)