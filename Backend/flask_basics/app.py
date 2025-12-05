'''Flask is a lightweight web framework for Python that lets you build web applications quickly.
Every Flask app starts with Flask(__name__) and @app.route to define routes.'''
'''To Run , install -> pip install Flask ,,,, In terminal run -> python app.py'''
# ----- 01-flask-basics -----
from flask import Flask , request , jsonify , redirect , url_for
# Create Flask application instance
app = Flask(__name__)
# # Define a route for the homepage
# @app.route('/')
# def home():
#     return '<h1>Welcome to Flask Basics!</h1>'

# # add new route /welcome/<name> 
# @app.route('/welcome/<name>')
# def welcome(name):
#     return f'<h1>Welcome, {name}!</h1>'

# ----- 02-request-response -----
@app.route('/hello')
def hello():
    # Getting query parameters (e.g., /hello?name=John)
    name = request.args.get('name','Guest')
    return f'<h1>Hello, {name}!</h1>'
@app.route('/user/<username>')
def show_user(username):
    # Getting URL path parameters
    return f'<h1>User: {username}</h1>'
@app.route('/redirect')
def redirect_demo():
    # Redirecting to another route
    return redirect(url_for("hello"))
@app.route('/json-demo')
def json_demo():
    # Return JSON response
    data = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)

# Task: Create a route /calculate that takes two query parameters a and b and returns their sum as a JSON response.
@app.route('/calculate')
def calculate():
    a = request.args.get('a', type=int, default=0)
    b = request.args.get('b', type=int, default=0)
    result = a+b
    return jsonify({'result':result,'operation':'sum'})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
# To run the app, use the command: python app.py