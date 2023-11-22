from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_page_title():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("http://127.0.0.1:4000/")

    expected_title = "Home"
    assert driver.title == expected_title

    driver.quit()
