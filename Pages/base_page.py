from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def goToPage(self, url):
        self.driver.get(url)

    def get_page_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def wait_for_element(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} was not clickable within timeout")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element {locator} was not found")

    def clear_field_text(self, locator):
        try:
            self.wait_for_element(locator).clear()
        except Exception as error:
            message = f"Could not clear field text on {locator}. {error}"
            raise Exception(message)

    def fill_text(self, locator, text):
        try:
            self.clear_field_text(locator)
            self.wait_for_element(locator).send_keys(text)
        except Exception as error:
            message = f"Entering text into field {locator} failed. {error}"
            raise Exception(message)

    def get_text(self, locator):
        try:
            return self.wait_for_element(locator).text
        except Exception:
            message = f"Could not get text from element {locator}"
            raise Exception(message)

    def click(self, locator):
        try:
            self.wait_for_element(locator).click()
        except Exception:
            message = f"Clicking on element {locator} failed"
            raise Exception(message)

    ## Need to refactor
    #
    # def select_from_dropdown_by_value(self, locator, value):
    #     selector = self.driver.find_element(*locator)
    #     Select(selector).select_by_value(value)
    #
    # def click_item_from_elements_list_by_position(self, locator, item_position):
    #     time.sleep(1)
    #     list_items = self.driver.find_elements(*locator)
    #     list_items[item_position].click()
    #
    # def click_all_list_elements(self, locator):
    #     list_elements = self.driver.find_elements(*locator)
    #     for item in list_elements:
    #         item.click()
    #
    # def get_number_of_list_elements(self, locator):
    #     time.sleep(2)
    #     list_items = self.driver.find_elements(*locator)
    #     return len(list_items)
    #
    # def get_list_of_elements_text(self, locator):
    #     list_elements = self.driver.find_elements(*locator)
    #     price_list = []
    #     for element in list_elements:
    #         price_list.append(element.text)
    #     return price_list
    #
    # def is_element_displayed(self, locator):
    #     time.sleep(2)
    #     is_element_displayed = False
    #     try:
    #         is_element_displayed = self.driver.find_element(*locator).is_displayed()
    #     except Exception as error:
    #         print({error})
    #     return is_element_displayed
    #
    # def is_element_enabled(self, locator):
    #     time.sleep(2)
    #     is_element_enabled = False
    #     try:
    #         is_element_enabled = self.driver.find_element(*locator).is_enabled()
    #     except Exception as error:
    #         print({error})
    #     return is_element_enabled
    #
    # def is_element_selected(self, locator):
    #     time.sleep(2)
    #     is_element_selected = False
    #     try:
    #         is_element_selected = self.driver.find_element(*locator).is_selected()
    #     except Exception as error:
    #         print({error})
    #     return is_element_selected
