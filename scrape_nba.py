import MySQLdb 
import urllib.request
from NBAUploader import Uploader
from Scraper import Scraper
import os


base_url = 'http://www.nba.com/standings/%s/team_record_comparison/conferenceNew_Std_Div.html'
scraper = Scraper()
for year in urls:
	request = urllib.request.Request(urls[year])
	response = urllib.request.urlopen(request)
	scraper.scrape_nba_html(year, str(response.read()))

dbh = MySQLdb.connect(os.environ['NBA_DB_HOST'],os.environ['NBA_DB_USER'],os.environ['NBA_DB_PASSWORD'],os.environ['NBA_DB_NAME'])
try:
	uploader = Uploader(dbh)
	uploader.upload_standings(scraper.get_standings())
finally:
	dbh.close()
