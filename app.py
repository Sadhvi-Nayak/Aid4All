from flask import Flask,redirect,render_template,url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os, csv, smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aid4all.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

news_api_key = os.getenv('NEWS_API_KEY')
app.config["EMAIL"] = os.getenv("EMAIL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

def send_mail(recipient, subject, body):
	FROM = app.config["EMAIL"]
	TO = recipient if isinstance(recipient, list) else [recipient]
	SUBJECT = subject
	TEXT = body + "\n\nThanks & Regards,\nTeam Aid4All"
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (
        FROM,
        ", ".join(TO),
        SUBJECT,
        TEXT,
    )
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(app.config["EMAIL"], app.config["SECRET_KEY"])
		server.sendmail(FROM, TO, message)
		server.close()
	except:
		flash("Check your internet connection", "error")
		return redirect(url_for("home"))

class Volunteers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.String(250))
    def __repr__(self):
        return "<Volunteer %r>" % self.email

class ResourceRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    resource_type = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    urgency = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return "<ResourceRequest %r>" % self.email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crisisDashboard")
def crisisDashboard():
    return render_template("crisisDashboard.html",news_api_key=news_api_key)

@app.route("/requestResources")
def requestResources():
	resourcesRequests = ResourceRequests.query.all()
	return render_template("requestResources.html",resourcesRequests=resourcesRequests)

@app.route("/donateSupport")
def donateSupport():
    return render_template("donateSupport.html")

@app.route("/volunteerSignup")
def volunteerSignup():
	volunteers = Volunteers.query.all()
	return render_template("volunteerSignup.html",volunteers=volunteers)
	
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

@app.route("/volunteer_signup", methods=['POST'])
def volunteer_signup():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		location = request.form['location']
		role = request.form['role']
		availability = request.form['availability']
		comments = request.form['comments']
		email_check = Volunteers.query.filter_by(email=email).first()
		if not email_check:
			phone_check = Volunteers.query.filter_by(phone=phone).first()
			if not phone_check:
				volunteer = Volunteers(
                    name=name,
                    email=email,
                    phone=phone,
					location=location,
					role=role,
					availability=availability,
					comments=comments
                )
				db.session.add(volunteer)
				db.session.commit()
				send_mail(
                    email,
                    "Volunteer Signup Successfull for Aid4All",
                    "Hi "
                    + str(name)
                    + ",\nThank you for registering with Aid4All! We are excited to have you on board and appreciate your commitment to making a difference."
					+ "\nPlease keep an eye out for a WhatsApp message from 91234567890, where you will receive further updates and important information about your involvement."
                )
				flash("Signup successfully", "success")
				return redirect(url_for("volunteerSignup"))
			else:
				flash("Phone Number already in use", "error")
				return redirect(url_for("volunteerSignup"))
		else:
			flash("Email ID already in use", "error")
			return redirect(url_for("volunteerSignup"))

@app.route("/request_resources", methods=['POST'])
def request_resources():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		resource_type = request.form.getlist('resource_type')
		location = request.form['location']
		urgency = request.form['urgency']
		description = request.form['description']
        
		email_check = ResourceRequests.query.filter_by(email=email).first()
		if not email_check:
			phone_check = ResourceRequests.query.filter_by(phone=phone).first()
			if not phone_check:
				resource_request = ResourceRequests(
					name=name,
					email=email,
					phone=phone,
					resource_type=', '.join(resource_type),
					location=location,
					urgency=urgency,
					description=description
				)
				db.session.add(resource_request)
				db.session.commit()
				send_mail(
					email,
					"Resource Request Submitted Successfully",
					"Hi "
					+ str(name)
					+ ",\nThank you for your resource request to Aid4All! Our team will review your request and get back to you shortly."
					+ "\nPlease keep an eye on your email for updates."
				)
				flash("Resource request submitted successfully", "success")
				return redirect(url_for("requestResources"))
			else:
				flash("Phone Number already in use", "error")
				return redirect(url_for("requestResources"))
		else:
			flash("Email ID already in use", "error")
			return redirect(url_for("requestResources"))

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True)