import pytest
#from pages.AuthorizationPage import Faker
from pages.Google_Autorization_Page import Gmail_Authorization_Page
import allure
from allure import step


@allure.feature('Авторизация с помощью Gmail на Главной странице')
@allure.title('Авторизация с помощью Gmail на Главной странице')
def test_gmail_autorization(browser):
    authorization_page = Gmail_Authorization_Page(browser)
    authorization_page.open_authorization_page()
    authorization_page.close_advertiser_fullscreen()
    authorization_page.click_to_auth_block()
    authorization_page.click_to_gmail_button()
    authorization_page.switch_to_gmail_window()
    authorization_page.fill_gmail_login()
    authorization_page.click_to_gmail_next_button()
    authorization_page.fill_gmail_pass()
    authorization_page.click_to_gmail_pass_next_button()
    authorization_page.switch_to_tribuna_body()
    authorization_page.check_autorization_gmail_user_name()