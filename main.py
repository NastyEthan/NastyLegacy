from flask import render_template, request # flask

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
