from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField, DateField, TextAreaField, FieldList, FormField, HiddenField, validators
from wtforms.validators import DataRequired, InputRequired, NumberRange, Email, Length, Optional
from wtforms.fields.html5 import EmailField, IntegerField
from bson.objectid import ObjectId

class CreateProfile(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    origin = StringField('Origin', validators=[InputRequired()])
    email = EmailField('E-mail', validators=[InputRequired()])      
    trails_completed = IntegerField('Trails Completed')
    profile_pic = HiddenField("Profile Picture")
    submit = SubmitField('Submit')

class SightingsForm(FlaskForm):
    tag = StringField('e.g. Birds', validators=[Optional()])
    class Meta:
        csrf = False

class CommentsForm(FlaskForm):
    profile = SelectField('Profile', validators=[InputRequired()], coerce=ObjectId)
    body = TextAreaField('Comments', validators=[InputRequired()])
    sightings = FieldList(FormField(SightingsForm, label='e.g. Birds'), label=None, min_entries=1, max_entries=6)
    ratings = RadioField('Ratings', coerce=int, choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])      #, Unique(model= Hiker)])
    date_started = DateField('Date Started Hiking', format='%b %d, %Y')
    hours_taken = IntegerField('Hours Taken')
    minutes_taken = IntegerField('Minutes Taken')
    submit = SubmitField('Submit')