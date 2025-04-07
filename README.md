# 🏛️ Law Suit Court - IPC & Case Filing Web Application

## 📘 Introduction

This project is a **web application** built to assist users in understanding **Indian Penal Code (IPC) Sections** and generating **legal case applications** in a structured format. It aims to bridge the gap between common people and the legal system by providing a platform that explains IPC sections, their descriptions, and associated punishments. The system allows users to generate a PDF document with all necessary legal and personal details to be submitted in court.

---

## 💡 Key Features

- User login and role-based access (Customer/Admin)
- Choose case type: Criminal or Civil
- View IPC Sections with descriptions and punishments
- Generate legal case applications by providing party details and case narrative
- Export final case as a structured **PDF** including all relevant legal information
- Admin-only access for modifications or updates
- Case tracking and status updates for users

---

## 🌐 Scope

This web application provides a practical solution to the drawbacks of traditional legal documentation. It helps **common citizens** avoid repeated visits to advocates for understanding IPC and preparing case files.

The system:
- Automates application generation using user-inputted data and IPC section mappings
- Reduces time, effort, and cost for both advocates and complainants
- Can be used in real-world legal workflows with minimal customization
- Makes legal knowledge accessible and transparent

---

## ⚙️ Technology Stack

- **Frontend**: HTML/CSS, JavaScript
- **Backend**: Flask (Python), Django (optional for future expansion)
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **PDF Generation**: ReportLab
- **Image Handling**: Pillow (PIL)
- **Additional Libraries**: Caption_Creator

---

## 🛠️ Setup Instructions

### 🔹 Prerequisites
- Python 3.x
- MySQL Server

### 🔹 Install Required Packages

Use the `requirements.txt` file:

bash
pip install -r requirements.txt


### Data Base SetUP
mysql -u your_username -p < database_setup.sql

## Home Page
![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Home_Page.PNG)


## Add User
![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Add_User.PNG)


## Documentation produce
![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Dosumentation.PNG)


![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Dosumentation2.PNG)


##IPC/BNS Search
![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Find.PNG)


## Results:
![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/IPC_Result.PNG)

![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Application_Result.PNG)

![Homepage Screenshot](https://github.com/YashowardhanTripathi/Law-Document-Search-Automate/blob/main/Images/Application_Result2.PNG)



