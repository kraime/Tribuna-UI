import logging
import time
import pytest
from allure import step
from pages.base import Base
from locators.Tribuna import TribunaPageLocators
from locators.Facebook import FacebookPageLocators
from utils.constants import FB_CORRECT_EMAIL, FB_CORRECT_PASS
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.incremental
class News_Page(Base):
    path = "/en/news/realmadrid-2021-12-01-vinicius-reveals-his-closest-friend-at-real-madrid/"

    @step
    def open_news_page(self):
        self.browser.get(self.url + self.path)
        time.sleep(10)
        WebDriverWait(self.browser, 10).until(
            lambda driver: self.browser.execute_script('return document.readyState') == 'complete')

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
        email_login = self._wait_element_to_be_clickable(
            FacebookPageLocators.FB_EMAIL)
        self._input_text(email_login, FB_CORRECT_EMAIL)

        pass_login = self._wait_element_to_be_clickable(
            FacebookPageLocators.FB_PASS)
        self._input_text(pass_login, FB_CORRECT_PASS)

    @step
    def click_to_fb_enter(self):
        fb_button_submit = self._wait_element_to_be_clickable(FacebookPageLocators.FB_ENTER)
        fb_button_submit.click()
        time.sleep(3)

    @step
    def check_autorization_user_name(self):
        user_name = self._find_element(TribunaPageLocators.USER_BLOCK_NAME)
        assert user_name.text == 'Pushmaster'

    @step
    def scroll_down_page(self):
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 6000)")
        time.sleep(5)

    @step
    def click_to_show_comments(self):
        comments_button = self._wait_element_to_be_clickable(TribunaPageLocators.SHOW_COMMENTS)
        comments_button.click()
        time.sleep(3)

    @step
    def input_text_comment(self):
        text_comment = self._wait_element_to_be_clickable(TribunaPageLocators.TEXT_AREA_COMMENTS)
        text_comment.clear()
        text_comment.click()
        self._input_text(text_comment, "Good news!")
        time.sleep(3)

    @step
    def send_comment(self):
        send_comment = self._find_element(TribunaPageLocators.SEND_COMMENT)
        send_comment.click()
        time.sleep(3)

    @step
    def check_comment_in_the_field(self):
        check_comment = self._find_element(TribunaPageLocators.CHECK_COMMENT)
        assert check_comment.text == 'Good news!'

    @step
    def press_like_button_at_news(self):
        like_button = self._find_element(TribunaPageLocators.LIKE_BUTTON_AT_NEWS)
        like_button.click()
        time.sleep(3)
