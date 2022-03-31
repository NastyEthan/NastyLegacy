from flask import render_template, request, session, Flask  # flask
from __init__ import app


@app.route('/login/', methods=['POST'])
# def do_admin_login():
#   login = request.form
#   userName = login['username']
#   password = login['password']
#
#   if account:
#     session['logged_in'] = True
#   else:
#     # flash('wrong password!')
#     return home()

def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('nasty.html')


def login():
    # usr = input("Enter a login: ")
    # pwd = input("Enter a password: ")
    classcode = input("Enter classcode: ")

    # if usr is in users AND pwd is in passwords: ## checking if user and pwd fits
    if classcode == "nighthawkcodingsociety":
        print("Correct code")
        account = True
    else:
        # alert("Invalid Password or Username")
        return home()

    if account:
        session['logged_in'] = True
        print("test")
    else:
        # flash('wrong password!')
        return home()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


def loginTester():
    try:
        login()
    except:
        print("Something went wrong")
loginTester()

if __name__ == "__main__":
    app.run(debug=False)
