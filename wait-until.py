from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://www.bigkinds.or.kr/v2/news/search.do;Bigkinds=3E4DB94BEB9E4D39625A7790957669EE')

wait = WebDriverWait(browser, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'resulteRe-btn')))
print('페이지 로딩 완료')

