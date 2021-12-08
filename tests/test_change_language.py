import pytest
from pages.Dropdown_menu_page import Dropdown_menu_page
import allure
from allure import step


@allure.feature('Осуществляется смена языка на французский')
@allure.title('Осуществляется смена языка на французский')
def test_gmail_autorization(browser):
    tribuna_page = Dropdown_menu_page(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        tribuna_page.open_main_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит клик на выпадающее меню с выбором языка"):
        tribuna_page.click_to_dropdown_menu()
    with step("Происходит выбор французского языка на сайте"):
        tribuna_page.click_to_fr_language()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит сравнение урла после переключения на французский язык"):
        current_url = browser.current_url
        assert current_url == 'https://tribuna.com/fr/'
