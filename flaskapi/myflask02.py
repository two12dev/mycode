#!/usr/bin/python3
from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect("/hello/user")

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
