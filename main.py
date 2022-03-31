from flask import render_template, Flask # flask
import requests

from users.crudu_app import app_crudu
from users.userapi import api_bp
from __init__ import app


app.register_blueprint(app_crudu)
app.register_blueprint(api_bp)



# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("nasty.html")


@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")



@app.route('/userapi/', methods=['GET', 'POST'])
def userapi():
    url = "http://127.0.0.1:5000/usercrud/questions/"
    response = requests.request("GET", url)
    questions = response.json()
    questionList = []
    for question in questions:
        questionList.append(question)
    return render_template("userapi.html", questions=questions, questionList=questionList)


if __name__ == "__main__":
    app.run(debug=True)
