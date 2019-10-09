import time

from flask import render_template, flash, redirect, url_for, escape
from werkzeug.security import generate_password_hash

from webapp import db
from webapp.client import bp

from flask_login import current_user, login_user, logout_user, login_required
from webapp.main.classes.compte_courant import CompteCourant
from webapp.main.classes.compte import Compte
from webapp.main.classes.utilisateur import Utilisateur
from webapp.admin.forms import ConseillerCreationForm
from webapp.main.requetes import inserer
from webapp.auth.email import send_password_reset_email
from webapp.main.classes.conseiller import Conseiller
from flask_babel import lazy_gettext as _l


@bp.route('index', methods=['GET', 'POST'])
@bp.endpoint('index')
@login_required
def index():
    if current_user.is_authenticated and current_user.discriminator == 'client':
        return render_template('client/index.html', user=current_user, title='Espace Client')
    redirect(url_for('main.index'))


@bp.route('/compteCourant', methods=['GET', 'POST'])
@bp.endpoint('/compteCourant')
def compteCourant():
    if current_user.is_authenticated and current_user.discriminator == 'client':
        compte = CompteCourant.query.filter_by(titulaire=current_user).first()
        print(compte)
        flash(compte)
        print(type(current_user.comptes))
        for compte in current_user.comptes:
            print(compte)
        print(list(current_user.comptes).__len__())
        if compte.operations is None:
            flash(_l('Aucune opération n a été effectuée sur ce compte'))
        else:
            pass




        return render_template('client/compteCourant.html', user=current_user, title='Compte Courant', comptes=list(current_user.comptes))
    redirect(url_for('main.index'))


@bp.route('/compteEpargne', methods=['GET', 'POST'])
@bp.endpoint('/compteEpargne')
def compteEpargne():
    return render_template('client/compteEpargne.html', user=current_user, title='Compte Courant')






