from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse
import csv


browser = webdriver.Chrome()

keyword = input('검색 키워드:')
encoded = urllib.parse.quote_plus(keyword)
browser.get(f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={encoded}')


fields_name = ['제목', 'URL', '언론사']
news_result = []

with open('news_result.csv', 'w') as news_csv:
    csv_writer = csv.writer(news_csv, delimiter=',', quotechar=',')
    for i in range(10):
        list_news = browser.find_element(By.CLASS_NAME, 'list_news').find_elements(By.CLASS_NAME, 'bx')[i * 10: i * 10 + 10]
        # 10개씩 더 가져온다.
        for news in list_news:
            news_title = news.find_element(By.CLASS_NAME, 'news_tit').get_attribute('title')
            information = news.find_elements(By.CLASS_NAME, 'info')
            if len(information) == 3:
                news_url = information[2].get_attribute('href')
            else:
                news_url = None
            press = news.find_element(By.CLASS_NAME, 'press').text
            original_window = browser.current_window_handle
            time.sleep(0.1)
            if type(news_url) == str:
                browser.switch_to.new_window('tab')
                browser.get(news_url)
                article = browser.find_element(By.ID, 'dic_area').text
                csv_writer.writerow([news_title, news_url, press, article])
                browser.close()
                browser.switch_to.window(original_window)

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(4)

