from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo


class AcceptForm(FlaskForm):
    value = IntegerField('id', validators=[DataRequired()])
    action = StringField('action', validators=[DataRequired()])


# class ClientCreationForm(FlaskForm):
#     login = StringField('login', validators=[DataRequired()])
#     password = PasswordField('Mot de passe', validators=[DataRequired()])
#     password_bis = PasswordField('Confirmation du mot de passe', validators=[DataRequired()])
#     date_debut = DateTimeField('Date_Entree', validators=[DataRequired()])
#     date_fin = DateTimeField('Date_sortie')
#     submit = SubmitField("Creation")
