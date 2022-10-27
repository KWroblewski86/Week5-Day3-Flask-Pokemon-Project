import requests
from app import app
from flask import render_template, request
from app.main.forms import getPokemonForm
from app.models import Pokemon, User, pokedex



@app.route('/home')
def homePage():
    characters = ['Pikachu', 'Bulbasaur', 'Charmander', 'Charizard', 'Kadabra', 'Spearow', 'Pidgeot', 'or so many others!!']
    
    
    
    return render_template('index.html', characters=characters)


@app.route('/pokemon', methods=["GET", "POST"])
def characterPage():

    form = getPokemonForm()
    if request.method=="POST":
        
        if form.validate():
            
            poke_name = form.pokemon.data
            # submit = form.submit.data
            
            poke = Pokemon.query.filter_by(name=poke_name).first()

            if poke:
                return render_template('pokemon.html', form=form, poke=poke)


            url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
            response = requests.get(url)
            if response.ok:
                data = response.json()
                characterPage = {}
                characterPage[poke_name.title()] = {
                    'sprite': data['sprites']['other']['official-artwork']['front_default'],
                    'base_exp': data['base_experience'],
                    'ability': data['abilities'][0]['ability']['name'],
                    'base_hp': data['stats'][0]['base_stat'],
                    'base_att': data['stats'][1]['base_stat'],
                    'base_def': data['stats'][2]['base_stat']
                }
                img_url = characterPage[poke_name.title()]['sprite']
                base_exp = characterPage[poke_name.title()]['base_exp']
                ability = characterPage[poke_name.title()]['ability']
                base_hp = characterPage[poke_name.title()]['base_hp']
                base_att = characterPage[poke_name.title()]['base_att']
                base_def = characterPage[poke_name.title()]['base_def']

            poke = Pokemon(poke_name, ability, img_url, base_att, base_hp, base_def, base_exp)
            print(poke)
            poke.saveToDB()

            return render_template('pokemon.html', form=form, poke=poke)
            
            # print(poke_name, submit)
            # user = User(poke_name, submit)
            # user.saveToDB()

    return render_template('pokemon.html', form=form)




@app.route('/battle')
def battlePage():
    users = User.query.all()
    
    
    
    return render_template('battle.html', users=users)



@app.route('/attack/<int:user_id>')
def attackUser(user_id):
    p = pokedex()
    p.save()
    

    return




# Link pokemon to user
# Click catch button
# Pass pokemon name from front end to back end
# Use name to query database to initialize 
# Does current user already have pokemon
    # if pokemon is in user.pokemon(does user already have it)
# Check amount of pokemon current user has
    # if user.pokemon.count() < 5:
        #catch



