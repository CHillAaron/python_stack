from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  
    
@app.route('/play')
def base():
    return render_template("index.html", num_times=3, color_choice = 'blue')

@app.route('/play/<int:times>')
def box(times):
    return render_template("index.html", num_times = int(times), color_choice = 'blue')

@app.route('/play/<int:times>/<color>')
def color(times, color):
    return render_template("index.html", num_times = int(times) , color_choice = color)

    
if __name__=="__main__":
    app.run(debug=True)