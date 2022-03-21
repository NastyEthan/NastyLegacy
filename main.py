from flask import render_template, Flask # flask

app = Flask(__name__)
# Blueprints


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("nasty.html")

@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")


if __name__ == "__main__":
    app.run(debug=True)
