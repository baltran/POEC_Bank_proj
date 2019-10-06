from webapp import create_app, db, cli, mail
from webapp.main.classes.utilisateur import Utilisateur
from flask_mail import Message

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': Utilisateur, 'Message': Message, 'mail': mail}

