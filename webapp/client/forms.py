from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Optional


class CompteEpargneCreationForm(FlaskForm):
    titulaire_id = IntegerField('titulaire', validators=[DataRequired()])
    taux_remuneration = StringField('Taux Rémuneration', default=0.02)
    submit = SubmitField("Creation")


class VirementForm(FlaskForm):
    compte_src = IntegerField('compte source' , validators=[DataRequired()])
    compte_dest = IntegerField('compte destinataire', validators=[DataRequired()])
    valeur = FloatField('Somme', validators=[DataRequired()])
    submit = SubmitField("Effectuer")