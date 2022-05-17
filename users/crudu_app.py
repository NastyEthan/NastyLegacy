from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_login import login_required, login_manager
from flask_restful import Api
from users.model import Users
import hashlib

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
from users.query import login #, authorize

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

def codeEncryption(code):
    classcode = hashlib.sha512(code.encode()).hexdigest()


""" app route section """
# if login url, show phones table only
@app_crudu.route('/login/', methods=["GET", "POST"])
def crud_login():
    # obtains form inputs and fulfills login requirements
    classcode = "bingbong"
    if request.form:
        if classcode == request.form.get("classcode"):
            return redirect(url_for('usercrud.crudu'))
        else:
            return redirect(url_for('usercrud.crud_login'))
        # password = request.form.get("password")
        # email = request.form.get("email")
        # if login(classcode):       # zero index [0] used as email is a tuple

    # if not logged in, show the login page
    return render_template("login.html")



# @app_crudu.route('/changepass/', methods=['GET', 'POST'])
# def crud_changepass():
#     if request.form:
#         oldcode = request.form.get("oldcode")
#         newcode = request.form.get("newcode")
#         classcode = request.form.get("classcode")
#
#
#     if request.form.get("adminpass") == "jmort123":
#             if oldcode == classcode:
#                 classcode = newcode
#
#     return render_template("changepass.html")
#

# @app_crudu.route('/authorize/', methods=["GET", "POST"])
# def crud_authorize():
#     # check form inputs and creates user
#     if request.form:
#         # validation should be in HTML
#         classcode = request.form.get("classcode")
#         adminpass = request.form.get("adminpass")           # password should be verified
#         if authorize(classcode, adminpass):    # zero index [0] used as user_name and email are type tuple
#             return redirect(url_for('crud.crud_login'))
#     # show the auth user page if the above fails for some reason
#     return render_template("authorize.html")

# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     return redirect('/adminlogin/')


# Default URL
@app_crudu.route('/')
# @login_required # login_url="/adminlogin/"
def crudu():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crudu.html", table=users_all())

@app_crudu.route('/admin')
def crudAdmin():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crudAdmin.html", table=users_all())

def find(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.filter((Users.name.ilike(term)) | (Users.email.ilike(term)))
    return [peep.read() for peep in table]

@app_crudu.route('/search', methods=['GET', 'POST'])
def search():
    """obtains all Users from table and loads Admin Form"""
    return render_template("search.html")

@app_crudu.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    return response

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
            request.form.get("saveKey"),
        )
        po.create()
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
        saveKey = request.form.get("saveKey")
        po = users_by_id(userID)
        if po is not None:
            print("among")
            if (saveKey == po.saveKey):
                print("us")
                po.update(name, grade, email, period, group, ghName, slName, saveKey)
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
