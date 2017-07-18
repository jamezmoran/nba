# NBA Standings Scraper

This project scrapes a given list of URLs from the NBA website and pushes the standings into a MySQL database. 

Setup Instructions
============
This project requires that python3, pip, and virtualenv be installed. Below are instructions on how to install the dependencies for this library:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Default usage
=============

To use the default `scrape_nba.py` script, you must define the login details of the MySQL datastore. These should be set by exporting the following environment variables:

```
$ export NBA_DB_HOST=<Hostname of the MySQL DB> 
$ export NBA_DB_USER=<your MySQL username>
$ export NBA_DB_PASSWORD=<your MySQL password
$ export NBA_DB_NAME=<Name of the MySQL DB>
```

To scrape from individual NBA pages using the default script, you must provide a list of years on the command line to the `scrape_nba.py`, for example:

```
$ scrape_nba.py 2012 2013 2014
```

This will pull data from each of the years 2012, 2013, and 2014, and then push the scraped data into the MySQL database given by the` NBA_DB` environement variables.

Library usage
=============
Contained are two classes, `Scraper` and `Uploader`. With the `Scraper.scrape_nba_html` module you can pass in HTML pulled from the NBA standings website. 
Below is a basic example of how you would use these classes in your own code:

```py
from NBAUploader import Uploader
from Scraper import Scraper
import MySQLdb 
import urllib.request

urls = {
	'2014' : 'http://www.nba.com/standings/2014/team_record_comparison/conferenceNew_Std_Div.html',
	'2013' : 'http://www.nba.com/standings/2013/team_record_comparison/conferenceNew_Std_Div.html',
	'2012' : 'http://www.nba.com/standings/2012/team_record_comparison/conferenceNew_Std_Div.html'
}

scraper = Scraper()
for year in urls:
	request = urllib.request.Request(urls[year])
	response = urllib.request.urlopen(request)
	# Must pass raw HTML into scraper object
	scraper.scrape_nba_html(year, str(response.read()))

# Create database handle and pass it into uploader
dbh = MySQLdb.connect('localhost', 'myuser', 'mypass', 'mydbname')
try:
	uploader = Uploader(dbh)
	uploader.upload_standings(scraper.get_standings())
finally:
	dbh.close()
```


