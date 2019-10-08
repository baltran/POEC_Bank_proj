from flask import url_for, request
from flask_admin import AdminIndexView
from flask_admin.contrib import sqla
from flask_admin.menu import MenuLink
from flask_login import current_user
from werkzeug.utils import redirect


class GestiBankModelView(sqla.ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.discriminator == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))


class DemandeModelView(GestiBankModelView):
    can_create = False
    can_edit = True
    form_columns = ['mon_conseiller']
    column_exclude_list = (
        'password',
    )


class ConseillerModelView(GestiBankModelView):
    column_exclude_list = (
        'discriminator',
        'token',
        'token_expiration')
    form_columns = ['username', 'password', 'nom', 'prenom', 'email', 'date_debut', 'date_fin']


class MyAdminIndexView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.discriminator == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))


class HomeMenuLink(MenuLink):

    def is_accessible(self):
        return not current_user.is_authenticated


class LogoutMenuLink(MenuLink):

    def is_accessible(self):
        return current_user.is_authenticated