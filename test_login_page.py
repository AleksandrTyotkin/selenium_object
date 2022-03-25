from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_should_login_page(browser):
    #  link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
