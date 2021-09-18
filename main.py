from flask_sqlalchemy import SQLAlchemy
import os
from movie_recommender import get_recommendations
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "sqlite:///movies.db").replace("s://", "sql://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

POSTMAN_URL = "https://documenter.getpostman.com/view/14999299/UUxtDVjK"


class Movie(db.Model):

    __tablename__ = 'movies'

    movieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    originalTitle = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genres = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    writer = db.Column(db.String, nullable=False)
    actors = db.Column(db.String, nullable=False)
    plot = db.Column(db.String, nullable=False)
    poster = db.Column(db.String, nullable=False)
    imdbRating = db.Column(db.String, nullable=False)
    imdbVotes = db.Column(db.String, nullable=False)
    imdbID = db.Column(db.String, nullable=False)

    def items(self):
        return {column.name: getattr(self, column.name)
                for column in self.__table__.columns}


db.create_all()


def get_watched_movies(movie_ids, ratings):
    movies = []
    for id in movie_ids:
        movie = Movie.query.get(id)
        movies.append(movie)

    watched_movies = []
    try:
        i = 0
        for movie in movies:
            watched_movies.append({
                "movieId": int(movie.movieId),
                "title": f"{movie.title}({movie.year})",
                "rating": ratings[i]
            })
            i += 1
    except AttributeError:
        return []
    return watched_movies


def get_recommended_movies(recommended_titles):
    recommendations = []
    for title in recommended_titles:
        movie = db.session.query(Movie).filter_by(title=title[:-6]).first()
        recommendations.append(movie.items())

    return recommendations


def get_movie_by_id(id):
    try:
        movie = Movie.query.get(id)
        return movie.items()
    except AttributeError:
        return None


def get_movie_by_imdbID(imdbID):
    try:
        movie = db.session.query(Movie).filter_by(imdbID=imdbID).first()
        return movie.items()
    except AttributeError:
        return None


def get_movie_by_title(title):
    try:
        movie = db.session.query(Movie).filter_by(originalTitle=title).first()
        return movie.items()
    except AttributeError:
        return None


@app.route("/")
def documentation():
    return redirect(POSTMAN_URL)


@app.route("/getRecommendedData")
def getRecommendedData():
    try:
        size = int(request.args.get('size'))
        movie_ids = []
        ratings = []
        for i in range(1, size + 1):
            movie_ids.append(request.args.get(f'id_{i}'))
            ratings.append(int(request.args.get(f'rating_{i}')))

        watched_movies = get_watched_movies(movie_ids, ratings)
        recommended_titles = get_recommendations(watched_movies)
        recommendations = get_recommended_movies(recommended_titles)
        return jsonify(recommendations=recommendations), 200
    except TypeError:
        return jsonify(Error="Inappropriate Request"), 405


@app.route("/searchMovieID")
def searchMovieID():
    try:
        id = request.args.get('id')
        movie = get_movie_by_id(id)
        return jsonify(movie=movie), 200
    except TypeError:
        return jsonify(Error="Inappropriate Request"), 405


@app.route("/searchImdbID")
def searchImdbID():
    try:
        imdbID = request.args.get('imdbID')
        movie = get_movie_by_imdbID(imdbID)
        return jsonify(movie=movie), 200
    except TypeError:
        return jsonify(Error="Inappropriate Request"), 405


@app.route("/searchMovieTitle")
def searchMovieTitle():
    try:
        title = request.args.get('title')
        movie = get_movie_by_title(title)
        return jsonify(movie=movie), 200
    except TypeError:
        return jsonify(Error="Inappropriate Request"), 405


@app.route("/allMovies")
def getAllMovies():
    movies = [movie.items() for movie in db.session.query(Movie).all()]
    data = {
        "size": len(movies),
        "movies": movies
    }
    return jsonify(all_movies=data), 200


if __name__ == '__main__':
    app.run(debug=True)
