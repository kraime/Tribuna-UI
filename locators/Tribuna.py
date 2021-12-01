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
