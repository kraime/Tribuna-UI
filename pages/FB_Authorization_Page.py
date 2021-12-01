import logging
import time
from allure import step
from pages.base import Base
from locators.Tribuna import TribunaPageLocators
from locators.Facebook import FacebookPageLocators
from utils.constants import FB_CORRECT_EMAIL, FB_CORRECT_PASS
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import TimeoutException

class FB_Authorization_Page(Base):
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
    def click_to_fb_button(self):
        fb_button = self._find_element(TribunaPageLocators.FB_BUTTON)
        fb_button.click()
        time.sleep(3)

    @step
    def switch_to_fb_window(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    @step
    def switch_to_tribuna_body(self):
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(3)

    @step
    def fill_fb_credentionals(self):
        email_login = self._wait_element_to_be_clickable(FacebookPageLocators.FB_EMAIL)
        self._input_text(email_login, FB_CORRECT_EMAIL)

        pass_login = self._wait_element_to_be_clickable(FacebookPageLocators.FB_PASS)
        self._input_text(pass_login, FB_CORRECT_PASS)

    @step
    def click_to_fb_enter(self):
        fb_button_submit = self._wait_element_to_be_clickable(FacebookPageLocators.FB_ENTER)
        fb_button_submit.click()
        time.sleep(3)

    @step
    def check_autorization_user_name(self):
        user_name = self._find_element(TribunaPageLocators.USER_BLOCK_NAME)
        assert user_name.text == 'PushmasteR'




