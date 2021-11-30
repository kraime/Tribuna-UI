from selenium.webdriver.common.by import By


class GooglePageLocators:
    GMAIL_LOGIN = (By.ID, "identifierId")
    GMAIL_LOGIN_NEXT_BUTTON = (By.ID, "identifierNext")
    GMAIL_PASSWORD = (By.CSS_SELECTOR, "input[type=password")
    GMAIL_PASSWORD_NEXT_BUTTON = (By.ID, "passwordNext")