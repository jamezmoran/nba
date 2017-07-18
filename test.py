from Scraper import Scraper
import unittest
import json

class TestScraper(unittest.TestCase):
	def test_1(self):
		test_file = open("tests/test_case_1.html", "r")
		html_string = test_file.read()
		test_file.close()
		expected_output_file = open("tests/expected_output_1.json")
		expected = json.loads(expected_output_file.read())
		expected_output_file.close()

		scraper = Scraper()
		scraper.scrape_nba_html('2013',html_string)
		self.assertEqual(scraper.get_standings(), expected)

	def test_2(self):
		test_file = open("tests/test_case_2.html", "r")
		html_string = test_file.read()
		test_file.close()
		expected_output_file = open("tests/expected_output_2.json")
		expected = json.loads(expected_output_file.read())
		expected_output_file.close()

		scraper = Scraper()
		scraper.scrape_nba_html('2014',html_string)
		self.assertEqual(scraper.get_standings(), expected)
