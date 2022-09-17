from flask import Flask, render_template, url_for 
#from sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def welcome_site():
    return render_template("main.html")

@app.route("/register")
def register():
    return render_template("Register.html")

@app.route("/login")
def login():
    return render_template("Login.html")

if __name__ == "__main__":
    app.run()
#    app.run(host="0.0.0.0", port="443")





