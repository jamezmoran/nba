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

To use the Uploader module, pass into the `upload_standings` the output from the `get\_standings()` method on `Scraper`, or alternatively a dict of the format:
```
{
	'<year>' : {
		'<conference name>' : {
			'<division name>' : {
				'<team name>' : {
					'wins' : <wins no.>,
					'losses' : <losses no.>,
					'pct' : <PCT stat>,
					'gb' : <GB stat>,
					'conf_wins' : <conf wins>,
					'conf_losses' : <conf losses>,
					'div_wins' : <division wins>,
					'div_losses' : <division losses>,
					'home_wins' : <home wins>,
					'home_losses' : <home losses>,
					'road_wins' : <road wins>,
					'road_losses' : <road losses>,
					'l10_wins' : <last ten wins>,
					'l10_losses' : <last ten losses>,
					'streak' : <streak>
				}
			}
		}
	}
}
```

Testing
=======
I have provided a basic test driver to test the `Scraper` module. It passes two example HTML files into the `Scraper` modules and tests the output it generates against the content of the two JSON files `expected_output_1.json` and `expected_output_2.json`. To run the test driver, run the following command:
```
$ python3 -m unittest test.py
```


