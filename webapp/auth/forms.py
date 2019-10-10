from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se rappeler de moi')
    submit = SubmitField('Me connecter')


class SignupForm(FlaskForm):
    prenom = StringField('Prénom', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    username = StringField('Utilisateur', validators=[DataRequired()])
    # password = PasswordField('Mot de passe', validators=[DataRequired()])
    # password_bis = PasswordField('Confirmation du mot de passe', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    adresse = StringField('Adresse', validators=[DataRequired()])
    tel = StringField('Téléphone', validators=[DataRequired()])
    revenu_mensuel = StringField('Revenu mensuel moyen', validators=[DataRequired()])
    submit = SubmitField("Demander mon compte")


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password_bis = PasswordField('Repeter votre mot de passe',
                                 validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Réinitialisez votre mot de passe')