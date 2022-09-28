
import requests, urllib, json
from flask import Flask, render_template, url_for, request
#from flask_sqlalchemy import SQLAlchemy


#create flask-app
app = Flask(__name__)

# post request
rq = requests.post
    
#     return user

#main site
@app.route("/", methods=['GET','POST'])
def welcome_site():
    print(request)
    return render_template("main.html")

#registration site
@app.route("/register", methods=['GET','POST'])
def register():

    
    firstname = request.form.get("fname")
    lastname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("passwd")

    user_data = {
        "Firstname" : firstname,
        "Lastname" : lastname,
        "Email" : email,
        "Password" : password
     }
    print(request)

#post data to external database aan redirect
    if request.method=="POST":
        if request.form.get("submit_button") == "Submit":
            print(json.dumps(user_data, indent=4))
            return render_template("enter.html", fname=firstname, lname=lastname)
        else:
            print("REQUEST SUBMITTED !")
    else:
        pass
         
    
    return render_template("Register.html",  fname=firstname, lname=lastname, email=email, passwd=password)


#enter site

@app.route("/enter", methods=['GET','POST'])
def complete_registration():
        return render_template("enter.html")

#login site
@app.route("/login",methods=['GET','POST'])
def login():
    args = request.args
    email = args.get("email")
    passwordwd = args.get("passwd")

    print(request)
    return render_template("Login.html", email=email, passwd=passwordwd)



if __name__ == "__main__":
#    app.run()
    app.run(host="0.0.0.0", port="80")


#app.run(debug=True)


