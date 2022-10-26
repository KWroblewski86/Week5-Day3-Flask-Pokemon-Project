from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class getPokemonForm(FlaskForm):
    poke_name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField()