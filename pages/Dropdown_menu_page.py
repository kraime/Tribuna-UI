import logging
import time
import pytest
from allure import step
from pages.base import Base
from locators.Tribuna import TribunaPageLocators


@pytest.mark.incremental
class Dropdown_menu_page(Base):
    path = "/"

    @step
    def open_main_page(self):
        self.browser.get(self.url + self.path)
        time.sleep(5)

    @step
    def close_advertiser_fullscreen(self):
        adv_close = self._find_element(TribunaPageLocators.CLOSE_TAB)
        adv_close.click()
        time.sleep(3)

    @step
    def click_to_dropdown_menu(self):
        dropdown_menu = self._wait_element_to_be_clickable(TribunaPageLocators.DROPDOWN_MENU)
        dropdown_menu.click()
        time.sleep(3)

    @step
    def click_to_fr_language(self):
        fr_lang = self._find_elements(TribunaPageLocators.DROPDOWN_LANG_FR)
        fr_lang[1].click()
        time.sleep(3)
