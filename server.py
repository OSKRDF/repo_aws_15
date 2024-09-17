

from flask import Flask, render_template

app=Flask(__name__, template_folder="template")

@app.route('/')
def home():
    return render_template("register.html")

if __name__=="__main__":
    host = "127.0.0.1"
    port="4000"
    app.run(host,port,True)

    
    
 