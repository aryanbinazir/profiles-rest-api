
# Profiles REST API

A simple Django REST Framework project for managing user profiles and authentication.  
This project is designed as a learning exercise to understand core REST principles using Django.

## 🚀 Features

- ✅ Full CRUD operations for user profiles
- 🔐 Token-based authentication with login support
- 📡 Browsable Django REST API
- 🧪 Basic test coverage
- 🐳 Vagrant environment for consistent development setup

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- Vagrant & VirtualBox (for development)

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aryanbinazir/profiles-rest-api.git
cd profiles-rest-api
```

### 2. Start with Vagrant

Make sure you have [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) installed.

```bash
vagrant up
vagrant ssh
cd /vagrant
```

### 3. Activate Virtual Environment

```bash
source ~/env/bin/activate
```

### 4. Run the Django Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Visit `http://localhost:8000` in your browser.

## 🔍 API Overview

### Create User Profile

`POST /api/profile/`  
Create a new user with name, email, and password.

### Get All Profiles

`GET /api/profile/`  
List all registered user profiles (requires auth).

### Update/Delete Profile

`PUT/PATCH/DELETE /api/profile/<id>/`  
Update or delete a user profile (only by owner).

### Login & Get Auth Token

`POST /api/login/`  
Pass valid credentials to receive an auth token.

## 🔐 Authentication

Use the token obtained from login in the `Authorization` header:

```
Authorization: Token your_token_here
```

## 🧪 Running Tests

```bash
python manage.py test
```

## 📂 Project Structure (simplified)

```
profiles-rest-api/
├── app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── tests.py
├── profiles_project/
├── Vagrantfile
└── requirements.txt
```


