class Uploader:
	def __init__(self,db):
		self.dbh = db
	
	def upload_standings(self,standings):
		with self.dbh.cursor() as cursor:
			for year, conferences in standings.items():
				for conf_name, conference in conferences.items():
					sql = "INSERT INTO Conference (name) " \
								"VALUES (%s) " \
								"ON DUPLICATE KEY UPDATE id=id"
					cursor.execute(sql, [conf_name])
					for div_name, division in conference.items():
						sql = "INSERT INTO Division (name, conference) " \
									"SELECT %s, Conference.id " \
									"FROM Conference " \
									"WHERE Conference.name=%s " \
									"ON DUPLICATE KEY UPDATE Division.id=Division.id"
						cursor.execute(sql, [div_name, conf_name])
						for team_name, stats in division.items():
							sql = "INSERT INTO Team (name, division) " \
										"SELECT %s, Division.id " \
										"FROM Division " \
										"WHERE Division.name=%s " \
										"ON DUPLICATE KEY UPDATE Team.id=Team.id "
							cursor.execute(sql, [team_name, div_name])
							sql = "INSERT INTO Standings " \
										"(`team`, `year`, `win`, `loss`, `pct`, `gb`," \
										"`conf_win`, `conf_loss`, `div_win`, `div_loss`, `home_win`," \
										"`home_loss`, `road_win`, `road_loss`, `l10_win`, `l10_loss`," \
										"`streak`) " \
										"SELECT Team.id, %s, %s, %s, %s, %s, %s, %s, %s, " \
										"%s, %s, %s, %s, %s, %s, %s, %s " \
										"FROM Team WHERE Team.name = %s " \
										"ON DUPLICATE KEY UPDATE Standings.id=Standings.id"
							cursor.execute(sql, [year, stats['wins'], stats['losses'], stats['pct'], stats['gb'],
								stats['conf_wins'], stats['conf_losses'], stats['div_wins'], stats['div_losses'],
								stats['home_wins'], stats['home_losses'], stats['road_wins'], stats['road_losses'],
								stats['l10_wins'], stats['l10_losses'], stats['streak'], team_name])
		self.dbh.commit()
