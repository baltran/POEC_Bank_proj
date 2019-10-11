import time

from flask import render_template, flash, redirect, url_for, escape, request
from werkzeug.security import generate_password_hash

from webapp import db
from webapp.client import bp

from flask_login import current_user, login_user, logout_user, login_required
from webapp.main.classes.compte_courant import CompteCourant
from webapp.main.classes.compte_epargne import CompteEpargne
from webapp.main.classes.operation import Operation
from webapp.client.forms import CompteEpargneCreationForm
from webapp.admin.forms import ConseillerCreationForm
from webapp.main.requetes import inserer
from webapp.auth.email import send_password_reset_email
from webapp.main.classes.conseiller import Conseiller
from flask_babel import lazy_gettext as _l


@bp.route('index', methods=['GET', 'POST'])
@bp.endpoint('index')
@login_required
def index():
    print(len(current_user.comptes.all()))
    print(current_user.comptes.all())
    if current_user.is_authenticated and current_user.discriminator == 'client':
        return render_template('client/index.html', user=current_user, title='Espace Client', nb_comptes=len(current_user.comptes.all()))
    redirect(url_for('main.index'))


@bp.route('/compteCourant', methods=['GET', 'POST'])
@bp.endpoint('/compteCourant')
def compteCourant():
    if current_user.is_authenticated and current_user.discriminator == 'client':
        compte = CompteCourant.query.filter_by(titulaire=current_user).first()
        #flash(compte)
        #print(type(current_user.comptes))
        #for compte in current_user.comptes:
            #print(compte.operations)
        #print(list(current_user.comptes).__len__())
        operations= compte.operations.union_all(compte.virements).all()
        #Operation.query.filter_by(compte_id=compte.id).all()


        print('++++++++++', operations[0])
        if compte.operations is None:
            flash(_l('Aucune opération n\' a été effectuée sur ce compte'))
        else:
            pass

        #if (compte.solde > 0 or  compte.autorisation_decouvert) and ():






        return render_template('client/compteCourant.html', user=current_user, compte =compte, title='Compte Courant', operations=operations)
    redirect(url_for('main.index'))


@bp.route('/compteEpargne', methods=['GET', 'POST'])
@bp.endpoint('/compteEpargne')
def compteEpargne():
    return render_template('client/compteEpargne.html', user=current_user, title='Compte Courant')



@bp.route('/CreerCompteEpargne', methods=['GET', 'POST'])
@bp.route('/CreerCompteEpargne')
def CreerCompteEpargne():
    if current_user.is_authenticated and current_user.discriminator == 'client':
        #return redirect(url_for('main.index'))
        form = CompteEpargneCreationForm()
        if form.validate_on_submit():
            data ={form.titulaire_id.name: form.titulaire_id.data,
                form.taux_remuneration.name: form.taux_remuneration.data,
                   }
            compte_e = CompteEpargne(**data)
            insertion = inserer(compte_e)
            if insertion:
                return redirect(url_for('client.compteEpargne'))
            #afficher le solde du compte epargne
            #rémuneration d'un compte et verser la rémunération dans

        return render_template('client/creerCompteEpargne.html', user=current_user, compte=compte, title='Création COmpte Epargne', operations=operations,
                               form=form)

    redirect(url_for('main.index'))


@bp.route('/Virement', methods=['GET', 'POST'])
@bp.route('/Virement')
def Virement(somme):
    compte = CompteCourant()
