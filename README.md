# Healthcare Management System API

A Healthcare Management System API built using Django REST Framework (DRF), PostgreSQL, and JWT Authentication. The system enables authenticated users to manage patients, doctors, and patient-doctor assignments through secure RESTful APIs.

---

## Overview

This project provides a backend solution for healthcare management, allowing users to:

* Register and authenticate using JWT
* Manage patient records
* Manage doctor records
* Assign doctors to patients
* View patient-doctor relationships
* Remove doctor assignments from patients

The application follows RESTful API principles and uses PostgreSQL for persistent data storage.

---

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Protected API Access

### Patient Management

* Create Patient
* Retrieve All Patients Created By Logged-In User
* Retrieve Patient Details
* Update Patient Information
* Delete Patient

### Doctor Management

* Create Doctor
* Retrieve All Doctors
* Retrieve Doctor Details
* Update Doctor Information
* Delete Doctor

### Patient-Doctor Mapping

* Assign Doctor To Patient
* Retrieve All Patient-Doctor Mappings
* Retrieve All Doctors Assigned To A Patient
* Remove Doctor Assignment From A Patient

### API Documentation

* Swagger UI Documentation
* OpenAPI Schema Generation

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* PostgreSQL

### Authentication

* JWT Authentication
* djangorestframework-simplejwt

### API Documentation

* drf-spectacular
* Swagger UI

### Development Tools

* Postman
* Git
* GitHub
* VS Code

---

## Project Structure

```text
healthcare/
│
├── accounts/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── patients/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── doctors/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── healthcare/
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
├── manage.py
└── README.md
```

---

## Installation and Setup

### Prerequisites

* Python 3.10+
* PostgreSQL
* Git

### Clone Repository

```bash
git clone <repo-url>

cd healthcare
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows

```bash
env\Scripts\activate
```

Linux / macOS

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Application will be available at:

```text
http://127.0.0.1:8000/
```

---


## Authentication

All protected endpoints require JWT Authentication.

Header:

```http
Authorization: Bearer <access_token>
```

---

# API Endpoints

## Authentication APIs

### Register User

```http
POST /api/auth/register/
```

Request

```json
{
    "username": "anurag",
    "email": "anurag@example.com",
    "password": "password123"
}
```

Response

```json
{
    "id": id,
    "username": usernamae,
    "first_name": firstname,
    "last_name": lastname,
    "email": email.id
}
```

---

### Login User

```http
POST /api/auth/login/
```

Request

```json
{
    "username": "anurag",
    "password": "password123"
}
```

Response

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## Patient Management APIs

### Create Patient

```http
POST /api/patients/
```

Request

```json
{
    "name": "Rahul Sharma",
    "age": 25,
    "gender": "M",
    "phone": "9876543210"
}
```

Response

```json
{
    "message": "Patient created successfully"
}
```

---

### Get All Patients

```http
GET /api/patients/
```

Returns all patients created by the authenticated user.

---

### Get Patient Details

```http
GET /api/patients/<id>/
```

---

### Update Patient

```http
PUT /api/patients/<id>/
```

Request

```json
{
    "name": "Rahul Sharma",
    "age": 26,
    "gender": "M",
    "phone": "9876543210"
}
```

---

### Delete Patient

```http
DELETE /api/patients/<id>/
```

Response

```json
{
    "message": "Patient deleted"
}
```

---

## Doctor Management APIs

### Create Doctor

```http
POST /api/doctors/
```

Request

```json
{
    "name": "Dr Amit",
    "specialization": "Cardiologist"
}
```

---

### Get All Doctors

```http
GET /api/doctors/
```

---

### Get Doctor Details

```http
GET /api/doctors/<id>/
```

---

### Update Doctor

```http
PUT /api/doctors/<id>/
```

---

### Delete Doctor

```http
DELETE /api/doctors/<id>/
```

---

## Patient-Doctor Mapping APIs

### Assign Doctor To Patient

```http
POST /api/mappings/
```

Request

```json
{
    "patient_id": 1,
    "doctor_id": 2
}
```

Response

```json
{
    "message": "Doctor assigned",
    "mapping_id": 1
}
```

---

### Retrieve All Mappings

```http
GET /api/mappings/
```

Response

```json
[
    {
        "id": 1,
        "patient": "Rahul Sharma",
        "doctor": "Dr Amit"
    }
]
```

---

### Get All Doctors Assigned To Patient

```http
GET /api/mappings/<patient_id>/
```

Response

```json
{
    "patient": "Rahul Sharma",
    "doctors": [
        {
            "id": 1,
            "name": "Dr Amit"
        }
    ]
}
```

---

### Remove Doctor Assignment

```http
DELETE /api/mappings/<mapping_id>/
```

Response

```json
{
    "message": "Mapping removed"
}
```

---

## Validation Rules

### Patient Validation

* Name is required
* Age must be greater than zero
* Phone number must contain exactly 10 digits
* Gender must be valid

### Mapping Validation

* Patient must exist
* Doctor must exist
* Duplicate patient-doctor mappings are not allowed

---

## Future Improvements

* Role-Based Access Control
* Appointment Management
* Medical Records Management
* Doctor Availability Scheduling

---

## Author

Anurag Singh

GitHub: https://github.com/anurag433

