from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

# chrome_option = Options()
# driver_path = '~/Downloads/chromedriver'
browser = webdriver.Chrome()

browser.get('https://www.nesdc.go.kr/portal/bbs/B0000005/list.do?menuNo=200467')

# Locator Strategy
# https://www.selenium.dev/documentation/webdriver/elements/locators/

# 1. Dropdown selection
search_time = browser.find_element(By.ID, 'searchTime')
# browser.find_element(By.CSS_SELECTOR, 'select[name=ageForm]')
date_option = search_time.find_element(By.XPATH, '//option[@value="1"]')
date_option.click()


# 2. Form Input
search_word = browser.find_element(By.ID, 'searchWrd')
# browser.find_element(By.CSS_SELECTOR, '[]')
search_word.send_keys('키워드')


# 일반화된 form 입력 함수
def input_form(form_css_selector: str, value: str):
    form = browser.find_element(By.CSS_SELECTOR, form_css_selector)
    form.send_keys(value)
