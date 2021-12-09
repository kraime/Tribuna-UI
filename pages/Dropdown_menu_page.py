import logging
import time
import pytest
from allure import step
from pages.base import Base
from locators.Tribuna import TribunaPageLocators


@pytest.mark.incremental
class DropdownMenuPage(Base):
    path = "/"

    @step
    def open_main_page(self):
        self.browser.get(self.url + self.path)
        time.sleep(3)

    @step
    def close_advertiser_fullscreen(self):
        adv_close = self._find_element(TribunaPageLocators.CLOSE_TAB)
        adv_close.click()

    @step
    def click_to_dropdown_menu(self):
        dropdown_menu = self._wait_element_to_be_clickable(TribunaPageLocators.DROPDOWN_MENU)
        dropdown_menu.click()
        time.sleep(3)

    @step
    def click_to_fr_language(self):
        fr_lang = self._find_elements(TribunaPageLocators.DROPDOWN_LANG)
        fr_lang[1].click()

    @step
    def click_to_de_language(self):
        de_lang = self._find_elements(TribunaPageLocators.DROPDOWN_LANG)
        de_lang[2].click()

    @step
    def click_to_it_language(self):
        it_lang = self._find_elements(TribunaPageLocators.DROPDOWN_LANG)
        it_lang[3].click()

    @step
    def click_to_es_language(self):
        es_lang = self._find_elements(TribunaPageLocators.DROPDOWN_LANG)
        es_lang[4].click()

    @step
    def click_to_ar_language(self):
        ar_lang = self._find_elements(TribunaPageLocators.DROPDOWN_LANG)
        ar_lang[5].click()

