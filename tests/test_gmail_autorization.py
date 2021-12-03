import pytest
#from pages.AuthorizationPage import Faker
from pages.Google_Autorization_Page import Gmail_Authorization_Page
import allure
from allure import step


@allure.feature('Авторизация с помощью Gmail на Главной странице')
@allure.title('Авторизация с помощью Gmail на Главной странице')
def test_gmail_autorization(browser):
    authorization_page = Gmail_Authorization_Page(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        authorization_page.open_authorization_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        authorization_page.close_advertiser_fullscreen()
    with step("Производится клик по блоку авторизации в хеддере"):
        authorization_page.click_to_auth_block()
    with step("Производится клик по кнопке авторизации через Google"):
        authorization_page.click_to_gmail_button()
    with step("Происходит переключение на окно авторизации Google"):
        authorization_page.switch_to_gmail_window()
    with step("Происходит заполнение логина Google"):
        authorization_page.fill_gmail_login()
    with step("Происходит клик по кнопке Дальше"):
        authorization_page.click_to_gmail_next_button()
    with step("Происходит заполнение пароля Google"):
        authorization_page.fill_gmail_pass()
    with step("Происходит клик по кнопке Дальше"):
        authorization_page.click_to_gmail_pass_next_button()
    with step("Происходит переключение на окно Tribuna.com"):
        authorization_page.switch_to_tribuna_body()
    with step("Происходит проверка авторизационного юзера через Google"):
        authorization_page.check_autorization_gmail_user_name()