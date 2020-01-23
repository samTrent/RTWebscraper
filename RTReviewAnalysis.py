import UserReview
import CriticReview

#
#   Contains functions for conducting analysis on 
#   movie review data
#


# User review analysis
def getUserReviewScoreAvg(reviews):
    reviewAvg = 0
    for review in reviews:
        reviewAvg += review.getScore()
      
    
    return reviewAvg / len(reviews)

def getUserReviewScorePercent(reviews):
    userScoresGreaterThan3Point5 = 0
    for review in reviews:
        if float(review.getScore()) >= 3.5:
            userScoresGreaterThan3Point5 += 1
    
    return (userScoresGreaterThan3Point5 * 100.00) / float(len(reviews))

# Critic review analysis
def getCriticFreshRatingPercent(reviews):
    numberOfCriticsRatedFresh = 0
    for review in reviews:
        if float(review.getFreshRating() == True):
            numberOfCriticsRatedFresh += 1
    
    return (numberOfCriticsRatedFresh * 100.00) / float(len(reviews))