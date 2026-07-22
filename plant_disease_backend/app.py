from datetime import timedelta
import os

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager

from config import UPLOAD_FOLDER
from routes.auth import auth
from routes.predict import predict_bp
from routes.history import history_bp
from routes.profile import profile_bp
from routes.dashboard import dashboard_bp
from datetime import timedelta
app = Flask(__name__)

# ======================================
# Flask Configuration
# ======================================

app.config["JWT_SECRET_KEY"] = "plant_disease_secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)

# Maximum upload size (16 MB)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

# Enable CORS
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"]
)

@app.route("/test-token")
@jwt_required()
def test_token():
    return {
        "user_id": get_jwt_identity()
    }

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# JWT
jwt = JWTManager(app)

# ======================================
# Register Blueprints
# ======================================

app.register_blueprint(auth)
app.register_blueprint(predict_bp)
app.register_blueprint(history_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(dashboard_bp)
# ======================================
# Static Route for Uploaded Images
# ======================================

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ======================================
# Home Route
# ======================================

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Plant Disease Detection Backend is Running",
        "version": "1.0"
    }

# ======================================
# Run Server
# ======================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )