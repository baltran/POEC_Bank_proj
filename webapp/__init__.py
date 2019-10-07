
from flask import Flask, request, session, current_app
from flask_babel import Babel

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

#app = Flask(__name__)
#app.config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
mail = Mail()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    #bootstrap.init_app(app)
    #moment.init_app(app)
    babel.init_app(app)

    # ... no changes to blueprint registration
    from webapp.auth import bp as auth_bp
    from webapp.main import bp as main_bp
    #from webapp.api import bp as api_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    #app.register_blueprint(api_bp, url_prefix='/api')
    if not app.debug and not app.testing:
        # ... no changes to logging setup
        pass
    with app.app_context():
        pass

    return app


from webapp.main import models, filters


@babel.localeselector
def get_locale():
    if request.args.get('lang') in current_app.config['LANGUAGES']:
        session['lang'] = request.args.get('lang')
    local_language = session.get('lang', request.accept_languages.best_match(current_app.config['LANGUAGES']))
    return local_language