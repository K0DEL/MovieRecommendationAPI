# Movies

An API to get the recommendations for the movies selected by the user.The API also returns details of a particular movie based on it's ID or title.

#

## GET

**getRecommendedData**

This calls takes in a number of movies and their ratings from the user and returns 100 movie that match the most to the user's desires.

        https://kodelmovieapi.herokuapp.com/getRecommendedData?size=1&id_1=122912&rating_1=5

### PARAMS

- size

  _total number of movies being sent_

- id_1

  _id of the ith movie is denoted with id_i_

- rating_1

  _rating of the ith movie is denoted with rating_i_

#

## GET

**SearchImdbID**

This Call takes in the imdbID of the movie and returns the details of the same.

    https://kodelmovieapi.herokuapp.com/searchImdbID?imdbID=tt0114709

### PARAMS

- imdbID

  _imdbID of the movie being searched_

#

## GET

**searchMovieTitle**

This Call takes in the title of the movie and returns the details of the same.

        https://kodelmovieapi.herokuapp.com/searchMovieTitle?title=Avengers: Infinity War

### PARAMS

- title

  _title of the movie being searched_

#

## GET

**searchMovieID**

This Call takes in the movieID of the movie and returns the details of the same.

        https://kodelmovieapi.herokuapp.com/searchMovieID?id=1307

### PARAMS

- id

  _movieID of the movie being searched_

#

## GET

**allMovies**

Returns all the movies available in the database of the API.

        https://kodelmovieapi.herokuapp.com/allMovies
