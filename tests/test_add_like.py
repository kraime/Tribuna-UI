# from pages.AuthorizationPage import Faker
import pytest
# from pages.AuthorizationPage import Faker
from pages.News_page import News_Page
import allure
from allure import step


@allure.feature('Проставление лайка на странице новости')
@allure.title('Проставление лайка на странице новости')
def test_fb_autorization(browser):
    authorization_page = News_Page(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        authorization_page.open_news_page()
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
    with step("Проставление лайка новости"):
        authorization_page.press_like_button_at_news()