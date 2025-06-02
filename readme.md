# 🎸 BandConnect

## **BandConnect** is a full-stack capstone project that brings fans closer to their favorite music band. The platform allows users to view concert pictures, read song lyrics, check upcoming events, register for concerts, and manage their reservations — all in one seamless experience.

## 🧱 System Architecture

![System Design](system_architecture.png)

This diagram shows the interaction between the user, Django main site, Flask microservices, and the databases:

- **Django** runs on IBM Kubernetes Service and interacts with:
  - A Flask microservice on IBM Code Engine (pictures)
  - A Flask + MongoDB microservice on RedHat OpenShift (songs)
- Data is stored in **MySQL**, **MongoDB**, and **IBM Cloud Object Storage**.

---

---

## 🚀 Features

### 🧑‍🎤 Anonymous Users

- View popular song lyrics
- Browse pictures from past concerts
- See upcoming events

### 🔐 Registered Users

- Create an account and sign in
- Register for upcoming concerts
- View and manage their registrations

### ⚙️ Admin Users

- Modify concert details (e.g., update concert dates)

---

## 🛠️ Technologies Used

### 🔹 Microservices

- **Flask** for building REST APIs

  - **Get Pictures Service**
    Serves images from past concerts with full CRUD support.

    **Endpoints:**

    | Action | Method | Return Code    | Body                               | URL Endpoint    |
    | ------ | ------ | -------------- | ---------------------------------- | --------------- |
    | List   | GET    | 200 OK         | Array of picture URLs `[{...}]`    | `/picture`      |
    | Create | POST   | 201 CREATED    | A picture resource as JSON `{...}` | `/picture`      |
    | Read   | GET    | 200 OK         | A picture as JSON `{...}`          | `/picture/{id}` |
    | Update | PUT    | 200 OK         | A picture as JSON `{...}`          | `/picture/{id}` |
    | Delete | DELETE | 204 NO CONTENT | `""`                               | `/picture/{id}` |

  - **Get Songs Service**
    Serves song lyrics from a MongoDB database.

### 🔹 Database

- **MongoDB** for storing and retrieving song lyrics
- **SQLite** for managing Django application data

### 🔹 Main Application

- **Django** for core web application (MVC structure)
- **Django Templates** for rendering views
- **Django Auth** for user registration and login

### 🔹 Deployment

- **IBM Code Engine** for deploying the Pictures microservice
- **RedHat OpenShift** for deploying the Songs microservice and MongoDB
- **IBM Kubernetes Service (IKS)** for deploying the main Django application

---

## 📸 Screenshots

> Screenshots demonstrating features and architecture to be added during implementation

---

## 🧭 Project Structure

```
bandconnect/
├── pictures-service/          # Flask microservice for event images
├── songs-service/             # Flask + MongoDB microservice for song lyrics
├── main-app/                  # Django web application
└── README.md
```

---

## 🧪 Health Checks

Each microservice exposes a `/health` endpoint to monitor its status.

---

## 📦 Setup Instructions

> Setup and deployment instructions will be updated here as development progresses.

---

## 🌐 Live Demo

> [Coming Soon – to be updated after deployment]

---

## 🤝 Contributing

Contributions are welcome. Please fork the repository and open a pull request.

---

build a songs microservice in Flask.

This microservice works with MongoDB database to store lyrics of the most popular songs of the band. You will be using the PyMongo python module to interact with MongoDB programatically.

Action Method Return code Body URL Endpoint
List GET 200 OK Array of songs [{...}] GET /song
Create POST 201 CREATED A song resource as json {...} POST /song
Read GET 200 OK A song as json {...} GET /song/{id}
Update PUT 200 OK A song as json {...} PUT /song/{id}
Delete DELETE 204 NO CONTENT "" DELETE /song/{id}
Health GET 200 OK "" GET /health
Count GET 200 OK "" GET /count
