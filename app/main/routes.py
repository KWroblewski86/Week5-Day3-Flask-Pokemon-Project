from app import app
from flask import render_template, request
from app.main.forms import getPokemonForm
from app.models import User

@app.route('/')
def homePage():
    characters = ['Pikachu', 'Bulbasaur', 'Charmander', 'Charizard', 'Kadabra', 'Spearow', 'Pidgeot', 'or so many others!!']
    
    
    
    return render_template('index.html', characters=characters)


@app.route('/pokemon', methods = ["GET", "POST"])
def characterPage():
    
    url = 'https://pokeapi.co/'
    poke_info = {'name': "f'{url}api/v2/pokemon/{name}'",
    'hp stat': 'f"{name} has a {hp_stat} hp stat"',
    'defense stat': 'f"{name} has a {defense_stat} defense stat"',
    'attack stat': 'f"{name} has a {attack_stat} attack stat"',
    'url': 'f"Here is the link, {front_shiny}, for a {name} image"',
    'ability': 'f"{name} has the {ability} ability"'}



    form = getPokemonForm()
    if request.method == "POST":
         if form.validate():
            poke_name = form.poke_name.data
            submit = form.submit.data

            print(poke_name, submit)

            user = User(poke_name, submit)

            user.saveToDB()




    return render_template('pokemon.html', poke_info=poke_info, form=form)