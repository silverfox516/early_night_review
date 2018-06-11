from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("main.html")

@app.route('/page1')
def page1():
	return render_template("page1.html")

@app.route('/nav')
def nav():
	return render_template("nav.html")

if __name__ == "__main__":
	app.run(debug=True)
