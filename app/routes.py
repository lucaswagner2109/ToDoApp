from flask import render_template, redirect, url_for

from app import app
from app.forms import SigninForm

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    title = "Hello, Visitor!"
    message = "This will be an innovative ToDo WebApp using Python Flask!"
    return render_template("index.html", title = title, message = message)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    # create form
    form = SigninForm()
    title = "Sign In"
    # validate input
    if form.validate_on_submit():
        return redirect("/index")
    return render_template("signin.html", title = title, form=form)
