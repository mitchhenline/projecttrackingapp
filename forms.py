from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('Team Name:', validators=[DataRequired(), Length(min=2, max=255)])
    submit = SubmitField('Submit:')