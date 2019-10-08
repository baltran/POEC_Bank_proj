from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

class ConseillerCreationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password_bis = PasswordField('Confirmation du mot de passe', validators=[DataRequired()])
    date_debut = DateField('Date Entree', format='%d-%m-%Y')
    date_fin = DateField('Date sortie', format='%d-%m-%Y', validators=[Optional()])
    submit = SubmitField("Creation")