from flask import Flask, render_template, url_for, request
#from sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Creds():
    def __init__(self, fname, lname, email, passwd):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.passwd = passwd
        

@app.route("/")
def welcome_site():
    print(request)
    return render_template("main.html")

@app.route("/register")
def register():
    args = request.args
    Creds.fname = args.get("fname")
    Creds.lname = args.get("lname")
    Creds.email = args.get("email")
    Creds.passwd = args.get("passwd")

    print(request)
    return render_template("Register.html", fname=Creds.fname, lname=Creds.lname, email=Creds.email, passwd=Creds.passwd)

@app.route("/login")
def login():
    args = request.args
    Creds.email = args.get("email")
    Creds.passwd = args.get("passwd")

    print(request)
    return render_template("Login.html", email=Creds.email, passwd=Creds.passwd)

if __name__ == "__main__":
#    app.run()
    app.run(host="0.0.0.0", port="80")





