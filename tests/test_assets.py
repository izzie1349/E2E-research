from Constants import GE_Constants
from BaseTestCase import BaseTestCase
from pages.LibraryPage import LibraryPage
from pages.BasePage import BasePage
import unittest
import time


'''
DONE: Select an asset
Star rate an asset
DONE: rate asset (approve, select,kill,alt)
flag an asset
select multiple assets
DONE: unselect assets
'''

class TestAssets(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(TestAssets, self).setUp()
        self.navigate_to_page(GE_Constants['Base_URL'])

    # assets
    def test_select_first_asset(self):
        library_page = LibraryPage(self.driver)
        library_page.select_asset()

    def test_unselect_first_asset(self):
        library_page = LibraryPage(self.driver)
        library_page.select_asset()
        library_page.unselect_asset()

    # status labels
    def test_unselect(self):
        '''
        unselect a Select Status Label
        '''
        library_page = LibraryPage(self.driver)
        library_page.unselect_select_status_label()

    def test_select_alt(self):
        '''
        select a ALT Status Label
        '''
        library_page = LibraryPage(self.driver)
        library_page.select_alt_status_label()

    def test_select_approve(self):
        '''
        select a APPROVE Status Label
        '''
        library_page = LibraryPage(self.driver)
        library_page.select_approve_status_label()

    def test_unselect_kill(self):
        '''
        unselect a KILL Status Label
        '''
        library_page = LibraryPage(self.driver)
        library_page.unselect_kill_status_label()




    def tearDown(self):
        super(TestAssets, self).tearDown()

if __name__ == "__main__":
   unittest.main()
