import MySQLdb 
import urllib.request
from NBAUploader import Uploader
from Scraper import Scraper
import os

urls = {
	'2014' : 'http://www.nba.com/standings/2014/team_record_comparison/conferenceNew_Std_Div.html',
	'2013' : 'http://www.nba.com/standings/2013/team_record_comparison/conferenceNew_Std_Div.html',
	'2012' : 'http://www.nba.com/standings/2012/team_record_comparison/conferenceNew_Std_Div.html'
}

scraper = Scraper()
for year in urls:
	request = urllib.request.Request(urls[year])
	response = urllib.request.urlopen(request)
	scraper.scrape_nba_html(year, str(response.read()))

dbh = MySQLdb.connect(os.environ['NBA_DB_HOST'],os.environ['NBA_DB_USER'],os.environ['NBA_DB_PASSWORD'],os.environ['NBA_DB_NAME'])
try:
	uploader = Uploader(dbh)
	uploader.upload_standings(scraper.get_standings(), '2014')
finally:
	dbh.close()
