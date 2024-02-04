from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text

    sum = int(num1) + int(num2)
    sum = str(sum)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(sum)


finally:
    sleep(10)
    browser.quit()