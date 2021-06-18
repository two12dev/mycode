from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home_page():
    return render_template("/home.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=2224)
