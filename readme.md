# 🎸 BandConnect

**BandConnect** is a full-stack capstone project that brings fans closer to their favorite music band. The platform allows users to view concert pictures, read song lyrics, check upcoming events, register for concerts, and manage their reservations — all in one seamless experience.

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
  - **Get Pictures Service**: Serves images from past concerts (CRUD support)
  - **Get Songs Service**: Serves song lyrics from a MongoDB database

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
