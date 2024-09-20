

from flask import Flask, render_template, request
from database.db import *

app=Flask(__name__, template_folder="template")

#@app.route('/')
@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    id, name, lastname, birthday = data["id"], data["name"], data["lastname"], data["birthday"]
    #print(id, name, lastname, birthday)
    insert(id, name, lastname, birthday)
    return "User added"


if __name__=="__main__":
    host = "127.0.0.1"
    port="4000"
    app.run(host,port,True)

    
    
 