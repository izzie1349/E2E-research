# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# desired_cap = {
#  'browser': 'IE',
#  'browser_version': '8.0',
#  'os': 'Windows',
#  'os_version': '7',
#  'resolution': '1024x768'
# }
#
# driver = webdriver.Remote(
#     command_executor='http://israelalvarez1:sL9S7MhmmxZzuHGZ5kVh@hub.browserstack.com:80/wd/hub',
#     desired_capabilities=desired_cap)
#
# driver.get("http://www.google.com")
# if not "Google" in driver.title:
#     raise Exception("Unable to load google page!")
# elem = driver.find_element_by_name("q")
# elem.send_keys("BrowserStack")
# elem.submit()
# print driver.title
# driver.quit()
#
#
# ############################################
#
#
#
#
# import sys
# import unittest
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# # Edit these to match your credentials
# USERNAME = None
# BROWSERSTACK_ACCESS_KEY = None
#
# if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
#     raise Exception("Please provide your BrowserStack username and access key")
#     sys.exit(1)
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         url = "http://%s:%s@hub.browserstack.com/wd/hub" %(
#             USERNAME, BROWSERSTACK_ACCESS_KEY
#         )
#
#         self.driver = webdriver.Remote(
#             command_executor=url,
#             desired_capabilities=DesiredCapabilities.FIREFOX
#         )
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.google.com")
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("selenium")
#         elem.submit()
#         self.assertIn("Google", driver.title)
#
#     def tearDown(self):
#         self.driver.quit()
