from selenium import webdriver
driver = webdriver.Chrome('C:/Users/yws72/Desktop/chromedriver.exe')

from bs4 import BeautifulSoup

page_url = []
for page in range(4,5):
    driver.get('https://store.musinsa.com/app/items/lists/001001/?category=&d_cat_cd=001001&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90&page=' + str(page))
    html = driver.page_source
    bsObject = BeautifulSoup(html, "html.parser")
    bs1 = bsObject.find('ul', {'id':'searchList'})
    bs2 = bs1.find_all('div', {'class':'list_img'})
    for cover in bs2:
        link = cover.select('a')[0].get('href')
        page_url.append(link)

target = open('test.csv', mode='w', encoding='ansi')
header = 'brand,ss,view,qty,like,satisfaction,purchase,delivery,delivery_day,goods_price,list_price,point,touch,flex,trans,thick,season,color,ingredient,guarantee,totalview,view_age18,view_age24,' \
         'view_age34,view_age44,view_age45,view_male,view_female,view_unknown,qa,rvcount,rvstyle,rvphoto,rvgoods\n'

