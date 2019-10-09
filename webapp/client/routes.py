import time

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from webapp import db
from webapp.client import bp

from flask_login import current_user, login_user, logout_user
from webapp.main.classes.compte_courant import CompteCourant
from webapp.admin.forms import ConseillerCreationForm
from webapp.main.requetes import inserer
from webapp.auth.email import send_password_reset_email
from webapp.main.classes.conseiller import Conseiller

@bp.route('/compteCourant', methods=['GET', 'POST'])
@bp.endpoint('compteCourant')
#@roles_required('client')
def compteCourant():
    if current_user.is_authenticated:
        print(current_user)
        render_template('client/compteCourant.html')

@bp.route('compteEpargne', methods=['GET', 'POST'])
@bp.endpoint('compteEpargne')
def compteEpargne():

    render_template('client/compteEpargne')





