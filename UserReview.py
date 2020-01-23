#An object containing data for a single user review 
class UserReview:
    def __init__(self, firstname, middlename, lastname, reviewDescription, score, reviewDate):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.reviewDescription = reviewDescription
        self.score = score
        self.reviewDate = reviewDate

    def getFirstname(self):
        return self.firstname

    def getScore(self):
        return self.score

    def getFullReview(self):
        fullReview = self.firstname + " " + self.middlename + " " + self.lastname + "\tScore: " + str(self.score) + "\n" + self.reviewDescription + "\n" + self.reviewDate + "\n"
        return fullReview

#Takes user review data and builds an object out it. 
#That object is placed inside of an array called "userReviews"
def buildUserReviewObject(reviewData, stars):
    reviewData = reviewData.strip()
    reviewData = reviewData.split('\n')

    #remove empty fields, theres a lot of empty fields be default...
    while("" in reviewData) : 
        reviewData.remove("")

    score = 0
    #convert stars into decimal value
    for star in stars:
        #the star object itself is actually an array
        if star[0] == 'star-display__filled':
            score += 1
        elif star[0] == 'star-display__half':
            score += 0.5
        

    firstname = "No Name"
    middlename = ""
    lastname = ""

    #Detect if the review has a user name
    if reviewData[1] == "                            ":
        nameComponents = reviewData[0].split(' ')
        #get all name components
        if(len(nameComponents) == 3):
            firstname = nameComponents[0]
            middlename = nameComponents[1]
            lastname = nameComponents[2]
        elif(len(nameComponents) == 2):
            firstname = nameComponents[0]
            lastname = nameComponents[1]
        else:
            firstname = nameComponents[0]
  
        return UserReview(firstname, middlename, lastname, reviewData[3], score, reviewData[2])
    else: 
        #the reviewer does not have a username
        return UserReview(firstname, middlename, lastname, reviewData[1], score, reviewData[0])
        
