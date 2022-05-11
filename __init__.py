from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_admin import Admin

app = Flask(__name__)

dbURI = 'sqlite:///model/userDatabase.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)

# admin = Admin(app, name='administrator', template_mode='bootstrap5')
# Setup LoginManager object (app)
login_manager = LoginManager()
login_manager.init_app(app)