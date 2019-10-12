from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_babel import lazy_gettext as _l

class CompteEpargneCreationForm(FlaskForm):
    titulaire_id = IntegerField(_l('titulaire'), validators=[DataRequired()])
    taux_remuneration = StringField(_l('Taux Rémuneration'), default=0.02)
    submit = SubmitField(_l('Creation'))


class VirementForm(FlaskForm):
    compte_src = IntegerField(_l('compte source') , validators=[DataRequired()])
    compte_dest = IntegerField(_l('compte destinataire'), validators=[DataRequired()])
    valeur = FloatField(_l('Montant du Virement'), validators=[DataRequired()])
    submit = SubmitField(_l('Effectuer'))