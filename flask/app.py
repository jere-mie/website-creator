from flask import Flask
from flask import render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from makeSite import makeSite

class WebForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=0, max=100)])    
    img = StringField('Link to Picture', validators=[DataRequired(), Length(min=0, max=300)])    
    desc = StringField('Short Personal Description (1 sentence)', validators=[DataRequired(), Length(min=0, max=100)])    
    school = StringField('School', validators=[DataRequired(), Length(min=0, max=90)])    
    year = StringField('Graduation Year', validators=[DataRequired(), Length(min=0, max=20)])    
    github = StringField('GitHub Link', validators=[DataRequired(), Length(min=0, max=90)])    
    linkedin = StringField('Linkedin Link', validators=[DataRequired(), Length(min=0, max=90)])    
    resume = StringField('Link to Resume', validators=[DataRequired(), Length(min=0, max=90)])    
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = '79efe2f763efd0ez71a69bc58jjj2p50'


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = WebForm()
    if form.validate_on_submit():
        info = {
            "name":form.name.data,
            "img":form.img.data,
            "desc":form.desc.data,
            "school":form.school.data,
            "year":form.year.data,
            "github":form.github.data,
            "resume":form.resume.data,
            "linkedin":form.linkedin.data
        }
        makeSite(info)
        return render_template('index.html', websiteMade=True)
    return render_template('index.html', form=form)



if __name__=='__main__':
    app.run(debug=True)