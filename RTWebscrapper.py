import requests #for making web requests
import bs4 # formatting the HTML
import json

from UserReview import UserReview
from UserReview import buildUserReviewObject
from CriticReview import CriticReview
from CriticReview import buildCriticReviewObject
from Movie import Movie
from Movie import buildMovieObject
import RTReviewAnalysis

#list of all the reviews
userReviews = []
criticReviews = []

movie = object()

#formats the users input to follow rotten tomatoes api
def formatMovieName(movieName):
    movieName = movieName.lower()
    movieName = movieName.replace(" ", "_")
    movieName = movieName.strip() #remove any leading or trailing whitespace
    return movieName


def getMovieData():
    global movie #ensure that python knows that movie is a gobal object
    movieUserWantsToFind = input("Enter movie name followed by the year it came out: ")
    print() #space
    RTFormattedMovieTitle = formatMovieName(movieUserWantsToFind)

    res = requests.get('https://www.rottentomatoes.com/m/' + RTFormattedMovieTitle) #makes a get request to RT, holds the HTML
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # soup.find("ul", {"class": "info"}).findChildren()[3].findChildren()[1].text.split(',')
    pageMovieTitle = soup.select("h1")
   
    #check to see if the movie was found/exists
    if(pageMovieTitle[0].getText() == "404 - Not Found"):
        print(movieUserWantsToFind + " was not found...make sure that you entered the correct name and release date for the movie")
        getMovieData()
    else:
        print("The movie " + pageMovieTitle[0].getText().strip() + " was found!")
        # print(soup.find("ul", {"class": "info"}).findChildren()[30])
        #Build Movie Object
        movie = buildMovieObject(soup.select("h1"),                                                   #movie title
        soup.find("div", {"class": "movie_synopsis clamp clamp-6 js-clamp"}).text.strip(),            #Synopsis
        soup.find(id="tomato_meter_link").findChildren()[1].text.strip(),                             #Tomatometer
        soup.find(href="#audience_reviews").findChildren()[1].text.strip(),                           #audienceScore
        soup.find("small", {"class": "mop-ratings-wrap__text--small"}).text.strip(),                  #totalCriticReviews
        soup.find("div", {"class": "audience-score"}).findChildren()[6].text.split(':')[1].strip(),   #totalAudienceReviews
        soup.find("ul", {"class": "info"}).findChildren()[2].text.strip(),                            #rating
        soup.find("ul", {"class": "info"}).findChildren()[2].text.strip(),                           #runtime 28
        soup.find("ul", {"class": "info"}).findChildren()[20].text.strip(),                           #releasedate
        soup.find("ul", {"class": "info"}).findChildren()[12].text.strip(),                           #director
        soup.find("ul", {"class": "info"}).findChildren()[15].text.strip(),                           #writer
        soup.find("ul", {"class": "info"}).findChildren()[3].findChildren()[1].text.split(','),       #genre
        #soup.find("ul", {"class": "info"}).findChildren()[32].text.strip())                          #studio
        "N/A")
        # print(movie.getTomatometerRating())
        #get the reviews
        getUserReviewsForMovie(RTFormattedMovieTitle)
        getCriticReviewsForMovie(RTFormattedMovieTitle, str(1))

def getCriticReviewsForMovie(movieTitle , pageNumber):
    print("Review collection in progess: " + str(len(criticReviews)) + " scraped")
    url = 'https://www.rottentomatoes.com/m/' + movieTitle + '/reviews?type=&sort=&page=' + pageNumber
    res = requests.get(url) #makes a get request to RT, holds the HTML
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    rawReviews = soup.findAll("div", {"class": "row review_table_row"}) #gets all the reviews

    #scrap data from review and build object
    for review in rawReviews: 
        #get fresh rating
        isFresh = False
        if review.find('div',{'class':'review_icon icon small fresh'}):
            isFresh = True
        #get reivew link
        reviewLink = ""
        reviewLinkData = review.find('div',{'class':'small subtle review-link'}).findChildren()
        if(reviewLinkData):
            reviewLink = reviewLinkData[0]['href']
        #build object
        criticReviews.append(buildCriticReviewObject(review.text, isFresh, reviewLink))


    #find the number of review pages there are
    if(soup.find("span", {"class": "pageInfo"})):
        # print(reviewPageData.text)
        reviewPageData = soup.find("span", {"class": "pageInfo"}).text.split(' ')
        currentPage = reviewPageData[1]
        totalPages = reviewPageData[3]
        print("Page " + currentPage + " of " + totalPages)

        #go to next page
        if(int(currentPage) < int(totalPages)):
            nextPage = int(currentPage) + 1
            getCriticReviewsForMovie(movieTitle, str(nextPage))
        else:
            print("Review collection done: " + str(len(criticReviews)) + " scraped")

#Gets all the submitted user reviews for movie
def getUserReviewsForMovie(movieTitle):
    url = 'https://www.rottentomatoes.com/m/' + movieTitle + '/reviews?type=user'
    res = requests.get(url) #makes a get request to RT, holds the HTML


    soup = bs4.BeautifulSoup(res.text, 'lxml')
    rawReviews = soup.findAll("li", {"class": "audience-reviews__item"}) #gets all the reviews

    #get all the reviews on the page
    for review in rawReviews:
        stars = []
        for starData in review.find('span',{'class':'star-display'}).findChildren():
            stars.append(starData['class'])
        userReviews.append(buildUserReviewObject(review.text, stars))

    #go to next page
    # driver = webdriver.Safari()
    # driver.get(url)
    # driver.find_element_by_css_selector('js-prev-next-paging-next btn prev-next-paging__button prev-next-paging__button-right').click()
    # time.sleep(3)
    # html = driver.page_source.encode('utf-8')
    # newSoup = bs4.BeautifulSoup(html)
    # print(newSoup)
       
    
def main():
    getMovieData()
    # for review in userReviews:
    #     print()
    #     print(review.getFullReview())
    print()
    print("############### USER REVIEW ANALYSIS ###############")
    print("Total Scrape Audience Reviews: " + str(len(userReviews)))
    print("Average User Score: " + str(RTReviewAnalysis.getUserReviewScoreAvg(userReviews)))
    print("Scrape Audience Score: " + str(RTReviewAnalysis.getUserReviewScorePercent(userReviews)) + "%")
    print("------------------------------------------------------")
    print("Total RT Audience Reviews: " + str(movie.getTotalAudienceReviews()))
    print("RT Audience Score: " + str(movie.getAudienceScore()))
 

    # for review in criticReviews:
    #     print()
    #     print(review.getFullReview())

    # print()
    # print(criticReviews[50].getFullReview())

    print()
    print("############### CRITIC REVIEW ANALYSIS ###############")
    print("Scrape reviews: " + str(len(criticReviews)))
    print("Scraped Critic Approval Rating: " + str(RTReviewAnalysis.getCriticFreshRatingPercent(criticReviews)) + "%")
    print("------------------------------------------------------")
    print("Total RT Critic Reviews: " + str())
    print("RT Critic Approval Rating: " + str(movie.getTomatometerRating()))

    print()

#run program
main()

