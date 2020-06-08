from selenium import webdriver
from bs4 import BeautifulSoup
import numpy


driver = webdriver.Chrome('/Users/heesu.lee/Downloads/chromedriver')
driver.implicitly_wait(3)

prices = []

for page in range(1, 11):
    driver.get('https://editmon.com/work/resume_list.html?page=' + str(page))

    req = driver.page_source

    soup = BeautifulSoup(req, 'html.parser')
    divs = soup.findAll('div', {'class': 'sub_resume_list_con2'})

    for div in divs:
        case = div.find(class_='icon_case')

        if case is not None:
            prices.append(int(str(div.text).strip().replace(',', '').replace('원', '')))

        minutes = div.find(class_='icon_minute')

        if minutes is not None:
            prices.append(int(str(div.text).strip().replace(',', '').replace('원', '')) * 10)

prices.sort(reverse=True)

print(len(prices))

for price in prices:
    print(price)

print(numpy.mean(prices))
