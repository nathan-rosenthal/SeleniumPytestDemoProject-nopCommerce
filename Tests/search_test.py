import allure
from allure_commons.types import Severity
from selenium import webdriver

from Pages.home_page import HomePage


@allure.epic("Search Products")
@allure.feature("Basic Search")
class TestSearch:

    @allure.severity(Severity.CRITICAL)
    @allure.title("Basic search")
    @allure.title("Search with keyword loads Search results page")
    def test_basic_search_loads_search_page(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://demo.nopcommerce.com/')
        homePage = HomePage(driver)
        homePage.basic_search("abc")
        assert 'search' in homePage.get_search_page_title().lower(), 'Current page is not Search'
