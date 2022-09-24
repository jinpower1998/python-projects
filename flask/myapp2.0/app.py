from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


#create flask-app
app = Flask(__name__)

# create  db-extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"
# initialize the app with the extension
db.init_app(app)

#class for storing creds in db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()

#class for Credentials
class Creds():
    def __init__(self, fname, lname, email, passwd):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.passwd = passwd
        
# create user in db
def create_db_user_data(firstname, lastname, email, password):
    user = User(
            __fname__ = firstname,
            __lname__ = lastname,
            __email__ = email,
            __passwd__ = password
        )   
                    
    db.session.add(user)
    db.session.commit()        
    return user

#main site
@app.route("/")
def welcome_site():
    print(request)
    return render_template("main.html")

#registration site
@app.route("/register", methods=['GET', 'POST'])
def register():

    args = request.args
    Creds.fname = args.get("fname")
    Creds.lname = args.get("lname")
    Creds.email = args.get("email")
    Creds.passwd = args.get("passwd")
        
    print(request)

    if request.method=="GET":
        if "Submit" in request.form:
            print("REQUEST SUBMITTED !")
    
    return render_template("Register.html", fname=Creds.fname, lname=Creds.lname, email=Creds.email, passwd=Creds.passwd)

# @app.route("/users")
# def user_list():
#     users = db.session.execute(db.select(User).order_by(User.email)).all()
#     return render_template("user/list.html", users=users)

#login site
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


app.run(debug=True)


