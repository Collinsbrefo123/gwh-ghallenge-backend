# Django Todo API
This is a Django REST Framework (DRF) application serving as the backend for the Todo application frontend built with React.js. The API provides endpoints for creating and reading todos.

## Features
Exposes RESTful API endpoints for creating and retrieving todos.
Utilizes Django models to define the todo data structure.
Implements CRUD operations for managing todos.

## Technologies Used
Backend Framework: Django
REST Framework: Django REST Framework (DRF)
Database: SQLite (for simplicity, can be replaced with other databases supported by Django)

## Getting Started
1. Clone this repository: https://github.com/Collinsbrefo123/gwh-ghallenge-backend.git
2. Navigate to the project directory: cd gwh-ghallenge-backend
3. Create and activate a virtual environment (optional but recommended): 
   4. python -m venv env
   source env/bin/activate  # On Unix/Mac
   env\Scripts\activate     # On Windows
4. Install dependencies: pip install -r requirements.txt
5. Run migrations to create the database schema: Run migrations to create the database schema: python manage.py migrate
6. Start the django Project: python manage.py runserver


