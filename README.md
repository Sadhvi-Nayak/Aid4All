# Aid4All
AI-powered platform for real-time, equitable disaster resource management.  
<div align="center">
    <img src="https://github.com/user-attachments/assets/a7e86aaa-d9bc-44d7-af84-1fc591a8e495" alt="pic (1)" width="400" />
</div>
<br/>
Our team aimed to address the inefficiencies and inequities in disaster relief efforts. Many affected communities struggle with delayed or unequal access to essential resources like food, shelter, and medical aid. Aid4All seeks to provide a fair, real-time solution by optimizing resource distribution, improving coordination, and ensuring that help reaches those who need it most.  
<br/><br/>

- [Aid4All](#aid4all)
  - [Project Summary](#project-summary)
    - [Aid4All - An AI-Powered Disaster Relief Platform](#aid4all---an-ai-powered-disaster-relief-platform)
      - [Key Features:](#key-features)
      - [Impact:](#impact)
  - [Technology Implementation](#technology-implementation)
  - [Solution Architecture](#solution-architecture)
  - [Project development roadmap](#project-development-roadmap)
  - [Presentation Materials](#presentation-materials)
  - [Steps to setup](#steps-to-setup)
  - [Mail Auth](#mail-auth)
  - [Watsonx Auth](#watsonx-auth)
  - [Actions that can be performed](#actions-that-can-be-performed)
    - [Crisis Dashboard](#crisis-dashboard)
    - [Admin Page](#admin-page)
    - [Resource Request Page](#resource-request-page)
    - [Volunteer Signup Page](#volunteer-signup-page)
    - [Supply Management](#supply-management)
  - [Snapshots](#snapshots)
    - [Home Page](#home-page)
    - [Crisis Dashboard](#crisis-dashboard-1)
    - [Admin Page](#admin-page-1)
    - [Resources Request Page](#resources-request-page)
    - [Donate \& Support](#donate--support)
    - [Volunteer Signup](#volunteer-signup)
    - [Supply Management](#supply-management-1)


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

## Presentation Materials
Video Demo: [Youtube Link](https://youtu.be/wUh0pe-F6PM)  
PPT Presentation: [View here](https://www.canva.com/design/DAGTwuye_ik/j8FunoU9KavVcGzz1w3uLA/view?utm_content=DAGTwuye_ik&utm_campaign=designshare&utm_medium=link&utm_source=editor)  

## Steps to setup
- Install python on your linux machine using the command 'sudo yum install python3.9'
- Clone this repo into your local machine and open it using VS code or any other editor of your choice.
- Open the terminal and create a virtual environment using the command 'python3.9 -m venv aid4all'
- Activate the virtual env created using the command 'source aid4all/bin/activate'
- Verify python version inside venv by running python --version. It should be 3.9.19
- Once activated, install all the packages using the command 'pip install -r requirements.txt'.
- Once all packages are installed create a .env file and add the following:
```
NEWS_API_KEY="" (Get the API Key from https://newsapi.org/docs/endpoints/sources)
EMAIL="" (Email ID from which you want to send the mails)
SECRET_KEY="" (Steps to get this is mentioned below)
WATSONX_ACCESS_TOKEN=""
WATSONX_API_URL=""
```
- Now you are ready to run the application. Type 'py app.py' in the terminal and hit enter.
- A link like http://127.0.0.1:5000/ will pop up in the terminal. Press Ctrl and click on the link to open it in the browser to see the landing page of the application.

## Mail Auth
To set up the app password for the Gmail ID you will be used for sending emails:
1. Enable 2-factor authentication on your mail ID.
2. Go to this website https://myaccount.google.com/apppasswords
3. Enter the app name you wish and a app password will be created. You have to use this as the secret key and paste it in the .env file.
4. Yea! You are all set to send alerts using the mailing services.

## Watsonx Auth
To Configure the watsonx prompt lab and authenticate.
1. Create the project in the watsonx dataplatform(https://dataplatform.cloud.ibm.com/wx/prompts)
2. Create the API key in same the project created.
3. Generate the token using this API key, use the following command.  
``curl -X POST "https://iam.cloud.ibm.com/identity/token" --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' --data-urlencode 'grant_type=urn:ibm:params:oauth:grant-type:apikey' --data-urlencode 'apikey=<API_KEY>``
4. Add this api token in the `.env` file.
5. In app.py update the `project_id` in the request body.
 
## Actions that can be performed
### Crisis Dashboard
 - Users can input disaster type and location to receive AI-based predictions on severity.
 - Displays real-time data on disasters using Watsonx predictions.
 - Interactive map displaying disaster-prone areas with markers indicating intensity (low, medium, high) reported by the users.
 - View current news headlines fetched from a new API.

### Admin Page
 - Form to add the crisis data reported by the users.
 - Interactive map to view the added data.

### Resource Request Page
 - Affected individuals can submit requests for food, shelter, medical supplies, etc.
 - Admins can view and prioritize resource requests.
 - Available Resources, Emergency contacts and FAQs can be viewed.

### Volunteer Signup Page
 - Volunteers can sign up using a simple form.
 - Volunteers are displayed in a table view, showing their details.

### Supply Management
 - Displays a table showing resources distributed by volunteers, tracking who delivered what to which location.
 - Features three cards highlighting the top volunteer performers for recognition.
 - Provides a creative display of available stock of resources for quick insights.

## Snapshots
### Home Page
![image](https://github.com/user-attachments/assets/33f4b119-81e6-4433-98cb-d01b6618a539)
![image](https://github.com/user-attachments/assets/a541aca7-1f34-474d-981c-c6e4fab7ea56)
![image](https://github.com/user-attachments/assets/176dabb7-2f64-44fc-97e5-f033a992a607)

### Crisis Dashboard
![image](https://github.com/user-attachments/assets/80c43fe1-4f00-4075-a618-12917ec52e0b)
![image](https://github.com/user-attachments/assets/1e8b70c3-d29a-4998-8a64-364f1e37a1db)
![image](https://github.com/user-attachments/assets/49372102-d73b-4130-a85c-cf8b579f69f4)

### Admin Page
![image](https://github.com/user-attachments/assets/b74718b2-6520-4649-b00b-ab88f4cd8b4f)
![image](https://github.com/user-attachments/assets/11bbbaa8-a21d-412f-93e7-68a67b4f5ff4)

### Resources Request Page
![image](https://github.com/user-attachments/assets/49281572-e2c3-4a32-8a5d-02b2e9712a01)
![image](https://github.com/user-attachments/assets/7db6b90b-9a07-480d-aa9f-a337c2640ca3)
![image](https://github.com/user-attachments/assets/596f453f-0aab-4d4e-9d62-48ebc4e0106e)

### Donate & Support
![image](https://github.com/user-attachments/assets/b7659574-4138-44ee-85a6-76f1c203dd4b)
![image](https://github.com/user-attachments/assets/e9100526-d565-4f64-9987-1cde21c60505)
![image](https://github.com/user-attachments/assets/1cc32202-cdad-4fbc-be14-eb0e9c66db85)

### Volunteer Signup
![image](https://github.com/user-attachments/assets/4f1a6f6d-e465-42ad-ac50-6e3d3b30134b)
![image](https://github.com/user-attachments/assets/5448be4a-3763-4fe9-a282-ca72a12bbbbb)
![image](https://github.com/user-attachments/assets/e1ac56fa-0d65-4aa8-a25d-15863bcfa5a1)

### Supply Management
![image](https://github.com/user-attachments/assets/731f6f79-54cb-44e4-a6e3-751d31c6c6be)



