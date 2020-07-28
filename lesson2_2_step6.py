from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try: 
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector('#input_value');
    x_value = int(x_element.text)
    y = str(calc(x_value))
    input = browser.find_element_by_css_selector('#answer');
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox');
    checkbox.click()
    
    radiobutton = browser.find_element_by_css_selector("#robotsRule");
    radiobutton.click()
    
    radiobutton.click()

    # Отправляем заполненную форму

    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()