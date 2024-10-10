from flask import Flask,redirect,render_template,url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aid4all.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crisisDashboard")
def crisisDashboard():
    return render_template("crisisDashboard.html")

@app.route("/requestResources")
def requestResources():
    return render_template("requestResources.html")

@app.route("/donateSupport")
def donateSupport():
    return render_template("donateSupport.html")

@app.route("/volunteerSignup")
def volunteerSignup():
    return render_template("volunteerSignup.html")
	
@app.route("/supplyManagement")
def supplyManagement():
    return render_template("supplyManagement.html")

if __name__ == '__main__':
    app.run(debug=True)