import os
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage


# @pytest.fixture(scope="class", autouse=True)
# def setup(request):
#     global driver
#     options = Options()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options)
#     request.cls.driver = driver
#     driver.maximize_window()
#     driver.get('https://demo.nopcommerce.com/')
#     yield
#     # Teardown - close browser and shutdown driver
#     driver.quit()


@pytest.fixture(scope="class", autouse=True)
def setup_v2(request):
    global driver
    # Configure remote webdriver - selenoid
    chrome_options = webdriver.ChromeOptions()
    chrome_options.browser_version = "120.0"
    chrome_options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableLog": True,
            "enableVideo": True,
            "videoName": f"{datetime.now()}.mp4",
        },
    )
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub", options=chrome_options
    )
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
    return {"home page": home_page,
            "search page": search_results_page}


@pytest.hookimpl()
def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl()
def pytest_sessionfinish() -> None:
    environment_properties = {
        'browser': driver.name,
        'browser_version': driver.capabilities['browserVersion'],
        'platform_name': driver.capabilities['platformName']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)
