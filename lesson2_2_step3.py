import math
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    sum = str(int(x) + int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)
    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(10)
    browser.quit()


