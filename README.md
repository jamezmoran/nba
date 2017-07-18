# NBA Standings Scraper

This project scrapes a given list of URLs from the NBA website and pushes the standings into a MySQL database. 

Instructions
============
This project requires that python3, pip, and virtualenv be installed. Below are instructions on how to install the dependencies for this library:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Example usage
=============

To use the default `scrape_nba.py` script, you must define the login details of the MySQL datastore. These should be set by exporting the following environment variables:

```
$ export NBA_DB_HOST=<Hostname of the MySQL DB> 
$ export NBA_DB_USER=<your MySQL username>
$ export NBA_DB_PASSWORD=<your MySQL password
$ export NBA_DB_NAME=<Name of the MySQL DB>
```

To scrape from individual NBA pages, you must provide a list of years on the command line to the `scrape_nba.py`, for example:

```
$ scrape_nba.py 2012 2013 2014
```

This will pull data from each of the years 2012, 2013, and 2014, and then push the scraped data into the MySQL database given by the NBA_\* environement variables.


