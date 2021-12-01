import pytest
# from pages.AuthorizationPage import Faker
from pages.FB_Authorization_Page import FB_Authorization_Page
import allure
from allure import step


@allure.feature('Авторизация с помощью Facebook на Главной странице')
@allure.title('Авторизация с помощью Facebook на Главной странице')
def test_fb_autorization(browser):
    authorization_page = FB_Authorization_Page(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        authorization_page.open_authorization_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        authorization_page.close_advertiser_fullscreen()
    with step("Производится клик по блоку авторизации в хеддере"):
        authorization_page.click_to_auth_block()
    with step("Производится клик по кнопке авторизации через Facebook"):
        authorization_page.click_to_fb_button()
    with step("Происходит переключение на окно авторизации Facebook"):
        authorization_page.switch_to_fb_window()
    with step("Происходит заполнение данных авторизации Facebook"):
        authorization_page.fill_fb_credentionals()
    with step("Клик по кнопке Вход Facebook"):
        authorization_page.click_to_fb_enter()
    with step("Происходит переключение на окно Tribuna.com"):
        authorization_page.switch_to_tribuna_body()
    with step("Происходит проверка авторизационного юзера через Facebook"):
        authorization_page.check_autorization_user_name()
