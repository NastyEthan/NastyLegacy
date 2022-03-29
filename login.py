@app.route('/login/')
def home():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    return render_template('index.html')

def login():
  usr = input("Enter a login: ")
  pwd = input("Enter a password: ")

  if usr is in users AND pwd is in passwords: ## this stuff actually works
    account = True
  else:
    alert("Invalid Password or Username")
  return home() 

  if account:
    session['logged_in'] = True
  else:
    flash('wrong password!')
  return home()

@app.route('logout')
def logout():
  session['logged_in'] = False
  return home()