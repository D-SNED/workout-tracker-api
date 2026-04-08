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
"date": "2026-04-05",
"notes": "Chest, Shoulders and Triceps"
}
```

## ⚙️ Getting Started

1. Clone the repo

   ```
   git clone https://github.com/D-SNED/workout-tracker-api.git
   cd workout-tracker-api
   ```

2. Backend Setup

   ```
   Make sure you are in the workout-tracker-api directory (cd workout-tracker-api), run the following commands:

   python -m venv venv
   source venv/bin/activate (Mac/Linux)
   # venv\Scripts\activate (Windows)
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

   the backend should run on localhost:8000
   ```

3. Frontend Setup

   ```
   open another terminal window (you will need two terminals to run this app), run the following commands:

   cd workout-tracker-frontend
   npm install
   npm start

   the frontend should run on localhost:5173
   ```

## 🔮 Future Improvements

- User authentication (JWT)
- Workout history and analytics
- Improved UI/UX styling
- Deployment (Render / Vercel)
- Pagination and filtering for workouts
