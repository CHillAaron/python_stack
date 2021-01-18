from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #espn.com/ or amazon.com/ or facebook.com/ localhost:5000/
def homePage():
    return render_template("index.html")


@app.route('/nba') #localhost:5000/nba
def showNbaPage():
    return "Placeholder for the nba page"

@app.route("/wnba")
def showWnba():
    return "WNBA page here"

@app.route("/teams/<int:teamId>")
def showTeam(teamId):
    print("*******")
    print(teamId)
    print("*******")

    return f"Placeholder for an html page to show Info about team # {teamId}"

@app.route("/saysomething/<word>/<int:num>")
def saysomething(word,num):
    return word * num











if __name__ =='__main__':
    app.run(debug = True)