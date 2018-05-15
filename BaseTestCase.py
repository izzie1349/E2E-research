from selenium import webdriver
from Constants import GE_Constants
import unittest

class BaseTestCase(object):

	def setUp(self):
		if GE_Constants['Browser'].lower() == "firefox":
			self.driver = webdriver.Firefox()
		elif GE_Constants['Browser'].lower() == "chrome":
			self.driver = webdriver.Chrome()
		elif GE_Constants['Browser'].lower() == "internet explorer":
			self.driver = webdriver.Ie()
		else:
			raise Exception("unknown Browser")

	def navigate_to_page(self, url):
		self.driver.get(url)

	def tearDown(self):
		self.driver.quit()
