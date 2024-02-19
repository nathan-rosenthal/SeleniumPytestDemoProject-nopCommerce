import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class HomePage(BasePage):

    SEARCH_STORE_INPUT = (By.CSS_SELECTOR, '.search-box-text')
    SEARCH_STORE_BUTTON = (By.CSS_SELECTOR, '.search-box-button')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter a search term and click search")
    def basic_search(self, search_term):
        self.fill_text(self.SEARCH_STORE_INPUT, search_term)
        self.click(self.SEARCH_STORE_BUTTON)

