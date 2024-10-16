from flask import Flask,redirect,render_template,url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os, csv, smtplib
import re
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aid4all.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

news_api_key = os.getenv('NEWS_API_KEY')
EMAIL = os.getenv("EMAIL")
SECRET_KEY = os.getenv("SECRET_KEY")
API_TOKEN = os.getenv('WATSONX_ACCESS_TOKEN')
WATSONX_API_URL = os.getenv('WATSONX_API_URL')

def send_mail(recipient, subject, body):
	FROM = EMAIL
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
		server.login(EMAIL, SECRET_KEY)
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

class Donations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    donation_amount = db.Column(db.String(20), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "<Donation %r>" % self.email

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
	donations = Donations.query.all()
	return render_template("donateSupport.html",donations=donations)

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

@app.route("/submit_donation", methods=['POST'])
def submit_donation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        donation_amount = request.form['amount']
        payment_method = request.form['payment_method']

        email_check = Donations.query.filter_by(email=email).first()
        if not email_check:
            phone_check = Donations.query.filter_by(phone=phone).first()
            if not phone_check:
                donation = Donations(
                    name=name,
                    email=email,
                    phone=phone,
                    donation_amount=donation_amount,
                    payment_method=payment_method,
                )
                db.session.add(donation)
                db.session.commit()
                send_mail(
                    email,
                    "Donation Confirmation",
                    "Hi "
                    + str(name)
                    + ",\nThank you for your generous donation to Aid4All! Your contribution will make a significant impact."
                    + "\nPlease keep an eye on your email for updates on how your donation is being used."
                )
                flash("Donation successful", "success")
                return redirect(url_for("donateSupport"))
            else:
                flash("Phone Number already in use", "error")
                return redirect(url_for("donateSupport"))
        else:
            flash("Email ID already in use", "error")
            return redirect(url_for("donateSupport"))


@app.route('/disaster-info', methods=['POST'])
def get_disaster_info():
	input_data = request.json

	# Check if required fields are present
	if 'disaster_type' not in input_data or 'location' not in input_data:
		return jsonify({'error': 'Please provide both disaster_type and location.'}), 400

	# Construct the request body for WatsonX
	body = {
		"input": f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. \nYour answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don'\''t know the answer to a question, please don'\''t share false information.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nI need a list of coordinates showing disaster-prone areas for {input_data['disaster_type']} in {input_data['location']}. The list should be sorted based on the intensity of damage to property and life, from high to low. Please provide the coordinates in a format suitable for displaying on a map(latitude and longitude). The intensity levels should reflect historical data, risk factors, and impact on both property and life in the region. The output should always have the following format :\n\nArea name\n\nLatitude:\n\nLongitude:\n\n(These should be as accurate as possible (E.g. - 9.9391°N, 76.5214°E , etc)\n\nIntensity of risk: (Very high, High, Moderate, Low)\n\nReason: Brief reason for the risk level, considering local topography, population density, infrastructure vulnerability and historical occurences (1 linne decription).\n\nThe above details should be added one after the other following the same formate without any other headers.Ensure that the data is relevent, detailed, and accurate for mapping purposes.<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
		"parameters": {
			"decoding_method": "greedy",
			"max_new_tokens": 200,
			"repetition_penalty": 1
		},
		"model_id": "meta-llama/llama-3-405b-instruct",
		"project_id": "16f49676-9e61-4d0e-857f-c264130446ab",
		"moderations": {
			"hap": {
				"input": {
					"enabled": True,
					"threshold": 0.5,
					"mask": {
						"remove_entity_value": True
					}
				},
				"output": {
					"enabled": True,
					"threshold": 0.5,
					"mask": {
						"remove_entity_value": True
					}
				}
			}
		}
	}

	# Set the headers for the API request
	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": f"Bearer {API_TOKEN}"
	}

	# Make the POST request to WatsonX API
	response = requests.post(WATSONX_API_URL, headers=headers, json=body)

	# Check for errors in the response
	if response.status_code != 200:
		return jsonify({'error': response.json()}), response.status_code

	results = response.json().get("results", [])

	# Log the results for debugging
	print("Results from API:", results)

	# Ensure there are results to process
	if not results:
		return jsonify({'error': 'No results generated from the API.'}), 500

	# Extract the generated text
	generated_text = results[0].get("generated_text", "")
    
	# Use regex to extract latitude, longitude, risk factors, titles, and descriptions
	regions = re.findall(r'\*\*(.*?)\*\*', generated_text)
	latitudes = re.findall(r'(?:.*?Latitude:\s*([0-9\.]+)°[NS])', generated_text)
	longitudes = re.findall(r'(?:.\s*Longitude:\s*([0-9\.]+)°[EW])', generated_text)
	intensities = re.findall(r'(?:.*?Intensity of risk:\s*(.*))', generated_text)
	reasons = re.findall(r'(?:.*?Reason:\s*(.+?)(?:\n|$))?', generated_text)
	descriptions = [item for item in reasons if item != '']

	min_length = min(len(regions),len(latitudes),len(longitudes), len(intensities), len(descriptions))    
	regions = regions[:min_length]
	latitudes = latitudes[:min_length]
	longitudes = longitudes[:min_length]
	intensities = intensities[:min_length]
	descriptions = descriptions[:min_length]

	if not regions or not latitudes or not longitudes:
		flash("Something went wrong, Please try again!", "danger")
		return redirect("/admin")

	csv_file_path = 'static/crisis_user_data_v2.csv'    
	with open(csv_file_path, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Region','Latitude','Longitude','Intensity','Description'])
		for i in range(len(regions)):
			writer.writerow([regions[i], latitudes[i], longitudes[i], intensities[i], descriptions[i]])    
	flash("Data added successfully!", "success")
	return redirect("/admin")

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True)