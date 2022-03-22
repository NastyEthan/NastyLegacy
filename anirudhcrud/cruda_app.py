from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api
from anirudhcrud.modela import People

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_cruda = Blueprint('anirudhcrud', __name__,
                     url_prefix='/cruda',
                     template_folder='templates/cruda/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_cruda)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def people_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in People.query.all()]


def people_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = People.query.filter((People.studentName.ilike(term)) | (People.phoneNumber.ilike(term)) | (People.email.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def people_by_id(sid):
    """finds User in table matching userid """
    return People.query.filter_by(studentID=sid).first()


# User extraction from SQL
def people_by_studentName(phoneNumber):
    """finds User in table matching phoneNumber """
    return People.query.filter_by(phoneNumber=phoneNumber).first()


""" app route section """


# Default URL
@app_cruda.route('/')
def cruda():
    """obtains all Users from table and loads Admin Form"""
    return render_template("cruda.html", table=people_all())


# CRUD create/add
@app_cruda.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = People(
            request.form.get("sid"),
            request.form.get("studentName"),
            request.form.get("phoneNumber"),
            request.form.get("email")
        )
        po.create()
    return redirect(url_for('anirudhcrud.cruda'))


# CRUD read
@app_cruda.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        sid = request.form.get("sid")
        po = people_by_id(sid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("cruda.html", table=table)


# CRUD update
@app_cruda.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        sid = request.form.get("sid")
        studentName = request.form.get("studentName")
        phoneNumber = request.form.get("phoneNumber")
        po = people_by_id(sid)
        if po is not None:
            po.update(studentName)
            po.update(phoneNumber)
    return redirect(url_for('anirudhcrud.cruda'))


# CRUD delete
@app_cruda.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        sid = request.form.get("sid")
        po = people_by_id(sid)
        if po is not None:
            po.delete()
    return redirect(url_for('anirudhcrud.cruda'))


# Search request and response
@app_cruda.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(people_ilike(term)), 200)
    return response





