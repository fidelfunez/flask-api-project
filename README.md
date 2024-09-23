## Flask API Project

**Project Overview:**
<a name="project-overview"></a>

This project is a simple RESTful API built with Python's Flask framework, demonstrating how to manage user data with token-based authentication (JWT) and perform basic CRUD (Create, Read, Update, Delete) operations on a user database. The API is deployed on Heroku, making it accessible over the web.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Getting Started](#getting-started)
   1. [Prerequisites](#prerequisites)
   2. [Installation](#installation)
5. [API Endpoints](#api-endpoints)
6. [Deployment](#deployment)
   1. [Deploy to Heroku](#deploy-to-heroku)
7. [Future Improvements](#future-improvements)
8. [License](#license)

## Features:
<a name="features"></a>

- ### User Authentication:
Login functionality that generates a JSON Web Token (JWT) for secure access to protected endpoints.
- ### CRUD Operations:
  - Create: Add new users to the database.
  - Read: Retrieve a list of all users.
  - Update: Modify user details.
  - Delete: Remove users from the database.
  
- ### Error Handling

   The API implements basic error handling for common issues. For example:

- **404 Not Found**: When trying to access a user that doesn't exist.
  
  Example Response:
  ```json
  {
    "error": "User not found"
  }

- **500 Internal Server Error:** For unexpected errors, the server will respond with a 500 status.

  Example Response:
  ```json
  {
    "error": "Internal Server Error"
  }

## Technologies Used:
<a name="technologies-used"></a>
- [Python](https://www.python.org/): Main programming language.
- [Flask](https://flask.palletsprojects.com/): Web framework for building the API.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): ORM (Object Relational Mapper) for database management.
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/): For handling authentication with JSON Web Tokens.
- [Gunicorn](https://gunicorn.org/): WSGI server for deploying the app on Heroku.
- [Heroku](https://www.heroku.com/): Cloud platform for deploying the application.

## Getting Started
<a name="getting-started"></a>
**Disclaimer: These steps are primarily for someone who wants to recreate the project on their own machine or deploy it themselves, but they can also be used to run and interact with the already-deployed project (mine). While I've included code to easily copy and paste, I'd encourage you to write the code yourself, as writing yourself is what will help you grow and further improve in your journey, especially if you're a beginner. Happy coding! - FFC.** 

### To recreate the project, follow these steps:

## Prerequisites
<a name="prerequisites"></a>
- Python 3.x installed on your machine
- pip for managing Python packages

## Installation
<a name="instalation"></a>
You can copy the following code if you like (BASH):

**1. Clone the repository to your local machine:**
```bash
git clone https://github.com/fidelfunez/flask-api-project.git
```
```bash
cd flask-api-project
```

**2. Create a virtual environment and activate it:**
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

**3. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the Flask app:**
```bash
flask run
```

## API Endpoints
<a name="api-endpoints"></a>
You can copy the following code if you like (json):

**1. Login (Generate Token):**
- URL: `/login`
- Method: `POST`
- Data:
`{
    "username": "admin",
    "password": "password"
  }`
  
- Response:
`{
  "access_token": "your_jwt_token"
}`

**2. Get All Users:**
- URL: `/users`
- Method: `GET`
- Headers:
`{
  "Authorization": "Bearer your_jwt_token"
}`

- Response:
`{
  "users": [
    {"id": 1, "name": "Jane Doe", "email": "jane@example.com"},
    ...
  ]
}`

**3. Create User:**
- URL: `/users`
- Method: `POST`
- Data:
`{
  "name": "John Doe",
  "email": "john@example.com"
}`

**4. Update User**
- URL: `/users/<user_id>`
- Method: `PUT`
- Data:
`{
  "name": "Updated Name"
}`

**5. Delete User**
- URL: (`/users/<user_id>`)
- Method: (`DELETE`)

## Deployment
<a name="deployment"></a>
The API is deployed on Heroku at this [URL](https://flask-api-project-eff327bad6ee.herokuapp.com/). You can use the endpoints as described above by replacing the localhost URLs with the live link.

**Deploy to Heroku**
<a name="deploy-to-heroku"></a>
If you want to deploy your own version on Heroku:

You can copy the code if you like (BASH):

**1. Create a new Heroku app:**
```bash
heroku create your-app-name
```

**2. Push your code to Heroku:**
```bash
git push heroku main
```

**3. Scale the web dyno:**
```bash
heroku ps:scale web=1
```
  
## Future Improvements
<a name="future-improvements"></a>
- Add pagination for user retrieval.
- Implement user role management for admin-level access.
- Improve error handling and logging.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit: `git commit -m 'Added new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you'd like to change.

## License
<a name="license"></a>
This project is licensed under the MIT License - see the LICENSE file for details.
