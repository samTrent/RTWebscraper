#An object containing data for a single critic review
class CriticReview:
    def __init__(self, name, publication, isTopCritic, ratedFresh, reviewDescription, originalScore, reviewDate, linkToFullReview):
        self.name = name
        self.publication = publication
        self.isTopCritic = isTopCritic
        self.ratedFresh = ratedFresh
        self.reviewDescription = reviewDescription
        self.originalScore = originalScore
        self.reviewDate = reviewDate
        self.linkToFullReview = linkToFullReview

    def getCriticName(self):
        return self.name

    def getFreshRating(self):
        return self.ratedFresh

    def getFullReview(self):
        fullReview = (self.name + "\t" + self.publication
        + "\nTop Critic: " + str(self.isTopCritic) 
        + "\nFresh: " + str(self.ratedFresh) 
        + "\n" + self.reviewDescription 
        + "\n" + self.reviewDate 
        + "\nOriginal Score: " + str(self.originalScore) 
        + "\nFull Review Link: " + self.linkToFullReview)
        return fullReview

#Takes critic review data and builds an object out it. 
#That object is placed inside of an array called "criticReviews"
def buildCriticReviewObject(reviewData, isFresh, reviewLink):
    reviewData = reviewData.strip()
    reviewData = reviewData.split('\n')

    #remove empty fields, theres a lot of empty fields be default...
    while("" in reviewData): 
        reviewData.remove("")

    #get the original score
    orginalScore = ["N/A","N/A"]
    if(len(reviewData) > 10):
        reviewData[10] = reviewData[10].strip()
        orginalScore = reviewData[10].split(':')
        orginalScore[1] = orginalScore[1].strip()

    if(reviewData[0] == "Top Critic"):
        return CriticReview(reviewData[1], reviewData[2], True, isFresh, reviewData[5].strip(), orginalScore[1], reviewData[3].strip(), reviewLink)
    else:
        return CriticReview(reviewData[0], reviewData[1], False, isFresh, reviewData[4].strip(), orginalScore[1], reviewData[2].strip(), reviewLink)
