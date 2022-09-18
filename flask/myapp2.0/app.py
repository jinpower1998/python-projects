from flask import Flask, render_template, url_for, request
#from sqlalchemy import SQLAlchemy

app = Flask(__name__)



@app.route("/")
def welcome_site():
    print(request)
    return render_template("main.html")

@app.route("/register")
def register():
    args = request.args
    fname = args.get("fname")
    lname = args.get("lname")
    email = args.get("email")
    passwd = args.get("passwd")

    print(request)
    return render_template("Register.html", fname=fname, lname=lname, email=email, passwd=passwd)

@app.route("/login")
def login():
    args = request.args
    email = args.get("email")
    passwd = args.get("passwd")

    print(request)
    return render_template("Login.html", email=email, passwd=passwd)

if __name__ == "__main__":
    app.run()
#    app.run(host="0.0.0.0", port="443")





