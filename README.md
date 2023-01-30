# Cosmetic Spider
## Introduction
This is a Scrapy Spider implemented in Python to scrape information about cosmetic stores from the website `goschonheit.ch`. The scraper is designed to extract information related to cosmetic stores available on the website.

This project is also implemeted in Single File on Google Colab. 

## Functionality
* The Spider starts by making a request to the main page of the website, `http://goschonheit.ch/`.
* It then retrieves a list of cities from the page and makes subsequent requests to each city page to gather information about the cosmetic stores in that city.
* The Spider follows the next pages of each city until there are no more pages to follow.

## Information Extracted
The information collected by the scraper includes:

* Name of the store
* Rating of the store
* Address of the store
* Phone number of the store
* Website of the store
* City in which the store is located

## Output
The extracted information is stored in a JSON file named cosmetic_stores.json.

## Pagination
The scraper is designed to follow the website's pagination, and extract information from each page until all the pages are exhausted.

## Custom Settings
Custom settings are also defined in the code to control the behavior of the scraper. These settings include:

* The number of concurrent requests to make to the website.
* A delay between each download.
* A custom user agent to identify the Spider when making requests.
* The logging level for the Spider's log file.
* The format and URI for the file where the collected data will be saved.
* Enable or disable auto-throttling of requests, with a start delay and maximum delay specified.

By using these custom settings, the scraper can be easily adjusted to suit the requirements of the user.

