from selenium import webdriver
driver = webdriver.Chrome('C:/Users/yws72/Desktop/chromedriver.exe')

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://store.musinsa.com/app/items/lists/001001')
bsObject = BeautifulSoup(html, "html.parser")
bs1 = bsObject.find('ul', {'id':'searchList'})

best_page_urls = []
for cover in bs1.find_all('div', {'class':'list_img'}):
    link = cover.select('a')[0].get('href')
    best_page_urls.append(link)

print(best_page_urls)

for url in best_page_urls:
    driver.get("https://store.musinsa.com" + url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    pd_name = soup.find('div', {'class':'explan_product product_info_section'}).find_all('p', {'class':'product_article_contents'})[0].get_text()
    pd_ss = soup.find('div', {'class':'explan_product product_info_section'}).find_all('p', {'class': 'product_article_contents'})[1].get_text()
    pd_view = soup.find('div', {'class': 'explan_product product_info_section'}).find_all('p', {'class': 'product_article_contents'})[2].get_text()
    print(pd_name, pd_ss, pd_view)