# 🏋️ Workout Tracker

A full stack workout tracking application with a Django REST API and a lightweight React frontend. This project allows users to create, view, and manage workouts and exercises, demonstrating end-to-end client-server integration.

## 🚀 Tech Stack

Backend

- Python
- Django
- Django REST Framework

Frontend

- React
- JavaScript

Tools

- Postman (API testing)
- SQLite

## ✨ Features

- Create, read, update, and delete workouts
- Manage exercises within workouts
- RESTful API design with structured endpoints
- React frontend consuming backend API
- Modular and extensible backend architecture

## 🔌 API Overview

Example endpoints:

```
GET /api/workouts/  # Get all workouts
POST /api/workouts/   # Create a new workout
GET /api/workouts/:id   # Get a single workout
PUT /api/workouts/:id   # Update a workout
DELETE /api/workouts/:id  # Delete a workout
```

Example request:

POST /api/workouts/

```
{
"name": "Push Day",
"date": "2026-04-05"
}
```

## ⚙️ Getting Started

1. Clone the repo

   ```
   git clone https://github.com/your-username/workout-tracker.git
   cd workout-tracker
   ```

2. Backend Setup
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate # Mac/Linux
   ```

# venv\Scripts\activate # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 3. Frontend Setup
cd frontend
npm install
npm start
🔮 Future Improvements
User authentication (JWT)
Workout history and analytics
Improved UI/UX styling
Deployment (Render / Vercel)
Pagination and filtering for workouts
