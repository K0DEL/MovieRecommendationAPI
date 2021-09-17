from main import Movie, db
import json


file = open('movies.json')
data = json.load(file)['movies']

movies = []
for movie_data in data:
    movies.append(movie_data)

print(len(movies))

for movie in movies:
    new_movie = Movie(
        movieId=movie['movieId'],
        title=movie['title'],
        originalTitle=movie['originalTitle'],
        year=movie['year'],
        genres=movie['genres'],
        director=movie['director'],
        writer=movie['writer'],
        actors=movie['actors'],
        plot=movie['plot'],
        poster=movie['poster'],
        imdbRating=movie['imdbRating'],
        imdbVotes=movie['imdbVotes'],
        imdbID=movie['imdbID']
    )
    db.session.add(new_movie)

db.session.commit()
print("Completed")
