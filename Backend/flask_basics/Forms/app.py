# install --> pip install Flask Flask-WTF 
# Flask-WTF is an extension that integrates WTForms with Flask, making it easier to create and handle web forms.
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Required for CSRF protection

# Define a form class
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=50)
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=500)
    ])
    submit = SubmitField('Send Message')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    # Validate form submission
    if form.validate_on_submit():
        # Process form data
        name = form.name.data
        email = form.email.data
        message = form.message.data
        
        # Here you would typically save this data or send an email
        print(f"Received message from {name} ({email}): {message}")
        
        # Flash a message to the user
        flash('Your message has been sent successfully!', 'success')
        
        # Redirect to success page
        return redirect(url_for('success'))
    
    # If GET request or form not valid, render the form
    return render_template('contact.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)