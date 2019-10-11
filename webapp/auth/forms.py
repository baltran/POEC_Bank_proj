from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_babel import lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Utilisateur'), validators=[DataRequired()])
    password = PasswordField(_l('Mot de passe'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Se rappeler de moi'))
    submit = SubmitField(_l('Me connecter'))


class SignupForm(FlaskForm):
    prenom = StringField(_l('Prénom'), validators=[DataRequired()])
    nom = StringField(_l('Nom'), validators=[DataRequired()])
    username = StringField(_l('Utilisateur'), validators=[DataRequired()])
    # password = PasswordField('Mot de passe', validators=[DataRequired()])
    # password_bis = PasswordField('Confirmation du mot de passe', validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired()])
    adresse = StringField(_l('Adresse'), validators=[DataRequired()])
    tel = StringField(_l('Téléphone'), validators=[DataRequired()])
    revenu_mensuel = StringField(_l('Revenu mensuel moyen'), validators=[DataRequired()])
    submit = SubmitField(_l("Demander mon compte"))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Mot de passe'), validators=[DataRequired()])
    password_bis = PasswordField(_l('Repeter votre mot de passe'),
                                 validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Réinitialisez votre mot de passe'))