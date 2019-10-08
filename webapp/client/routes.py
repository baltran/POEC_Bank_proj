import time

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from webapp import db
from webapp.admin import bp
from flask_login import current_user, login_user, logout_user
from webapp.main.classes.utilisateur import Utilisateur
from webapp.admin.forms import ConseillerCreationForm
from webapp.main.requetes import inserer
from webapp.auth.email import send_password_reset_email
from webapp.main.classes.conseiller import Conseiller

@bp.route('/espaceClient', methods=['GET', 'POST'])
@bp.endpoint('espaceClient')
#@roles_required('admin')
def espaceClient():
    if current_user.is_authenticated:
        """consulter le compte"""
        render_template('client/espaceClient.html')
    else:
        redirect(url_for('auth.login'))





