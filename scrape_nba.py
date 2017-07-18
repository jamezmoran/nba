import MySQLdb 
import urllib.request
from NBAUploader import Uploader
from Scraper import Scraper
import os
import sys
import re

if len(sys.argv) < 2:
	raise RuntimeError("Not enough arguments provided, please provide a list of years")
	
for year in sys.argv[1:]:
	if not re.match(r'^\d\d\d\d$', year):
		raise RuntimeError("Argument %s does not fit the format of a year (^\d\d\d\d$)" % year)

base_url = 'http://www.nba.com/standings/%s/team_record_comparison/conferenceNew_Std_Div.html'
scraper = Scraper()
for year in sys.argv[1:]:
	request = urllib.request.Request(base_url % year)
	response = urllib.request.urlopen(request)
	scraper.scrape_nba_html(year, str(response.read()))

dbh = MySQLdb.connect(os.environ['NBA_DB_HOST'],os.environ['NBA_DB_USER'],os.environ['NBA_DB_PASSWORD'],os.environ['NBA_DB_NAME'])
try:
	uploader = Uploader(dbh)
	uploader.upload_standings(scraper.get_standings())
finally:
	dbh.close()
