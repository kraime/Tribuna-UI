import pytest
#from pages.AuthorizationPage import Faker
from pages.FB_Authorization_Page import FB_Authorization_Page
import allure
from allure import step


@allure.feature('Авторизация с помощью Facebook на Главной странице')
@allure.title('Авторизация с помощью Facebook на Главной странице')
def test_fb_autorization(browser):
    authorization_page = FB_Authorization_Page(browser)
    authorization_page.open_authorization_page()
    authorization_page.close_advertiser_fullscreen()
    authorization_page.click_to_auth_block()
    authorization_page.click_to_fb_button()
    authorization_page.switch_to_fb_window()
    authorization_page.fill_fb_credentionals()
    authorization_page.click_to_fb_enter()
    authorization_page.switch_to_tribuna_body()
    authorization_page.check_autorization_user_name()
