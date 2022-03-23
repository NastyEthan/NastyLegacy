from flask import render_template, Flask # flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("nasty.html")

@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")


if __name__ == "__main__":
    app.run(debug=True)
