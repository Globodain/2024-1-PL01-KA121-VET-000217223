
from flask_wtf import FlaskForm # type: ignore
from flask_babel import lazy_gettext as _l # type: ignore
from wtforms import TextAreaField, SubmitField # type: ignore
from wtforms.validators import DataRequired, Length # type: ignore

class MessageForm(FlaskForm):
    message = TextAreaField(
        _l('Message'),
        validators=[DataRequired(), Length(min=1, max=140)]
    )
    submit = SubmitField(_l('Submit'))

