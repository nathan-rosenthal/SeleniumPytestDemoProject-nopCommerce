import time

import allure
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class SearchResultsPage(BasePage):

    SEARCH_KEYWORD_INPUT = (By.CSS_SELECTOR, 'search-text')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.search-button')
    ADVANCED_SEARCH_CHECKBOX = (By.CSS_SELECTOR, '.form-fields #advs')
    CATEGORY_DROPDOWN_LIST = (By.CSS_SELECTOR, '.form-fields #cid')
    AUTOMATICALLY_SEARCH_SUB_CATEGORIES_CHECKBOX = (By.CSS_SELECTOR, '.form-fields #isc')
    MANUFACTURER_DROPDOWN_LIST = (By.CSS_SELECTOR, '.form-fields #mid')
    SEARCH_IN_PRODUCT_DESCRIPTIONS_CHECKBOX = (By.CSS_SELECTOR, '.form-fields #sid')
    PRODUCT_CLICKABLE_TITLE = (By.CSS_SELECTOR, '.product-title')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price')
    PRODUCT_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.product-box-add-to-cart-button')
    PRODUCT_ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, '.add-to-compare-list-button')
    PRODUCT_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, '.add-to-wishlist-button')
    SORT_BY_DROPDOWN = (By.CSS_SELECTOR, '.product-selectors #products-orderby')
    DISPLAY_RESULTS_PER_PAGE_DROPDOWN = (By.CSS_SELECTOR, '.product-selectors .product-page-size')


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get search results page title")
    def get_search_page_title(self):
        return self.get_page_title()

    @allure.step("Sort products by price: descending order")
    def sort_products_by_price_descending(self):
        self.select_from_dropdown_by_value(self.SORT_BY_DROPDOWN, '10')
        time.sleep(3)

    @allure.step("validate correct ordering of products by price - lowest first")
    def validate_correct_ordering_by_price_low_high(self):
        pass
