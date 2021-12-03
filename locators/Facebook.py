from selenium.webdriver.common.by import By


class FacebookPageLocators:
    FB_BODY = (By.ID, "content")
    FB_EMAIL = (By.ID, "email")
    FB_PASS = (By.ID, "pass")
    FB_ENTER = (By.ID, "loginbutton")
