"""
Flask Travel Destinations API

A simple REST API for managing travel destinations.
Supports CRUD operations with SQLite database.

Run with: python main.py
Test with: curl http://127.0.0.1:5000/destinations
"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
db = SQLAlchemy(app)


class Destination(db.Model):
    """Database model for travel destinations."""
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert destination to dictionary for JSON response."""
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating
        }


# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Root endpoint - API welcome message."""
    return jsonify({"message": "Welcome to Travel Destinations API"})


@app.route("/destinations", methods=["GET"])
def get_destinations():
    """Get all travel destinations."""
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])


@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    """Get a specific destination by ID."""
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    return jsonify({"error": "Destination not found"}), 404


@app.route("/destinations", methods=["POST"])
def add_destination():
    """Add a new destination.

    Expected JSON:
    {
        "destination": "Paris",
        "country": "France",
        "rating": 4.8
    }
    """
    data = request.get_json()

    # Validate required fields
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "destination" not in data or not data["destination"]:
        return jsonify({"error": "Destination name is required"}), 400

    if "country" not in data or not data["country"]:
        return jsonify({"error": "Country is required"}), 400

    if "rating" not in data:
        return jsonify({"error": "Rating is required"}), 400

    # Validate rating range
    try:
        rating = float(data["rating"])
        if rating < 0 or rating > 5:
            return jsonify({"error": "Rating must be between 0 and 5"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Rating must be a number"}), 400

    # Validate string lengths
    if len(data["destination"]) > 100:
        return jsonify({"error": "Destination name too long (max 100 characters)"}), 400

    if len(data["country"]) > 50:
        return jsonify({"error": "Country name too long (max 50 characters)"}), 400

    new_destination = Destination(
        destination=data["destination"],
        country=data["country"],
        rating=rating
    )
    db.session.add(new_destination)
    db.session.commit()
    return jsonify(new_destination.to_dict()), 201


@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    """Update an existing destination."""
    data = request.get_json()
    destination = Destination.query.get(destination_id)
    
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)
        db.session.commit()
        return jsonify(destination.to_dict())
    
    return jsonify({"error": "Destination not found"}), 404


@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):
    """Delete a destination."""
    destination = Destination.query.get(destination_id)

    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({"message": "Destination deleted successfully"})

    return jsonify({"error": "Destination not found"}), 404


# Custom error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found", "message": "The requested resource was not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors with database rollback."""
    db.session.rollback()
    return jsonify({"error": "Internal server error", "message": "An unexpected error occurred"}), 500


@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return jsonify({"error": "Bad request", "message": "The request was invalid"}), 400


if __name__ == "__main__":
    import os
    # Use environment variable for debug mode (default to False for production)
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    print(f"\n🚀 Starting Travel Destinations API")
    print(f"📍 Server: http://127.0.0.1:5000")
    print(f"📖 Docs: http://127.0.0.1:5000/destinations")
    print(f"🔧 Debug mode: {debug_mode}")
    print(f"\n⚠️  Set FLASK_DEBUG=true to enable debug mode\n")
    app.run(debug=debug_mode)
