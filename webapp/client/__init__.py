from flask import Blueprint

bp = Blueprint("client", __name__)

from webapp.client import routes
