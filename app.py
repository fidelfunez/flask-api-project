from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import re

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, this is your Flask API!"

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

# Create the database
with app.app_context():
    db.create_all()

# Helper function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Login route to generate JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data["username"] == "admin" and data["password"] == "password":  # Simplified login
        access_token = create_access_token(identity={"username": data["username"]})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials!"}), 401

# API routes for CRUD operations

# GET /users with pagination
@app.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    users = User.query.paginate(page=page, per_page=per_page)
    return jsonify({
        "users": [{"id": user.id, "name": user.name, "email": user.email} for user in users.items],
        "total": users.total,
        "pages": users.pages
    })

# POST /users (Add a new user) - Requires JWT token
@app.route('/users', methods=['POST'])
@jwt_required()
def add_user():
    data = request.get_json()

    # Validate input
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required!"}), 400

    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email format!"}), 400

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added!"}), 201

# PUT /users/<id> (Update a user) - Requires JWT token
@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found!"}), 404

    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Name is required!"}), 400

    user.name = data["name"]
    db.session.commit()
    return jsonify({"message": "User updated!"}), 200

# DELETE /users/<id> (Delete a user) - Requires JWT token
@app.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found!"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted!"}), 200

if __name__ == "__main__":
    app.run(debug=True)

