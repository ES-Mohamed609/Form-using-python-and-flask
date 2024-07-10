from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField,DateField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp





class InfoForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    information = TextAreaField('Information', validators=[Length(max=200)])
    excel_file = FileField('Upload Excel File', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired(),Length(min=11, max=11), Regexp(r'^01[0-2]\d{8}$', message="Invalid phone number")])
    submit = SubmitField("Submit")


