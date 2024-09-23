# Flask API Project
Project Overview
This project is a simple RESTful API built with Python's Flask framework, demonstrating how to manage user data with token-based authentication (JWT) and perform basic CRUD (Create, Read, Update, Delete) operations on a user database. The API is deployed on Heroku, making it accessible over the web.

# Features:
User Authentication: Login functionality that generates a JSON Web Token (JWT) for secure access to protected endpoints.
CRUD Operations:
_Create: Add new users to the database.
Read: Retrieve a list of all users.
Update: Modify user details.
Delete: Remove users from the database.
_
Error Handling: Basic error handling for common HTTP errors (404, 500, etc.).

# Technologies Used:
Python: Main programming language.
Flask: Web framework for building the API.
Flask-SQLAlchemy: ORM (Object Relational Mapper) for database management.
Flask-JWT-Extended: For handling authentication with JSON Web Tokens.
Gunicorn: WSGI server for deploying the app on Heroku.
Heroku: Cloud platform for deploying the application.

# Getting Started
To recreate the project, follow these steps:
Disclaimer: These steps are primarily for someone who wants to recreate the project on their own machine or deploy it themselves, but they can also be used to run and interact with the already-deployed project (mine).

# Prerequisites
Python 3.x installed on your machine
pip for managing Python packages

# Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/fidelfunez/flask-api-project.git
cd flask-api-project

Create a virtual environment and activate it:
bash
Copy code
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:
bash
Copy code
pip install -r requirements.txt

Run the Flask app:
bash
Copy code
flask run

API Endpoints
Login (Generate Token)

URL: /login
Method: POST
Data:
json
Copy code
{
  "username": "admin",
  "password": "password"
}
Response:
json
Copy code
{
  "access_token": "your_jwt_token"
}
Get All Users

URL: /users
Method: GET
Headers:
json
Copy code
{
  "Authorization": "Bearer your_jwt_token"
}
Response:
json
Copy code
{
  "users": [
    {"id": 1, "name": "Jane Doe", "email": "jane@example.com"},
    ...
  ]
}
Create User

URL: /users
Method: POST
Data:
json
Copy code
{
  "name": "John Doe",
  "email": "john@example.com"
}
Update User

URL: /users/<user_id>
Method: PUT
Data:
json
Copy code
{
  "name": "Updated Name"
}
Delete User

URL: /users/<user_id>
Method: DELETE
Deployment
The API is deployed on Heroku at this URL. You can use the endpoints as described above by replacing the localhost URLs with the live link.

Deploy to Heroku
If you want to deploy your own version on Heroku:

Create a new Heroku app:

bash
Copy code
heroku create your-app-name
Push your code to Heroku:

bash
Copy code
git push heroku main
Scale the web dyno:

bash
Copy code
heroku ps:scale web=1
Future Improvements
Add pagination for user retrieval.
Implement user role management for admin-level access.
Improve error handling and logging.

License
This project is licensed under the MIT License - see the LICENSE file for details.
