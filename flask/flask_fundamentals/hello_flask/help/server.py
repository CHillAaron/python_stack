from flask import Flask, render_template
app = Flask(__name__)

#REQUESTS ARE MADE VIA THE BROWSER
# WHEN A REQUEST GETS MADE, THE NEXT STEP IS TO FIND THE ROUTE THAT MATCHES THE REQUEST
# in a for in loop, whatever you put after 'for' represents 
@app.route('/') #espn.com/ or amazon.com/ or facebook.com/ localhost:5000/
def homePage():
    myName = "Rob"
    
    bootlegDatabasePretend = [
        "Lasagna",
        "Pbj",
        'Spaghetti'

    ]
    ramenCount = 0
    for food in bootlegDatabasePretend:
        if food == "Ramen":
            ramenCount += 1

    print("***********")
    print(ramenCount)
    print("***********")



    return render_template("index.html", x = myName,  meals = bootlegDatabasePretend, r  = ramenCount)


@app.route('/circles/<int:num>')
def showCircles(num):

    return render_template('circles.html', num = num)