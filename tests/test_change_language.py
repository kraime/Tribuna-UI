import pytest
from pages.Dropdown_menu_page import DropdownMenuPage
import allure
from allure import step


@allure.feature('Переключение языков на сайте Tribuna.com')
@allure.title('Смена языка на французский')
def test_change_language_to_fr(browser):
    tribuna_page = DropdownMenuPage(browser)
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

@allure.title('Смена языка на немецкий')
def test_change_language_to_de(browser):
    tribuna_page = DropdownMenuPage(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        tribuna_page.open_main_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит клик на выпадающее меню с выбором языка"):
        tribuna_page.click_to_dropdown_menu()
    with step("Происходит выбор немецкого языка на сайте"):
        tribuna_page.click_to_de_language()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит сравнение урла после переключения на немецкий язык"):
        current_url = browser.current_url
        assert current_url == 'https://tribuna.com/de/'

@allure.title('Смена языка на итальянский')
def test_change_language_to_it(browser):
    tribuna_page = DropdownMenuPage(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        tribuna_page.open_main_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит клик на выпадающее меню с выбором языка"):
        tribuna_page.click_to_dropdown_menu()
    with step("Происходит выбор итальянского языка на сайте"):
        tribuna_page.click_to_it_language()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит сравнение урла после переключения на итальянский язык"):
        current_url = browser.current_url
        assert current_url == 'https://tribuna.com/it/'

@allure.title('Смена языка на испанский')
def test_change_language_to_es(browser):
    tribuna_page = DropdownMenuPage(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        tribuna_page.open_main_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит клик на выпадающее меню с выбором языка"):
        tribuna_page.click_to_dropdown_menu()
    with step("Происходит выбор испанского языка на сайте"):
        tribuna_page.click_to_es_language()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит сравнение урла после переключения на испанский язык"):
        current_url = browser.current_url
        assert current_url == 'https://tribuna.com/es/'

@allure.title('Смена языка на арабский')
def test_change_language_to_ar(browser):
    tribuna_page = DropdownMenuPage(browser)
    with step("Открывает Главную страницу Tribuna.com"):
        tribuna_page.open_main_page()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит клик на выпадающее меню с выбором языка"):
        tribuna_page.click_to_dropdown_menu()
    with step("Происходит выбор арабского языка на сайте"):
        tribuna_page.click_to_ar_language()
    with step("Закрывает рекламный баннер на Главной странице"):
        tribuna_page.close_advertiser_fullscreen()
    with step("Происходит сравнение урла после переключения на арабский язык"):
        current_url = browser.current_url
        assert current_url == 'https://tribuna.com/ar/'