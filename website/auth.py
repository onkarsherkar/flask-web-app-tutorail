from flask import Blueprint, render_template, request, flash

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

    flag = True
    if len(email) < 3:
      flag = False
      flash('Email minimum have 4 letter', category='error')
    if len(firstName) < 3:
      flag = False
      flash('First name minimum have 4 letter', category='error')
    if len(password1) < 3:
      flag = False
      flash('Password minimum have 4 letter', category='error')
    if password1 != password2:
      flag = False
      flash('Password is not matching', category='error')
    if flag:
      flash('Account is created!', category='success')

  return render_template("sign_up.html")
