``` python
from flask import render_template, request,  Blueprint
from __init__ import app
import requests
import urllib.request, json

aecreatetask_bp = Blueprint('aecreatetask', __name__,
                      url_prefix='/aecreatetask',
                      template_folder='aetemplates',
                      static_folder='static', static_url_path='static/aecreatetask')

@app.route('/aecreatetask/', methods=['GET', 'POST'])
def aecreatetask_index():
    try:
        if request.form:
            a = request.form.get("f") #user input
            print("The number is " + a)
            x = 0
            y = 1
            z = 0
            b = int(a)
            fs = [1,]
            if b == 1:
                z = 1
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", z=z)
            else:
                for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", fs=fs)
        return render_template("aecreatetaskIndex.html", a="")
    except:
        return render_template("aecreatetaskIndex.html", a="Something went wrong try again")

```
