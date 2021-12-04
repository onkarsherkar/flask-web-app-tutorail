from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from website import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 3:
      flash('Email minimum have 4 letter', category='error')
    elif len(firstName) < 3:
      flash('First name minimum have 4 letter', category='error')
    elif len(password1) < 3:
      flash('Password minimum have 4 letter', category='error')
    elif password1 != password2:
      flash('Password is not matching', category='error')
    else:
      new_user = User(email=email, password=generate_password_hash(password1, method='sha256'), first_name=firstName)
      db.session.add(new_user)
      db.session.commit()
      flash('Account is created!', category='success')
      return redirect(url_for('views.home'))

  return render_template("sign_up.html")
