# Aid4All
AI-powered platform for real-time, equitable disaster resource management.

Our team aimed to address the inefficiencies and inequities in disaster relief efforts. Many affected communities struggle with delayed or unequal access to essential resources like food, shelter, and medical aid. Aid4All seeks to provide a fair, real-time solution by optimizing resource distribution, improving coordination, and ensuring that help reaches those who need it most.

- [Project summary](#project-summary)
- [Technology implementation](#technology-implementation)
- [Solution architecture](#solution-architecture)
- [Project development roadmap](#project-development-roadmap)
- [Steps to setup the project](#steps-to-setup)



## Project Summary

### Aid4All - An AI-Powered Disaster Relief Platform

Disaster relief is often hampered by delays, unequal distribution of resources, and a lack of real-time information. Communities affected by natural calamities, such as floods, earthquakes, or hurricanes, frequently experience challenges in accessing critical aid like food, shelter, medical supplies, and financial assistance. Aid organizations struggle with coordinating efforts, managing volunteers, and efficiently allocating resources to the most affected areas.

**Aid4All** is our solution to these challenges, leveraging AI to ensure equitable, real-time access to disaster relief resources. Built using a combination of HTML, CSS, and Bootstrap for the frontend, Python Flask for the backend, and Watsonx AI for predictive capabilities, Aid4All is a comprehensive platform designed to streamline relief operations and ensure that no community is left behind during a disaster.

#### Key Features:

1. **Crisis Dashboard with AI Predictions**
   Aid4All features a dynamic crisis dashboard that enables users to select ongoing or upcoming natural calamities, such as floods or wildfires, and view real-time data. Watsonx AI powers predictive models that analyze weather patterns, historical data, and current conditions to forecast the severity and potential impact of disasters on specific locations. This feature helps both users and administrators anticipate and prepare for crises in advance.

2. **Resource Request System**
   During a disaster, affected individuals can use Aid4All to submit resource requests for food, shelter, medical supplies, or financial aid through a simple form. These requests are captured in the system and displayed in a table for administrators to process and prioritize based on the most urgent needs. Users can track the status of their requests to ensure transparency and accountability.

3. **Donation and Support**
   Aid4All allows users to donate funds to support relief efforts. Donors can view a list of available donation campaigns and contribute directly through the platform. The funds are then allocated to specific resource requests, ensuring that donations are used effectively to support communities in need. The platform also provides transparency by showing how donations are used.

4. **Volunteer Signup and Task Assignment**
   Volunteers play a crucial role in disaster relief, and Aid4All makes it easy for them to sign up and offer their assistance. Volunteers can register via the platform, and their information is stored in the database. The system matches volunteers with specific tasks based on their location, availability, and skill set. This ensures that volunteer efforts are efficiently coordinated and that the right people are deployed to the right areas.

5. **Supply Management and Tracking**
   Aid4All provides an integrated supply management system that consolidates data from resource requests and volunteer assignments. This feature allows administrators to track which volunteers are distributing aid and monitor the progress of resource deliveries. The system helps prevent bottlenecks and ensures that relief reaches affected areas in a timely manner.

6. **Real-Time Updates and External Data Integration**
   Aid4All integrates with external APIs, such as news APIs and government data sources, to provide real-time updates on disaster conditions. Users can stay informed about the latest developments and receive alerts about any changes in their area. This real-time data helps improve decision-making and ensures that relief efforts are aligned with current needs.

#### Impact:
With Aid4All, disaster relief efforts become more organized, transparent, and equitable. The platform ensures that resources reach the most vulnerable communities quickly and efficiently while providing real-time information and predictive insights. Aid4All empowers individuals, organizations, and volunteers to collaborate in a more effective way, ultimately saving lives and accelerating recovery efforts.

## Technology Implementation
Aid4All uses a robust tech stack to power its platform:
- **Frontend**: HTML, CSS, and Bootstrap for a responsive, user-friendly interface.
- **Backend**: Python Flask for handling user interactions, data processing, and resource management.
- **AI**: Watsonx AI for predictive analytics, generating disaster forecasts, and optimizing resource distribution.
- **Database**: SQLite to store user data, requests, donations, and volunteer information.
- **Cloud**: IBM Cloud for hosting and scalability.

## Solution Architecture

![Architecture](https://raw.githubusercontent.com/Sadhvi-Nayak/Aid4All/main/images/architectureDiagram.png)

## Project development roadmap

![Architecture](https://raw.githubusercontent.com/Sadhvi-Nayak/Aid4All/main/images/roadmap.png)

## Steps to setup
- Install python on your machine: sudo yum install python3.9
- Run python3.9 -m venv aid4all
- source aid4all/bin/activate
- Verify python version inside venv by running python --version. It should be 3.9.19
- Run pip install -r requirements.txt
- Run python app.py
- Click on the link http://127.0.0.1:5000
