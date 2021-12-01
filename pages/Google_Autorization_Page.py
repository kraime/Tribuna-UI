import logging
import time
import pytest
from allure import step
from pages.base import Base
from locators.Tribuna import TribunaPageLocators
from locators.Google import GooglePageLocators
from utils.constants import GMAIL_CORRECT_EMAIL, GMAIL_CORRECT_PASS


@pytest.mark.incremental
class Gmail_Authorization_Page(Base):
    path = "/"

    @step
    def open_authorization_page(self):
        self.browser.get(self.url + self.path)
        time.sleep(10)
        # WebDriverWait(self.browser, 10).until(
        #     lambda driver: self.browser.execute_script('return document.readyState') == 'complete')

    @step
    def close_advertiser_fullscreen(self):
        adv_close = self._find_element(TribunaPageLocators.CLOSE_TAB)
        adv_close.click()
        time.sleep(3)

    @step
    def click_to_auth_block(self):
        auth_block = self._wait_element_to_be_clickable(TribunaPageLocators.AUTH_BLOCK)
        auth_block.click()
        time.sleep(3)

    @step
    def click_to_gmail_button(self):
        gmail_button = self._find_element(TribunaPageLocators.GMAIL_BUTTON)
        gmail_button.click()
        time.sleep(3)

    @step
    def switch_to_gmail_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    @step
    def switch_to_tribuna_body(self):
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(3)

    @step
    def fill_gmail_login(self):
        gmail_login = self._wait_element_to_be_clickable(GooglePageLocators.GMAIL_LOGIN)
        self._input_text(gmail_login, GMAIL_CORRECT_EMAIL)

    @step
    def fill_gmail_pass(self):
        gmail_pass = self._wait_element_to_be_clickable(GooglePageLocators.GMAIL_PASSWORD)
        self._input_text(gmail_pass, GMAIL_CORRECT_PASS)

    @step
    def click_to_gmail_next_button(self):
        gmail_next_button = self._wait_element_to_be_clickable(GooglePageLocators.GMAIL_LOGIN_NEXT_BUTTON)
        gmail_next_button.click()
        time.sleep(3)

    @step
    def click_to_gmail_pass_next_button(self):
        gmail_pass_next_but = self._wait_element_to_be_clickable(GooglePageLocators.GMAIL_PASSWORD_NEXT_BUTTON)
        gmail_pass_next_but.click()
        time.sleep(3)

    @step
    def check_autorization_gmail_user_name(self):
        gmail_user_name = self._find_element(TribunaPageLocators.USER_BLOCK_NAME)
        assert gmail_user_name.text == 'Test Tribuna'
