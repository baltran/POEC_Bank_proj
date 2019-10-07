import time

from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from webapp import db
from webapp.auth import bp
from webapp.auth.forms import LoginForm, SigninForm, ResetPasswordRequestForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user
from webapp.main.classes.utilisateur import Utilisateur
from webapp.main.requetes import inserer
from webapp.auth.email import send_password_reset_email


@bp.route('login', methods=['GET', 'POST'])
@bp.endpoint('login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Utilisateur.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login ou mot de passe invalide')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
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
        if form.password.data == form.password_bis.data:
            data = {
                form.username.name: form.username.data,
                form.password.name: generate_password_hash(form.password.data),
                form.email.name: form.email.data
            }
            u = Utilisateur(**data)
            insertion = inserer(u)
            if insertion == -1:
                flash("l'utilisateur existe déjà !")
            elif not insertion:
                flash("Erreur dans la base de donnée !")
            else:
                return redirect(url_for('main.index'))
        else:
            form.password_bis.errors.append('Mot de passe non confirmé !')
    return render_template('auth/signin.html', title='Inscription',
                           form=form)


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