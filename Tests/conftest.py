import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get('https://demo.nopcommerce.com/')
    yield
    # Teardown - close browser and shutdown driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def page_objects():
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)
    return {"home page": home_page, "search page": search_results_page}


@pytest.hookimpl()
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
