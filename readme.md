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
    This microservice allows users to view, add, update, and delete images from past concerts. It provides a RESTful API for managing concert pictures, making it easy to integrate with other applications or frontends.

    **Endpoints:**

    | Action | Method | Return Code    | Body                               | URL Endpoint    |
    | ------ | ------ | -------------- | ---------------------------------- | --------------- |
    | List   | GET    | 200 OK         | Array of picture URLs `[{...}]`    | `/picture`      |
    | Create | POST   | 201 CREATED    | A picture resource as JSON `{...}` | `/picture`      |
    | Read   | GET    | 200 OK         | A picture as JSON `{...}`          | `/picture/{id}` |
    | Update | PUT    | 200 OK         | A picture as JSON `{...}`          | `/picture/{id}` |
    | Delete | DELETE | 204 NO CONTENT | `""`                               | `/picture/{id}` |

  - **Get Songs Service**
    This microservice manages the lyrics of the band's most popular songs using a MongoDB database. It supports full CRUD operations and provides additional endpoints for health checks and counting the number of songs. The PyMongo library is used for seamless interaction with MongoDB.

    **Endpoints:**

    | Action | Method | Return Code    | Body                            | URL Endpoint |
    | ------ | ------ | -------------- | ------------------------------- | ------------ |
    | List   | GET    | 200 OK         | Array of songs `[{...}]`        | /song        |
    | Create | POST   | 201 CREATED    | A song resource as JSON `{...}` | /song        |
    | Read   | GET    | 200 OK         | A song as JSON `{...}`          | /song/{id}   |
    | Update | PUT    | 200 OK         | A song as JSON `{...}`          | /song/{id}   |
    | Delete | DELETE | 204 NO CONTENT | `""`                            | /song/{id}   |
    | Health | GET    | 200 OK         | `""`                            | /health      |
    | Count  | GET    | 200 OK         | `""`                            | /count       |

### 🔹 Database

- **MongoDB** for storing and retrieving song lyrics
- **SQLite** for managing Django application data

### 🔹 Main Application

- **Django** for core web application (MVC structure)
- **Django Templates** for rendering views with Bootstrap styling
- **Django Auth** for user registration, login, and role-based access control
- **SQLite** database for storing concert and user registration data
- **Requests** library for consuming Flask microservices APIs

**Core Features:**

| Feature            | URL Pattern       | Description                                     | Access Level  |
| ------------------ | ----------------- | ----------------------------------------------- | ------------- |
| Home Page          | `/`               | Band introduction and featured content          | Public        |
| Songs List         | `/songs/`         | Display all song titles from Songs microservice | Public        |
| Photo Gallery      | `/photos/`        | Concert pictures from Pictures microservice     | Public        |
| User Login         | `/login/`         | Authentication for registered users             | Public        |
| User Signup        | `/signup/`        | New user registration                           | Public        |
| Concerts List      | `/concerts/`      | View upcoming concerts and registrations        | Authenticated |
| Concert Details    | `/concerts/<id>/` | Individual concert information                  | Authenticated |
| Concert Management | `/admin/`         | CRUD operations for concerts                    | Admin Only    |

**Django App Structure:**

- **concert/models.py** - Concert and UserRegistration data models
- **concert/views.py** - Business logic and microservice integration
- **concert/forms.py** - User input forms for registration and concert management
- **templates/** - HTML templates with responsive Bootstrap design
- **static/** - CSS, JavaScript, and image assets

**Microservice Integration:**

- Consumes Songs API at `/song` endpoint for lyrics display
- Fetches concert photos from Pictures API at `/picture` endpoint
- Handles API errors gracefully with fallback content

**Authentication & Authorization:**

- Django's built-in User model for account management
- Session-based authentication
- Role-based access (Admin users can manage concerts)
- User registration tracking for concert attendance

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
├── get_picture_service/       # Flask microservice for event images
├── get_songs_service/         # Flask + MongoDB microservice for song lyrics
├── main_django_app/           # Django web application
└── README.md
```

---

## 🧪 Health Checks

Each microservice exposes a `/health` endpoint to monitor its status.

---

## 🚀 Deployment Instructions

### 📱 Pictures Microservice - IBM Code Engine

Deploy the pictures microservice to IBM Code Engine using the source-to-image method:

| Step | Command                   | Description                                                                                                                        |
| ---- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Start Code Engine project | Initialize your Code Engine environment                                                                                            |
| 2    | Configure namespace       | Set up the container registry namespace                                                                                            |
| 3    | Build image               | `docker build -t us.icr.io/${SN_ICR_NAMESPACE}/pictures:1 .`                                                                       |
| 4    | Push to registry          | `docker push us.icr.io/$SN_ICR_NAMESPACE/pictures:1`                                                                               |
| 5    | Deploy application        | `ibmcloud ce app create --name pictures --image us.icr.io/${SN_ICR_NAMESPACE}/pictures:1 --registry-secret icr-secret --port 3000` |

### 🎵 Songs Microservice - RedHat OpenShift

Deploy the songs microservice to RedHat OpenShift with MongoDB:

**1. Install MongoDB on OpenShift:**

```yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: mongo
spec:
  lookupPolicy:
    local: false
  tags:
    - name: latest
      from:
        kind: DockerImage
        name: docker.io/library/mongo:latest
```

**2. Deploy the Songs Service:**

```bash
# Get project details
oc get project

# Deploy application with source-to-image
oc new-app https://github.com/${GITHUB_ACCOUNT}/Back-End-Development-Songs \
  --strategy=source \
  --name=songs \
  --env MONGODB_SERVICE=mongo.{OPENSHIFT_PROJECT}.svc.cluster.local

# Monitor build logs
oc logs -f buildconfig/songs

# Expose to internet
oc expose service/songs
oc get route songs
```

### 🌐 Django Application - IBM Kubernetes Service

Deploy the Django application on IBM Kubernetes Service (IKS):

1. Create a Dockerfile for the Django application
2. Build and push the image to IBM Container Registry (ICR)
3. Generate YAML files for Kubernetes deployment
4. Apply configurations to the IBM Kubernetes Cluster

---

## 🌐 Live Demo

- **Pictures Service**: https://pictures.1wgl1isji4om.us-south.codeengine.appdomain.cloud
- **Songs Service**: http://songs-sn-labs-tanimbsmrstu.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud

---

## 🤝 Contributing

Contributions are welcome. Please fork the repository and open a pull request.

---

every application has setup.sh to install and configure the environment , make sure its included

update readme , update the main application deploy process
add screenshots
get the url of main application
