from selenium import webdriver
import time
import urllib.parse


chrome = webdriver.Chrome()

browser = webdriver.Chrome()

keyword = input('검색 키워드:')
encoded = urllib.parse.quote_plus(keyword)
browser.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EC%9D%98&qdt=0&ie=utf8&query={encoded}')

for i in range(10):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(4)
