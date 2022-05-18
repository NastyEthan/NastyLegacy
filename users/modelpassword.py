from flask import render_template, request, url_for, redirect
from sqlalchemy.exc import IntegrityError
from __init__ import db, app
from __init__ import admin, login
from flask_login import current_user, login_user, logout_user, UserMixin
from flask_admin.contrib.sqla import ModelView
from users.model import MyModelView


class Passwords(db.Model, UserMixin):
    # define the Password schema
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, password):
        self.name = name
        self.password = password

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        print("We here now")
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "name": self.name,
            "password": self.password,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name="", password=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(password) > 0:
            self.password = password
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    def get_id(self):
        return (self.ID)




"""Database Creation and Testing section"""


def passwords_model_tester():
    print("--------------------------")
    print("Seed Data for Table: Passwords")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    t1 = Passwords(name='Admin', password='jmort123')
    t2 = Passwords(name='Class', password='ramenchoppa')
    table = [t1, t2]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            print("error")
            db.session.remove()

def passwords_model_printer():
    print("------------")
    print("Table: passwords with SQL query")
    print("------------")
    result = db.session.execute('select * from passwords')
    print(result.keys())
    for row in result:
        print(row)



if __name__ == "__main__":
    passwords_model_tester()  # builds model of Passwords
    passwords_model_printer()


