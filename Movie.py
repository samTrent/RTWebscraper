#An object that holds all the data for a movie
class Movie:
    def __init__(self, title, movieSynopsis ,tomatometer, audienceScore, totalCriticReviews, totalAudienceReviews, rating, runtime, inTheaters, director, writer, genre, studio):
        self.title = title
        self.movieSynopsis = movieSynopsis
        self.tomatometer = tomatometer
        self.audienceScore = audienceScore
        self.totalCriticReviews = totalCriticReviews
        self.totalAudienceReviews = totalAudienceReviews
        self.rating = rating
        self.runtime = runtime
        self.inTheaters = inTheaters
        self.director = director
        self.writer = writer
        self.genre = genre
        self.studio = studio
    
    def getTomatometerRating(self):
        return self.tomatometer
    
    def getAudienceScore(self):
        return self.audienceScore

    def getTotalAudienceReviews(self):
        return self.totalAudienceReviews

#Do any necissary processing when creating the movie object
def buildMovieObject(title, movieSynopsis ,tomatometer, audienceScore, totalCriticReviews, totalAudienceReviews, rating, runtime, inTheaters, director, writer, genre, studio):
    return Movie(title, movieSynopsis ,tomatometer, audienceScore, totalCriticReviews, totalAudienceReviews, rating, runtime, inTheaters, director, writer, genre, studio)
