import requests
from bs4 import BeautifulSoup
import re
import csv
#  create a csv file and write
f_name  = 'scrap.csv'
csv_write = csv.writer(open(f_name,'w'))

#  use request for scraping the first page of  web data 
url ='https://www.marketsandmarkets.com/telecom-and-IT-market-research-113.html'
html_code = requests.get(url).text

sp =BeautifulSoup(html_code,'lxml')
for tr in sp.findAll('tr'):
        data =[]
        for i in tr.findAll('a'):
            link ='https://www.marketsandmarkets.com'+i['href']
            data.append(link)
        for i  in tr.findAll('p'):
            data.append(i.text)
            per=re.findall('[0-9]+\.[0-9]+%',i.text)
            us=i.text.find('to USD')
            us1 = i.text.find('billion by')
            data.append(i.text[us+7:us1+7])
            data.append("".join(per))
            csv_write.writerow(data)
        print(data)

for i in range(1,20):
#  use request for scraping the  web data  second page onwords.
    url ='https://www.marketsandmarkets.com/telecom-and-IT-market-research-113_'+str(i)+'.html'
    html_code = requests.get(url).text
    sp =BeautifulSoup(html_code,'lxml')
    for tr in sp.findAll('tr'):
            data =[]
            for i in tr.findAll('a'):
                link ='https://www.marketsandmarkets.com'+i['href']
                data.append(link)
            for i  in tr.findAll('p'):
                data.append(i.text)
                per=re.findall('[0-9]+\.[0-9]+%',i.text)
                us=i.text.find('to USD')
                us1 = i.text.find('billion by')
                data.append(i.text[us+7:us1+7])
                data.append("".join(per))
                csv_write.writerow(data)
            print(data)




