import time

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from webapp import db
from webapp.auth import bp
from webapp.auth.forms import LoginForm, SigninForm, ResetPasswordRequestForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user
from webapp.main.classes.utilisateur import Utilisateur
from webapp.main.classes.demande import Demande
from webapp.main.requetes import inserer
from webapp.auth.email import send_password_reset_email


def redirect_by_role(user):
    if user.discriminator == "client":
        return redirect(url_for('client.index'))
    elif user.discriminator == "conseiller":
        return redirect(url_for('conseiller.index'))
    else:
        return redirect(url_for('admin.index'))


@bp.route('login', methods=['GET', 'POST'])
@bp.endpoint('login')
def login():
    if current_user.is_authenticated:
        return redirect_by_role(current_user)
    form = LoginForm()
    if form.validate_on_submit():
        user = Utilisateur.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login ou mot de passe invalide')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect_by_role(user)
        #return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Authentification',
                           form=form)


@bp.route('/logout')
@bp.endpoint('logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/signin', methods=['GET', 'POST'])
@bp.endpoint('signin')
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        data = {
            form.prenom.name: form.prenom.data,
            form.nom.name: form.nom.data,
            form.username.name: form.username.data,
            # form.password.name: generate_password_hash(form.password.data),
            form.email.name: form.email.data,
            form.adresse.name: form.adresse.data,
            form.tel.name: form.telephone.data,
            form.revenu_mensuel.name: form.revenu_mensuel.data
        }
        demande = Demande(**data)
        insertion = inserer(demande)
        if insertion == -1:
            flash("Demande déjà effectuée.")
        elif not insertion:
            flash("Erreur dans la base de données.")
        else:
            return redirect(url_for('auth.signin_confirmation'))
    return render_template('auth/signin.html', title='Inscription',
                           form=form)


@bp.route('/signin_confirmation', methods=['GET', 'POST'])
@bp.endpoint('signin_confirmation')
def signin_confirmation():
    return render_template('auth/signin_confirmation.html', title='Confirmation de demande')


@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = Utilisateur.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Consultez votre email pour et suivez les instructions')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = Utilisateur.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Votre mot de passe a été réinitialisé.')
        return redirect(url_for('auth.login'))
    exp = int(Utilisateur.get_exp_token(token) - time.time())
    return render_template('auth/reset_password.html', form=form, exp=exp)