from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class CitiesForm(FlaskForm):
    city_1 = StringField(validators=[InputRequired()])
    city_2 = StringField(validators=[InputRequired()])

