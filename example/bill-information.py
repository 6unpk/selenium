from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse
import csv

browser = webdriver.Chrome()

browser.get(f'https://likms.assembly.go.kr/bill/BillSearchSimple.do')

age_form_select = browser.find_element(By.NAME, 'ageFrom')
age_option = age_form_select.find_element(By.XPATH, '//option[@value="20"]')
age_option.click()

aget_to_select = browser.find_element(By.NAME, 'ageTo')
age_option = aget_to_select.find_element(By.XPATH, '//option[@value="20"]')
age_option.click()


browser.find_element(By.XPATH, "//button[contains(., '검 색')]").click()

with open('bill.csv', 'w') as bill_csv:
    csv_writer = csv.writer(bill_csv, delimiter=',', quotechar=',')
    for page in range(2, 2517):
        table = browser.find_element(By.CSS_SELECTOR, '.tableCol01 > table')
        rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            title = columns[1].find_element(By.TAG_NAME, 'a').get_attribute('title')
            s = columns[2].text
            date1 = columns[3].text
            date2 = columns[4].text
            result = columns[5].text
            csv_writer.writerow([title, s, date1, date2, result])
        browser.execute_script(f'GoPage({page});')


