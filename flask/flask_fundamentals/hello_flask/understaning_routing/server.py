# Create a route that responds with "Hi" and whatever name is in the URL after /say/
# Create a route that responds with the given word repeated as many times as specified in the URL
# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer (hint: http://exploreflask.com/en/latest/views.html#url-converters)
# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."


from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello world!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<text>')
def sayHi(text):
    return f'Hi {text}'

@app.route('/many/<text>/<int:num>')
def many(text, num):
    return text * num

@app.errorhandler(404) 
def nopPage(404):
    return ('Sorry! No response. Try again.')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

