from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database.db import get_connection
from utils.security import hash_password, verify_password

auth = Blueprint("auth", __name__)


# ==========================
# Register API
# ==========================
@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Invalid JSON data"
        }), 400

    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")

    if not full_name or not email or not password:
        return jsonify({
            "error": "All fields are required"
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    if user:
        cursor.close()
        conn.close()

        return jsonify({
            "error": "Email already exists"
        }), 400

    # Hash the password
    hashed_password = hash_password(password)

    # Insert new user
    cursor.execute(
        """
        INSERT INTO users (full_name, email, password_hash)
        VALUES (%s, %s, %s)
        """,
        (full_name, email, hashed_password)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "User Registered Successfully"
    }), 201


# ==========================
# Login API
# ==========================
@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Invalid JSON data"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email and Password are required"
        }), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT user_id, full_name, email, password_hash
        FROM users
        WHERE email=%s
        """,
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return jsonify({
            "error": "Invalid Email"
        }), 401

    user_id, full_name, email, password_hash = user

    # Verify password
    if not verify_password(password, password_hash):
        return jsonify({
            "error": "Invalid Password"
        }), 401

    # Generate JWT Token
    access_token = create_access_token(identity=str(user_id))

    return jsonify({
        "message": "Login Successful",
        "access_token": access_token,
        "user": {
            "user_id": user_id,
            "full_name": full_name,
            "email": email
        }
    }), 200