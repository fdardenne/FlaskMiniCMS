from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import RegistrationForm, LoginForm

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route("login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    flash("Bad login", "danger")
    return render_template('auth/login.html', title="Register", form=form)
    if form.validate_on_submit():
        flash("Successfully logged in", "primary")
        return redirect(url_for("home.home"))
    return render_template("auth/login.html", title="Login", form=form)

@mod_auth.route("register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

   
    if form.validate_on_submit():
        flash("Account created", "primary")
        return redirect(url_for('home.home'))

    return render_template('auth/register.html', title="Register", form=form)
