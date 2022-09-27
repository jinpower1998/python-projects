import email
from time import sleep
import requests, urllib
from flask import Flask, render_template, url_for, request
#from flask_sqlalchemy import SQLAlchemy


#create flask-app
app = Flask(__name__)

# post request
rq = requests.post


#class for Credentials
class Creds():
    def __init__(self, fname, lname, email, passwd):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.passwd = passwd
        
      
#     return user

#main site
@app.route("/", methods=['GET','POST'])
def welcome_site():
    print(request)
    return render_template("main.html")

#registration site
@app.route("/register", methods=['GET','POST'])
def register():

    args = request.args
    Creds.fname = args.get("fname")
    Creds.lname = args.get("lname")
    Creds.email = args.get("email")
    Creds.passwd = args.get("passwd")

    user_data = {
        "Firstname" : Creds.fname,
        "Lastname" : Creds.lname,
        "Email" : Creds.email,
        "Password" : Creds.passwd
    }

    print(request)

#post data to external database
    if request.method=="POST":
        if request.form.get("submit_button") == "Submit":
            print(user_data)
        else:
            print("REQUEST SUBMITTED !")
            pass
    
    return render_template("Register.html",  fname=Creds.fname, lname=Creds.lname, email=Creds.email, passwd=Creds.passwd)


#enter site
@app.route("/enter", methods=['GET','POST'])
def complete_registration():
    return render_template("enter.html")

#login site
@app.route("/login",methods=['GET','POST'])
def login():
    args = request.args
    Creds.email = args.get("email")
    Creds.passwd = args.get("passwd")

    print(request)
    return render_template("Login.html", email=Creds.email, passwd=Creds.passwd)




if __name__ == "__main__":
#    app.run()
    app.run(host="0.0.0.0", port="80")


#app.run(debug=True)


