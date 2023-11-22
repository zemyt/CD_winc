from selenium import webdriver

# pip install selenium


def test_page_title():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:4000/")

    expected_title = "Home"
    assert driver.title == expected_title

    driver.quit()
