from lxml import html

class Scraper:
	def __init__(self):
		self.standings = {}
	
	def scrape_nba_html(self, year, html_string):
		if year not in self.standings:
			self.standings[year] = {}
		tree = html.fromstring(html_string)
		rows = tree.xpath('//table[@class="genStatTable mainStandings"]/tr')
		teams = []
		divisions = []
		conferences = []

		current_conference = None
		current_division = None
		for row in rows:
			conference = row.xpath('td[@class="confTitle"]/text()')
			if conference:
				self.standings[year][conference[0]] = {}
				current_conference = conference[0]
				continue
			elif row.get('class') == 'title':
				division = row.xpath('td[@class="name"]/text()')
				if division:
					self.standings[year][current_conference][division[0]] = { }
					current_division = division[0]
				continue
			elif row.get('class') == 'odd' or row.get('class') == 'even': 
				[name, wins, losses, pct, gb, conf, div, home, road, l10, streak] = row.xpath('td')
				team_name = name.xpath('a/text()')[0]
				conf = conf.text.split('-')
				div = div.text.split('-')
				home = home.text.split('-')
				road = road.text.split('-')
				l10 = l10.text.split('-')
				streak = streak.text.split(' ')
				if streak[0] == 'L':
					streak = "-" + streak[1]
				else:
					streak = streak[1]
				team_dict = {
					'wins' : wins.text,
					'losses' : losses.text,
					'pct' : pct.text,
					'gb' : gb.text,
					'conf_wins' : conf[0],
					'conf_losses' : conf[1],
					'div_wins' : div[0],
					'div_losses' : div[1],
					'home_wins' : home[0],
					'home_losses' : home[1],
					'road_wins' : road[0],
					'road_losses' : road[1],
					'l10_wins' : l10[0],
					'l10_losses' : l10[1],
					'streak' : streak
				}
				self.standings[year][current_conference][current_division][team_name] = team_dict

	def get_standings(self):
		return self.standings
