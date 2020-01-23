# Rotten Tomatoes Web Scraper

This project is available for anyone who wants to use it to gather data on Rotten Tomatoes user and critic reviews.
This web scraper downloads all the reviews it can find for a given movie and computes the scores. Then it shows a comparison of the scores it calculated vs the scores displayed on the website.

NOTE: This project is currently a work in progress.
NOTE: Currently the program can only gather the first 10 reviews from the user scores. This issue is currently being worked on.


### Required Libraries

```
requests
bs4
lxml
```

NOTE: This project only runs on Python 3

## Getting Started

Simply run RTWebscrapper.py via Python 3 

Enter the name of a move you want to look up. If the move that you enter doesn't turn up, try entering the name of the move followed by the date the move came out. If the movie still doesn't show up but you know its listed on Rotten Tomatoes, check the URL on the movie's homepage and enter that in.

### Examples
```
alien
star wars
star wars the last jedi
star wars the rise of skywalker
terminator
the thing 2011 (Example of how sometimes you need to add the date the movie came out)
it 2017
1917 2019
1021244_thing (This is The Thing 1982, this is an example of how some movies don't follow the standard format)
```

## Authors

Sam Trent

## License

This project is licensed under the MIT License.
