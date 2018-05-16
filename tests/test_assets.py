from Constants import GE_Constants
from BaseTestCase import BaseTestCase
from pages.LibraryPage import LibraryPage
from pages.BasePage import BasePage
import unittest
import time
import nose
from nose.plugins.attrib import attr


class TestAssets(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(TestAssets, self).setUp()
        self.navigate_to_page(GE_Constants['Base_URL'])

    def test_select_first_asset(self):
        '''
        select first asset
        '''
        library_page = LibraryPage(self.driver)
        library_page.select_asset()

    def test_unselect_first_asset(self):
        '''
        unselect first asset
        '''
        library_page = LibraryPage(self.driver)
        library_page.select_asset()
        library_page.unselect_asset()

    @attr(priority='smoke')
    def test_select_multiple_assets(self):
        '''
        select the first 5 assets
        '''
        library_page = LibraryPage(self.driver)
        library_page.select_asset()
        library_page.select_second_asset()
        library_page.select_third_to_fifth_asset()

    @attr(priority='smoke')
    def test_unselect(self):
        '''
        unselect a Select Status Label
        '''
        library_page = LibraryPage(self.driver)
        library_page.unselect_select_status_label()

    @attr(priority='high')
    def test_select_alt(self):
        '''
        select a ALT Status Label
        '''
        library_page = LibraryPage(self.driver)
        library_page.select_alt_status_label()

    @attr(priority='high')
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
   nose.main()
