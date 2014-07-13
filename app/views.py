from flask import render_template, flash, redirect
from app import app
from forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "Miguel"}  # fake user
    posts = [
        # fake array of posts
        {"author": {"nickname": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"nickname": "Susan"},
            "body": "The Avengers movie was so cool!"},
        {"author":
            {"nickname": "Jack"},
            "body": "Flask isn't so bad...."}
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flashString = 'Login Requested for OpenID="'
        flashString += form.openid.data + '" remember me='
        flashString += str(form.remember_me.data)
        flash(flashString)
        return redirect("/index")

    return render_template("login.html", title="Sign In", form=form, providers=app.config['OPENID_PROVIDERS'])
