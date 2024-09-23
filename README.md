# Flask API Project
**Project Overview:**
This project is a simple RESTful API built with Python's Flask framework, demonstrating how to manage user data with token-based authentication (JWT) and perform basic CRUD (Create, Read, Update, Delete) operations on a user database. The API is deployed on Heroku, making it accessible over the web.

# Features:

- User Authentication: Login functionality that generates a JSON Web Token (JWT) for secure access to protected endpoints.
- CRUD Operations:
  - Create: Add new users to the database.
  - Read: Retrieve a list of all users.
  - Update: Modify user details.
  - Delete: Remove users from the database.
  
- Error Handling: Basic error handling for common HTTP errors (404, 500, etc.).

# Technologies Used:
- Python: Main programming language.
- Flask: Web framework for building the API.
- Flask-SQLAlchemy: ORM (Object Relational Mapper) for database management.
- Flask-JWT-Extended: For handling authentication with JSON Web Tokens.
- Gunicorn: WSGI server for deploying the app on Heroku.
- Heroku: Cloud platform for deploying the application.

# Getting Started
- To recreate the project, follow these steps:
- Disclaimer: These steps are primarily for someone who wants to recreate the project on their own machine or deploy it themselves, but they can also be used to run and interact with the already-deployed project (mine).

# Prerequisites
- Python 3.x installed on your machine
- pip for managing Python packages

# Installation
**1.** Clone the repository to your local machine -
You can copy the following code if you like (BASH):
- git clone https://github.com/fidelfunez/flask-api-project.git
- cd flask-api-project

**2.** Create a virtual environment and activate it:
- python3 -m venv venv
- source venv/bin/activate

**3.** Install the required dependencies:
- pip install -r requirements.txt

**4.** Run the Flask app:
- flask run

# API Endpoints
**1.** Login (Generate Token) - You can copy the following code if you like (json):
- URL: /login
- Method: POST
- Data:
{
    "username": "admin",
    "password": "password"
  }
  
- Response:
{
  "access_token": "your_jwt_token"
}

**2.** Get All Users:
- URL: /users
- Method: GET
- Headers:
{
  "Authorization": "Bearer your_jwt_token"
}

- Response:
{
  "users": [
    {"id": 1, "name": "Jane Doe", "email": "jane@example.com"},
    ...
  ]
}

**3.** Create User:
- URL: /users
- Method: POST
- Data:
{
  "name": "John Doe",
  "email": "john@example.com"
}

**4.** Update User
- URL: /users/<user_id>
- Method: PUT
- Data:
{
  "name": "Updated Name"
}

**5.** Delete User
- URL: /users/<user_id>
- Method: DELETE

# Deployment
The API is deployed on Heroku at this URL: https://flask-api-project-eff327bad6ee.herokuapp.com/. You can use the endpoints as described above by replacing the localhost URLs with the live link.

**Deploy to Heroku**

**If you want to deploy your own version on Heroku:**
-
**1.** Create a new Heroku app -
Copy code if you like (BASH):
- heroku create your-app-name

**2.** Push your code to Heroku:
- git push heroku main

**3.** Scale the web dyno:
- heroku ps:scale web=1
  
# Future Improvements
- Add pagination for user retrieval.
- Implement user role management for admin-level access.
- Improve error handling and logging.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
