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

with open('news_result.csv', 'w', encoding='utf-8') as news_csv:
    csv_writer = csv.writer(news_csv, delimiter=',', quotechar=',')

    for i in range(1):
        list_news = browser.find_element(By.CLASS_NAME, 'list_news').find_elements(By.CLASS_NAME, 'bx')[i * 10: i * 10 + 2]
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
            # 네이버 뉴스 기사 페이지로 창을 이동하는 부분
            if type(news_url) == str:
                browser.switch_to.new_window('tab') # 새로운 브라우저 탭을 생성
                browser.get(news_url) # 네이버 뉴스 기사로 이동
                article = browser.find_element(By.ID, 'dic_area').text
                try:
                    comment_button = browser.find_element(By.CLASS_NAME, 'media_end_head_cmtcount_button')
                    comment_count = comment_button.text
                    comment_button.click()
                except:
                    pass


                time.sleep(1)
                try:
                    while True:
                        browser.find_element(By.CLASS_NAME, 'u_cbox_more_wrap').click()
                        time.sleep(0.5)
                except:
                    pass

                chats = browser.find_elements(By.CLASS_NAME, 'u_cbox_contents')

                news_chat = []
                for chat in chats:
                    news_chat.append(chat.text)

                csv_writer.writerow([news_title, news_url, press, article, str(news_chat)])
                browser.close()
                browser.switch_to.window(original_window)

        # 스크롤을 내리는 명령
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(4)

