from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Constants import LocatorMode
from BasePage import BasePage, IncorrectPageException
import time


## ----- Page Elements ----- ##

assetPanelCss = "div.asset-panel-wrapper"

# unselected
assetTileCss = "div.tile.tile-medium"
# selected
selectedAssetTileCss = "div.tile.tile-medium"



# STATUS LABELS

# unselected labels
unselectSelectStatusLabelCss = "div.status-label.status-label-select.sm.is-selected"
unselectAltStatusLabelCss = "div.status-label.status-label-alt.sm.is-selected"
unselectApproveStatusLabelCss = "div.status-label.status-label-approve.sm.is-selected"
unselectKillStatusLabelCss = "div.status-label.status-label-kill.sm.is-selected"

# selected labels
selectSelectStatusLabelCss = "div.status-label.status-label-select.sm"
selectAltStatusLabelCss = "div.status-label.status-label-alt.sm"
selectApproveStatusLabelCss = "div.status-label.status-label-approve.sm"
selectKillStatusLabelCss = "status-label.status-label-kill.sm"


class LibraryPage(BasePage):

    def __init__(self, driver):
        super(LibraryPage, self).__init__(driver)

    def _verify_page(self):
        """
        This method verifies that we are on the correct page.
        """
        try:
            self.wait_for_element_visibility(5, "cssSelector", assetPanelCss)
        except:
            raise IncorrectPageException

    def select_asset(self):
        first_asset = self.wait_until_element_clickable(5, "cssSelector", assetTileCss)
        first_asset.click()

    def unselect_asset(self):
        first_asset = self.wait_until_element_clickable(5, "cssSelector", selectedAssetTileCss)
        first_asset.click()

    def unselect_select_status_label(self):
        first_asset = self.wait_until_element_clickable(5, "cssSelector", assetTileCss)
        first_asset.click()
        select_status_label = self.wait_until_element_clickable(5, "cssSelector", unselectSelectStatusLabelCss)
        select_status_label.click()

    def select_alt_status_label(self):
        first_asset = self.wait_until_element_clickable(5, "cssSelector", assetTileCss)
        first_asset.click()
        alt_status_label = self.wait_until_element_clickable(5, "cssSelector", selectAltStatusLabelCss)
        alt_status_label.click()

    def select_approve_status_label(self):
        first_asset = self.wait_until_element_clickable(5, "cssSelector", assetTileCss)
        first_asset.click()
        approve_status_label = self.wait_until_element_clickable(5, "cssSelector", selectApproveStatusLabelCss)
        approve_status_label.click()

    def unselect_kill_status_label(self):
        first_asset = self.wait_until_element_clickable(5, "cssSelector", assetTileCss)
        first_asset.click()
        kill_status_label = self.wait_until_element_clickable(7, "cssSelector", unselectKillStatusLabelCss)
        kill_status_label.click()
