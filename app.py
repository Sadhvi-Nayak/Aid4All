from flask import Flask,redirect,render_template,url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os, csv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aid4all.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

news_api_key = os.getenv('NEWS_API_KEY')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crisisDashboard")
def crisisDashboard():
    return render_template("crisisDashboard.html",news_api_key=news_api_key)

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

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/add_crisis_data", methods=['POST'])
def add_crisis_data():
	if request.method == "POST":
		latitude = request.form["latitude"]
		longitude = request.form["longitude"]
		title = request.form["title"]
		description = request.form["description"]
		intensity = request.form["intensity"]
		csv_file = "static/crisis_user_data.csv"
		with open(csv_file, mode="a", newline="") as file:
			writer = csv.writer(file)
			writer.writerow([latitude, longitude, title, description, intensity])
		flash("Data added successfully!", "success")
		return redirect("/admin")

if __name__ == '__main__':
    app.run(debug=True)