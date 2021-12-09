# from pages.AuthorizationPage import Faker
import pytest
# from pages.AuthorizationPage import Faker
from pages.News_page import News_Page
import allure
from allure import step


@allure.feature('Проставление лайка на странице новости')
@allure.title('Проставление лайка на странице новости')
def test_fb_autorization(browser):
    tribuna_page = News_Page(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        tribuna_page.open_news_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Производится клик по блоку авторизации в хеддере"):
        tribuna_page.click_to_auth_block()
    with step("Производится клик по кнопке авторизации через Facebook"):
        tribuna_page.click_to_fb_button()
    with step("Происходит переключение на окно авторизации Facebook"):
        tribuna_page.switch_to_fb_window()
    with step("Происходит заполнение данных авторизации Facebook"):
        tribuna_page.fill_fb_credentionals()
    with step("Клик по кнопке Вход Facebook"):
        tribuna_page.click_to_fb_enter()
    with step("Происходит переключение на окно Tribuna.com"):
        tribuna_page.switch_to_tribuna_body()
    with step("Проставление лайка новости"):
        tribuna_page.press_like_button_at_news()