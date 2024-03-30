from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

browser = webdriver.Chrome()

browser.get('https://www.bigkinds.or.kr/v2/news/index.do')

time.sleep(1)
# 1. 날짜 선택
browser.find_element(By.CLASS_NAME, 'tab1').click()
from_date = '2023-03-12'
to_date = '2023-04-12'
for i in range(10):
    browser.find_element(By.ID, 'search-begin-date').send_keys(Keys.BACK_SPACE)
browser.find_element(By.ID, 'search-begin-date').send_keys(from_date)
browser.find_element(By.ID, 'search-begin-date').send_keys(Keys.ENTER)
for i in range(10):
    browser.find_element(By.ID, 'search-end-date').send_keys(Keys.BACK_SPACE)
browser.find_element(By.ID, 'search-end-date').send_keys(to_date)
browser.find_element(By.ID, 'search-end-date').send_keys(Keys.ENTER)

# 2. 언론사 선택
# browser.find_element(By.CLASS_NAME, 'tab2').click()

# 3. 검색 버튼 클릭
browser.find_element(By.CLASS_NAME, 'news-report-search-btn').click()

# 4. 로딩 대기
wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'resulteRe-btn')))

result = []

time.sleep(2)
with open('big-kinds-search-result.csv', mode='w') as news_csv:
    csv_writer = csv.writer(news_csv, delimiter=',', quotechar=',')

    for page in range(0, 1):
        newsResult = browser.find_elements(By.CLASS_NAME, 'news-inner')
        for news in newsResult:
            newsTitle = news.find_element(By.CLASS_NAME, 'title-elipsis')
            newsDate = news.find_element(By.CSS_SELECTOR, '.info > p.name:nth-child(2)').text
            newsPress = news.find_element(By.CSS_SELECTOR, '.info .provider').text
            newsReporter = news.find_element(By.CSS_SELECTOR, '.info > p.name:nth-child(3)').text
            newsTitle.click()
            newsArticle = browser.find_element(By.CLASS_NAME, 'news-view-body').text
            browser.find_element(By.CSS_SELECTOR, '.modal-footer > .btn').click()
            csv_writer.writerow([newsTitle.text, newsDate, newsPress, newsReporter, newsArticle])

        # page_input.send_keys(Keys.BACK_SPACE)
        # page_input.send_keys(Keys.BACK_SPACE)
        # page_input.send_keys(Keys.BACK_SPACE)
        # page_input.send_keys(Keys.BACK_SPACE)
        # page_input.send_keys(f'{page}')
        # page_input.send_keys(Keys.ENTER)
        time.sleep(5)


print(result)
