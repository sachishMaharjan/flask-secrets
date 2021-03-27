from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "MYSECRETKEY"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=('GET', 'POST'))
def get_login():
    form = MyForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        if user_email == "admin@email.com" and user_password == "12345678":
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)