from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse
import csv


chrome = webdriver.Chrome()

browser = webdriver.Chrome()

keyword = input('검색 키워드:')
encoded = urllib.parse.quote_plus(keyword)
browser.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EC%9D%98&qdt=0&ie=utf8&query={encoded}')


fields_name = ['제목', 'URL', '언론사']
news_result = []

with open('news_result.csv', 'w') as news_csv:
    csv_writer = csv.writer(news_csv, delimiter=',', quotechar=',')
    for i in range(10):
        list_news = browser.find_elements(By.CLASS_NAME, 'list_news')[i * 10: i * 10 + 10]
        # 10개씩 더 가져온다.
        for news in list_news:
            news_title = news.find_element(By.CLASS_NAME, 'news_tit').get_attribute('title')
            news_url = news.find_element(By.CLASS_NAME, 'news_tit').get_attribute('href')
            press = news.find_element(By.CLASS_NAME, '').get_attribute('')
            csv_writer.writerow([news_title, news_url, press])

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(4)

