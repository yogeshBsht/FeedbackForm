from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, length
# from flask_babel import _, lazy_gettext as _l
from app.models import Feedback


class FeedbackForm(FlaskForm):
    username = StringField(("Username"),validators=[DataRequired()])
    email = StringField(("e-mail id"),validators=[DataRequired(), Email()])
    rating = RadioField(("Rating:"), choices=[*range(1,11)])
    # feedback = StringField(("Your feedback here"), validators=[DataRequired()])
    feedback = TextAreaField(("Your feedback here"), validators=[DataRequired(), length(max=200)])
    # fdbck_time = db.Column(db.DateTime, default=datetime.utcnow)
    # username = StringField(_l('Username'), validators=[DataRequired()])
    # password = PasswordField(_l('Password'), validators=[DataRequired()])
    # remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(('Submit'))