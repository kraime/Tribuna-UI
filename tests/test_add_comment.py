import pytest
#from pages.AuthorizationPage import Faker
from pages.News_page import News_Page
import allure
from allure import step


@allure.feature('Открытие новостной страницы Трибуны')
@allure.title('Добавление комментария на страницу новости')
def test_add_comment_on_news_page(browser):
    authorization_page = News_Page(browser)
    authorization_page.open_news_page()
    authorization_page.close_advertiser_fullscreen()
    authorization_page.click_to_auth_block()
    authorization_page.click_to_fb_button()
    authorization_page.switch_to_fb_window()
    authorization_page.fill_fb_credentionals()
    authorization_page.click_to_fb_enter()
    authorization_page.switch_to_tribuna_body()
    authorization_page.check_autorization_user_name()
    authorization_page.scroll_down_page()
    authorization_page.click_to_show_comments()
    authorization_page.input_text_comment()
    authorization_page.send_comment()
    authorization_page.check_comment_in_the_field()