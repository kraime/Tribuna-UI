from selenium.webdriver.common.by import By


class TribunaPageLocators:
    CLOSE_TAB = (By.CLASS_NAME, "desktop-fullscreen__close-btn")
    AUTH_BLOCK = (By.CLASS_NAME, "auth-block__not-loged")
    FB_BUTTON = (By.CLASS_NAME, "auth-popup__btn--fb")
    GMAIL_BUTTON = (By.CLASS_NAME, "auth-popup__btn--g")
    USER_BLOCK_NAME = (By.CLASS_NAME, "auth-block__username")
    SHOW_COMMENTS = (By.CLASS_NAME, "one-news__comments")
    TEXT_AREA_COMMENTS = (By.CLASS_NAME, "comments-form__textarea")
    SEND_COMMENT = (By.CLASS_NAME, "comments-form__btn")
    CHECK_COMMENT = (By.CLASS_NAME, "comments__text")
    LIKE_BUTTON_AT_NEWS = (By.CLASS_NAME, "user-post-footer__thumb-up")
    CLOSE_CATFISH = (By.CLASS_NAME, "banner__annotation--icon")
    USER_POST_OPTIONS = (By.CLASS_NAME, "user-post-header__options")
    USER_DELETE_POST_OPTION = (By.CLASS_NAME, "header-options-menu__option")
    DELETE_BUTTON = (By.CLASS_NAME, "SOME_CLASS_BUTTON")

