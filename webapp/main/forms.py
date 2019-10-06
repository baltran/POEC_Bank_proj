from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.widgets import TextArea


class CommentForm(FlaskForm):
    body = StringField(u'Text', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Poster")



