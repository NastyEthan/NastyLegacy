from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api
from users.model import Users

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crudu = Blueprint('usercrud', __name__,
                     url_prefix='/usercrud',
                     template_folder='templates/pages/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crudu)


# User/Users extraction from SQL
def users_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Users.query.all()]


def users_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.filter((Users.name.ilike(term)) | (Users.grade.ilike(term)) | (Users.email.ilike(term)) | (Users.period.ilike(term)) | (Users.group.ilike(term)) | (Users.ghName.ilike(term)) | (Users.slName.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def users_by_id(userID):
    """finds User in table matching userid """
    return Users.query.filter_by(userID=userID).first()


# User extraction from SQL
def users_by_name(name):
    """finds User in table matching phoneNumber """
    return Users.query.filter_by(name=name).first()


""" app route section """


# Default URL
@app_crudu.route('/')
def crudu():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crudu.html", table=users_all())


# CRUD create/add
@app_crudu.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("name"),
            request.form.get("grade"),
            request.form.get("email"),
            request.form.get("period"),
            request.form.get("group"),
            request.form.get("ghName"),
            request.form.get("slName"),
        )
        po.create()
        print("It is working")
    return redirect(url_for('usercrud.crudu'))


# CRUD read
@app_crudu.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userID = request.form.get("userID")
        po = users_by_id(userID)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crudu.html", table=table)


# CRUD update
@app_crudu.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userID = request.form.get("userID")
        name = request.form.get("name")
        grade = request.form.get("grade")
        email = request.form.get("email")
        period = request.form.get("period")
        group = request.form.get("group")
        ghName = request.form.get("ghName")
        slName = request.form.get("slName")
        po = users_by_id(userID)
        if po is not None:
            po.update(name)
            po.update(grade)
            po.update(email)
            po.update(period)
            po.update(group)
            po.update(ghName)
            po.update(slName)
    return redirect(url_for('usercrud.crudu'))


# CRUD delete
@app_crudu.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userID = request.form.get("userID")
        po = users_by_id(userID)
        if po is not None:
            po.delete()
    return redirect(url_for('usercrud.crudu'))






