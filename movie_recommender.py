from numpy import float64
import pandas as pd

item_similarity_df = pd.read_csv(
    "datasets/item_similarity_df.csv", index_col=0)


def seen(recommended_movie, watched_movies):
    for movie in watched_movies:
        if recommended_movie == movie["title"]:
            return True
    return False


def get_similar_movies(movie_name, user_rating):
    try:
        similar_score = item_similarity_df[movie_name]*(user_rating-2.5)
        similar_movies = similar_score.sort_values(ascending=False)
    except KeyError:
        similar_movies = pd.Series([], dtype=float64)
    return similar_movies


def get_recommendations(watched_movies):

    print(watched_movies)
    similar_movies = pd.DataFrame()

    for movie in watched_movies:
        similar_movies = similar_movies.append(get_similar_movies(
            movie["title"], movie["rating"]), ignore_index=True)

    all_recommend = similar_movies.sum().sort_values(ascending=False)

    recommended_movies = []
    for movie, score in all_recommend.iteritems():
        if not seen(movie, watched_movies):
            recommended_movies.append(movie)

    if len(recommended_movies) > 100:
        recommended_movies = recommended_movies[0:100]

    return recommended_movies
