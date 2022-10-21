from flask import Blueprint, render_template, request

from app.auth.forms import UserCreationForm
from app.models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=["GET", "POST"])
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
            


        
    return render_template('signup.html', form = form)


@auth.route('/login')
def loginMeIn():
    return render_template('login.html')