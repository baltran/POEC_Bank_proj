from flask import Blueprint

bp = Blueprint("admins", __name__)

from webapp.admin import routes
