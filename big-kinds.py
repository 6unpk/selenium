from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome = webdriver.Chrome()

browser = webdriver.Chrome()

browser.get('https://www.bigkinds.or.kr/v2/news/search.do;Bigkinds=3E4DB94BEB9E4D39625A7790957669EE')

wait = WebDriverWait(browser, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'resulteRe-btn')))


result = []

for page in range(1, 2000):
    page_input = browser.find_element(By.ID, 'paging_news_result')
    newsResult = browser.find_element(By.ID, 'news-results')
    newsTitle = newsResult.find_elements(By.CLASS_NAME, 'title-elipsis')

    for title in newsTitle:
        result.append(title.text)

    page_input.send_keys(Keys.BACK_SPACE)
    page_input.send_keys(f'{page}')
    page_input.send_keys(Keys.ENTER)
    time.sleep(5)


print(result)
