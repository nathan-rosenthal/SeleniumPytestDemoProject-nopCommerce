from datetime import datetime
from time import sleep

from selenium import webdriver


# def test_docker():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.browser_version = "120.0"
#     chrome_options.set_capability(
#         "selenoid:options",
#         {
#             "enableVNC": True,
#             "enableVideo": True,
#             "videoName": f"{datetime.now()}.mp4",
#         },
#     )
#     driver = webdriver.Remote(
#         command_executor="http://localhost:4444/wd/hub", options=chrome_options
#     )
#     driver.get("https://www.google.com")
#     sleep(5)
#     print(driver.title)
#     driver.quit()