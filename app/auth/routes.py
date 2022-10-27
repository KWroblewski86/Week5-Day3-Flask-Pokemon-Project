from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

import app
from .forms import LoginForm, UserCreationForm
from app.models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/', methods=["GET", "POST"])
def signMeUP():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data

            print(first_name, last_name, username, email, password)

            user = User(first_name, last_name, username, email, password)

            user.saveToDB()
            
            return redirect(url_for('auth.logMeIn'))
    return render_template('signup.html', form=form)


@auth.route('/login', methods=["GET", "POST"])
def logMeIn():
    form = LoginForm()
    if request.method == "POST":
        print('post method made')
        if form.validate():
            username = form.username.data
            password = form.password.data
            print(username, password)

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    print('successfully logged in')
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    print('incorrect password')

            else:
                print('user does not exist')
    
    
    
    return render_template('login.html', x=form)



@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))

