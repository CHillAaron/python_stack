from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route('/')                           
def hello_world():
    return render_template('index.html' , num_rows = 4, num_column=4 , color_first='red', color_second='black') 

@app.route('/<int:x>')
def rows(x):
    return render_template("index.html", num_rows = int(x), num_column=int(x), color_first='red', color_second='black')

@app.route('/<int:x>/<int:y>')
def column(x, y):
    return render_template("index.html", num_rows = int(x), num_column = int(y), color_first='red', color_second='black')

@app.route('/<int:x>/<int:y>/<color1>')
def color1(x, y, color1):
    return render_template("index.html", num_rows = int(x), num_column = int(y), color_first = color1 ,  color_second = "black")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def color2(x, y, color1 , color2):
    return render_template("index.html", num_rows = int(x), num_column = int(y), color_first = color1, color_second = color2)

if __name__=="__main__":
    app.run(debug=True)