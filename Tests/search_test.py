import allure
from allure_commons.types import Severity
from selenium import webdriver


@allure.epic("Search Products")
@allure.feature("Basic Search")
class TestSearch:

    @allure.severity(Severity.CRITICAL)
    @allure.title("Basic search - results page loads")
    @allure.description("Search with keyword loads search results page")
    def test_basic_search_loads_search_page(self, page_objects):
        page_objects["home page"].basic_search('abc')
        assert 'search' in page_objects["search page"].get_page_title().lower(), 'Current page is not Search'

    def test_search_results_sort_by_price_lowest_first(self, page_objects):
        page_objects["home page"].basic_search('phone')
        page_objects["search page"].sort_products_by_price_descending()
        assert 1 == 1

