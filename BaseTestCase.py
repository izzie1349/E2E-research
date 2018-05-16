from selenium import webdriver
from Constants import GE_Constants
import unittest

######### BROWSER STACK INTEGRATION #########
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



USERNAME = 'israelalvarez1'
BROWSERSTACK_ACCESS_KEY = 'sL9S7MhmmxZzuHGZ5kVh'

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)


class BaseTestCase(object):

	def setUp(self):
		url = "http://{}:{}@hub.browserstack.com/wd/hub".format(USERNAME, BROWSERSTACK_ACCESS_KEY)
		desired_cap = {
		 'browser': 'IE',
		 'browser_version': '8.0',
		 'os': 'Windows',
		 'os_version': '7',
		 'resolution': '1024x768'
		}

		self.driver = webdriver.Remote(command_executor=url,
									   desired_capabilities=desired_cap)


		# if GE_Constants['Browser'].lower() == "firefox":
		# 	self.driver = webdriver.Firefox()
		# elif GE_Constants['Browser'].lower() == "chrome":
		# 	self.driver = webdriver.Chrome()
		# elif GE_Constants['Browser'].lower() == "internet explorer":
		# 	self.driver = webdriver.Ie()
		# else:
		# 	raise Exception("unknown Browser")

	def navigate_to_page(self, url):
		self.driver.get(url)

	def tearDown(self):
		self.driver.quit()
