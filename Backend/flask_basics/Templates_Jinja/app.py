# Jinja2 is A templating engine that lets you create HTML pages with dynamic content.
from flask import Flask , render_template 
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    return render_template('home.html', title='Home Page', message='Welcome to Flask!' , now=now)
@app.route('/about')
def about():
    # Passing data to templates
    team = [
        {'name':'Alice','role':'Developer'},
        {'name':'Bob','role':'Designer'},
        {'name':'Charlie','role':'Manager'}
    ]
    return render_template('about.html',title='About Us',team=team)

if __name__ == '__main__':
    app.run(debug=True)