#This a simple python app to fetch book reviews using the New York Times API.

import requests
import logging
from config import Settings


# Configure the logger
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

print("Please enter author name: ")
entered_input = input()
author = entered_input.replace(" ", "+")
API_KEY = Settings.API_KEY


# Fetch reviews
def fetch_reviews():
    URL = "https://api.nytimes.com/svc/books/v3/reviews.json?author=" + author + "&api-key=" + API_KEY
    response = requests.get(url=URL)
    data = response.json()

    # Log the start of the function
    logging.info('Starting fetch_reviews function')

    print("\nREVIEWS FOR " + entered_input.upper())
    for i in data['results']:
        publication_date = i['publication_dt']
        summary = i['summary']
        book_title = i['book_title']

        # Log each review
        logging.info(f'Book Title: {book_title}, Book Summary: {summary}, Publication Date: {publication_date}')

        # Print results
        print("\n------------------------")
        print("Book Title: " + book_title + "\n")
        print("Book Summary: " + summary + "\n")
        print("Publication Date: " + publication_date)

    # Log the end of the function
    logging.info('Ending fetch_reviews function')


fetch_reviews()
