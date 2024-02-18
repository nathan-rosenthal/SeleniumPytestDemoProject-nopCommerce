from selenium import webdriver

from Pages.home_page import HomePage


class TestSearch:

    def test_basic_search_loads_search_page(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://demo.nopcommerce.com/')
        homePage = HomePage(driver)
        homePage.basic_search("abc")
        assert 'search' in homePage.get_search_page_title().lower(), 'Current page is not Search'
