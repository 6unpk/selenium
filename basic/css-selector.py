from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

# chrome_option = Options()
# driver_path = '~/Downloads/chromedriver'
browser = webdriver.Chrome()

browser.get('https://likms.assembly.go.kr/bill/BillSearchSimple.do')

# Locator Strategy
# https://www.selenium.dev/documentation/webdriver/elements/locators/

# 1. Dropdown selection
age_select = browser.find_element(By.NAME, 'ageFrom')
# browser.find_element(By.CSS_SELECTOR, 'select[name=ageForm]')
age_option = age_select.find_element(By.XPATH, '//option[@value="20"]')
age_option.click()


# 일반화된 select 함수
def select_dropdown(dropdown_css_selector: str, select_css_selector: str):
    dropdown = browser.find_element(By.CSS_SELECTOR, dropdown_css_selector)
    css_selector = dropdown.find_element(By.CSS_SELECTOR, select_css_selector)
    css_selector.click()

# 2. Form Input
bill_names = browser.find_elements(By.NAME, 'billName')
bill_name = bill_names[1]
# browser.find_element(By.CSS_SELECTOR, '[]')
# browser.execute_script('arguments[0].value = "1234";', bill_names[1])
bill_name.send_keys('의안명')

# 일반화된 form 입력 함수
def input_form(form_css_selector: str, value: str):
    form = browser.find_element(By.CSS_SELECTOR, form_css_selector)
    form.send_keys(value)

input_form('input[]')