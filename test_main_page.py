#запускаем командой pytest -v --tb=line --language=en test_main_page.py
#опция "--tb=line" указывает, что нужно выводить только одну строку из лога каждого упавшего теста
from pages.main_page import MainPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
