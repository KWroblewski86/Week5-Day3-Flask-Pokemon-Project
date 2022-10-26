from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


team = db.Table(
    'team',
    db.Column('team_id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('name', db.String, nullable=False)
)

pokedex = db.Table(
    'pokedex',
    db.Column('team_id', db.Integer, db.ForeignKey('team.team_id')),
    db.Column('poke_id', db.Integer, db.ForeignKey('pokemon.poke_id')),
    db.Column('win_count', db.Integer, db.ForeignKey('user.id')),
    db.Column('loss_count', db.Integer, db.ForeignKey('user.id'))
)

poke_type = db.Table(
    'poke type',
    db.Column('poke_id', db.Integer, db.ForeignKey('pokemon.poke_id')),
    db.Column('type_id', db.Integer, db.ForeignKey('type.type_id'))
)


class User(db.Model, UserMixin):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    


    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


    def saveToDB(self):
        db.session.add(self)
        db.session.commit()





class Pokemon(db.Model):
    poke_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    ability = db.Column(db.String(25))
    img_url = db.Column(db.String)
    attack = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)


    def __init__(self, poke_id, name, ability, img_url, attack, hp, defense):
        self.poke_id = poke_id
        self.name = name
        self.ability = ability
        self.img_url = img_url
        self.attack = attack
        self.hp = hp
        self.defense = defense


    def saveToDB(self):
        db.session.add(self)
        db.session.commit()





class Type(db.Model):
    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False)


    def __init__(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name


    def saveToDB(self):
        db.session.add(self)
        db.session.commit()