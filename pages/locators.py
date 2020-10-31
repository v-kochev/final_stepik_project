from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")

    URL_PARAMETER = "login"

    