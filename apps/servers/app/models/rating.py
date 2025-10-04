from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

rating_bp = Blueprint('rating', __name__)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Values can be 1–5

    def __repr__(self):
        return f"<Rating (id={self.id}, rating={self.rating}, user_id={self.user_id}, recipe_id={self.recipe_id})>"

@rating_bp.route('/recipe/<int:recipe_id>/rate', methods=['POST'])
def rate_recipe(recipe_id):
    data = request.get_json()
    rating_value = data.get('rating')
    user_id = data.get('user_id')

    if not (1 <= rating_value <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400

    # Save rating
    rating = Rating(recipe_id=recipe_id, user_id=user_id, rating=rating_value)
    db.session.add(rating)
    db.session.commit()
    return jsonify({'message': 'Rating added successfully'}), 201

@rating_bp.route('/recipe/<int:recipe_id>/average-rating', methods=['GET'])
def average_rating(recipe_id):
    avg_rating = db.session.query(func.avg(Rating.rating)).filter_by(recipe_id=recipe_id).scalar()
    avg_rating = round(avg_rating, 2) if avg_rating else None
    return jsonify({'recipe_id': recipe_id, 'average_rating': avg_rating})

# To activate: register rating_bp in your application factory or main app
