
from connect_database  import *
from flask import Flask, render_template, request


#create flask-app
app = Flask(__name__)

global db_email 
global db_password

#main site
@app.route("/", methods=['GET','POST'])
def __welcome_site__():
    print(request)
    return render_template("main.html")

#registration site
@app.route("/register", methods=['GET','POST'])
def __register__():

    firstname = request.form.get("fname")
    lastname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("passwd")

    print(request)

#post data to external database and redirect
    if request.method=="POST":
        if request.form.get("submit_button") == "Submit":

            response = connect_database.get_data(email)
            for i in response:
                db_email = i["Email"]
           
            try: db_email
            except NameError: db_email = None
           
            if db_email == email:
                return  f"<h1> user with email address '{ email }' already exits, please use another one !</h1>"
            elif db_email != email:
                connect_database.post_data(email, firstname, lastname, password)
            else:
                pass
            

            return render_template("enter.html", fname=firstname, lname=lastname)
        else:
            print("REQUEST SUBMITTED !")
  
    
    return render_template("Register.html",  fname=firstname, lname=lastname, email=email, passwd=password)


#enter site

@app.route("/enter", methods=['GET','POST'])
def __complete_registration__():
        return render_template("enter.html")

#login site
@app.route("/login",methods=['GET','POST'])
def __login__():
   
    email = request.form.get("email")
    password = request.form.get("passwd")


    if request.method == "POST":
        if request.form.get("login_button") == "login":
            response  = connect_database.get_data(email)
            for i in response:
                db_email = i["Email"]
                db_password= i["Password"]

            try: db_email
            except NameError: db_email = None   
            if db_email is None:
                return f"<h1> user with email address '{ email }' does not exist !</h1>"


            if email == db_email and password == db_password:
                return "<h1> login successful !</h1>"
            elif email != db_email or password != db_password:
                return "<h1> login failed ! </h1>"
            else:
                pass
      

    print(request)
    return render_template("Login.html", email=email, passwd=password)



if __name__ == "__main__":

    app.run(host="0.0.0.0", port="80")



