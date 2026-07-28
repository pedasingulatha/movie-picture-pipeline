import os
from flask import Flask
from flask_cors import CORS
from .resources import Movies
from flask import Blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

movies_api = Blueprint("movies_api", __name__)
movies = Movies.as_view("movies")

movies_api.add_url_rule("/movies", strict_slashes=False, defaults={"movie_id": None}, view_func=movies, methods=["GET"])
movies_api.add_url_rule("/movies", view_func=movies, methods=["POST"])
movies_api.add_url_rule("/movies/<int:movie_id>", view_func=movies, methods=["GET", "PUT", "DELETE"])

app.register_blueprint(movies_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_RUN_PORT", 5000)))
