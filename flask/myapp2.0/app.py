
import requests, urllib, json
from connect_database import *
from flask import Flask, render_template, url_for, request



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
        "Email" : email,
        "Firstname" : firstname,
        "Lastname" : lastname,
        "Password" : password
     }
    print(request)

#post data to external database aan redirect
    if request.method=="POST":
        if request.form.get("submit_button") == "Submit":
            user_data_json = json.dumps(user_data, indent=4)
            print(user_data_json)
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
   
    email = request.form.get("email")
    password = request.form.get("passwd")

    login_creds = {

        "Email" : email,
        "Password": password
    }

    

    if request.method == "POST":
        if request.form.get("login_button") == "login":
            connect_database.get_data()
            print(json.dumps(login_creds, indent=4))
            if email == "A" and password == "B":
                return "<h1> login successful !</h1>"
            else:
                return "<h1> login failed ! </h1>"
            
        else:
                pass


    print(request)
    return render_template("Login.html", email=email, passwd=password)



if __name__ == "__main__":
    app.run()
    #app.run(host="0.0.0.0", port="80")


#app.run(debug=True)


