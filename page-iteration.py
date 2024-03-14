from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

"""
페이지 구조를 알 수 있는 경우
https://yozm.wishket.com/magazine/list/develop/?page=3&sort=&q=
https://www.nesdc.go.kr/portal/bbs/B0000005/list.do?menuNo=200467

페이지 구조를 알 수 없어 DOM 요소로 Iteration 해야하는 경우
https://likms.assembly.go.kr/bill/BillSearchSimple.do
https://www.bigkinds.or.kr/v2/news/search.do;Bigkinds=3E4DB94BEB9E4D39625A7790957669EE
"""


# 더 쉬운 접근법 (1) - Javascript로 직접 호출하기
def paging2():
    page = 1
    browser.get('https://likms.assembly.go.kr/bill/BillSearchSimple.do')
    search = browser.find_element(By.XPATH, "//button[contains(., '검 색')]")
    search.click()
    while page < 10:
        browser.execute_script(f'GoPage({page});')
        page += 1
        time.sleep(2)



# 더 쉬운 접근법 (2) - 해당 사이트의 페이지네이션 URL 호출 구조를 이미 알고 있는 경우
def paging3():
    page = 1
    browser.get(
        f"https://www.nesdc.go.kr/portal/bbs/B0000005/list.do?menuNo=200467&searchTime=&sdate=&edate=&pdate=&pollGubuncd=&searchCnd=&searchWrd=&pageIndex={page}")
    while page < 10000:
        browser.get(f"https://www.nesdc.go.kr/portal/bbs/B0000005/list.do?menuNo=200467&searchTime=&sdate=&edate=&pdate=&pollGubuncd=&searchCnd=&searchWrd=&pageIndex={page}")
        page += 1


# paging2()
# paging3()