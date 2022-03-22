from sqlalchemy.exc import IntegrityError
from main import db

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of myDB.db


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL

class Users(db.Model):
    # define the Users schema

    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    grade = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    period = db.Column(db.String(255), unique=True, nullable=False)
    group = db.Column(db.String(255), unique=True, nullable=False)
    ghName = db.Column(db.String(255), unique=True, nullable=False)
    slName = db.Column(db.String(255), unique=True, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, grade, email, period, group, ghName, slName):
        self.name = name
        self.grade = grade
        self.email = email
        self.period = period
        self.group = group
        self.ghName = ghName
        self.slName = slName

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
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
            "grade": self.grade,
            "email": self.email,
            "period": self.period,
            "group": self.group,
            "ghName": self.ghName,
            "slName": self.slName,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name="", grade="", email="", period="", group="", ghName="", slName=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(grade) > 0:
            self.grade = grade
        if len(email) > 0:
            self.email = email
        if len(period) > 0:
            self.period = period
        if len(group) > 0:
            self.group = group
        if len(ghName) > 0:
            self.ghName = ghName
        if len(slName) > 0:
            self.slName = slName
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


# class Users(db.Model):
#     # define the Users schema
#     studentID = db.Column(db.Integer, primary_key=True)
#     studentName = db.Column(db.String(255), unique=False, nullable=False)
#     phoneNumber = db.Column(db.String(255), unique=True, nullable=False)
#     email = db.Column(db.String(255), unique=False, nullable=False)
#
#     # constructor of a User object, initializes of instance variables within object
#     def __init__(self, studentName, phoneNumber, email):
#         self.studentName = studentName
#         self.phoneNumber = phoneNumber
#         self.email = email
#
#     # CRUD create/add a new record to the table
#     # returns self or None on error
#     def create(self):
#         try:
#             # creates a person object from Users(db.Model) class, passes initializers
#             db.session.add(self)  # add prepares to persist person object to Users table
#             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None
#
#     # CRUD read converts self to dictionary
#     # returns dictionary
#     def read(self):
#         return {
#             "userID": self.userID,
#             "name": self.name,
#             "email": self.email,
#             "password": self.password,
#             "phone": self.phone
#         }
#
#     # CRUD update: updates users name, password, phone
#     # returns self
#     def update(self, name, password="", phone=""):
#         """only updates values with length"""
#         if len(name) > 0:
#             self.name = name
#         if len(password) > 0:
#             self.password = password
#         if len(phone) > 0:
#             self.phone = phone
#         db.session.commit()
#         return self
#
#     # CRUD delete: remove self
#     # None
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#         return None


"""Database Creation and Testing section"""


def users_model_tester():
    print("--------------------------")
    print("Seed Data for Table: Users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    s1 = Users(userID='1', name='Sahil', grade='11', email='sahillamarjacksonjr205@gmail.com', period='4', group='NastyLegacy', ghName='AD1616', slName='Sahil Samar')
    # s2 = Users(sid='2', studentName='CS', phoneNumber='g', email='qtr')
    # s3 = Users(sid='3', studentName='Bio', phoneNumber='h', email='zcv')
    table = [s1]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate name, or error: {row.name}")


def users_model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)



def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    users_model_tester()  # builds model of Users
    users_model_printer()
    # model_tester()  # builds model of Users
    model_printer()