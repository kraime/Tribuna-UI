import pytest
# from pages.AuthorizationPage import Faker
from pages.News_page import News_Page
import allure
from allure import step


@allure.feature('Открытие новостной страницы Трибуны')
@allure.title('Добавление комментария на страницу новости')
def test_add_comment_on_news_page(browser):
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
    with step("Происходит проверка авторизационного юзера через Facebook"):
        tribuna_page.check_autorization_user_name()
    with step("Происходит scroll новостной страницы до блока комментариев"):
        tribuna_page.scroll_down_page()
    with step("Происходит закрытие catfish баннера"):
        tribuna_page.close_catfish_banner()
    with step("Происходит клик по кнопке Показать комментарии"):
        tribuna_page.click_to_show_comments()
    with step("Scroll ниже еще"):
        tribuna_page.scroll_down_page_more()
    with step("Происходит ввод комментария в текстовое поле"):
        tribuna_page.input_text_comment()
    with step("Происходит отправка комментария"):
        tribuna_page.send_comment()
    with step("Происходит проверка отправленного комментария на новостной странице"):
        tribuna_page.check_comment_in_the_field()
    with step("Происходит клик по Опциям постов"):
        tribuna_page.click_to_user_posts_options()
    with step("Осуществляется выборка опции удаления комментария"):
        tribuna_page.choose_delete_option()
    with step("Происходит подтверждение удаления комментария в поп ап окне"):
        tribuna_page.confirm_alert_delete_post()
