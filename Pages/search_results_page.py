import allure

from Pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get search results page title")
    def get_search_page_title(self):
        return self.get_page_title()