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













# driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div/div/div[1]/div[1]/a').click()
# driver.find_elements(By.TAG_NAME('Nachiket Patel')).click()
# if driver.find_element_by_xpath('//*[@id="ember208"]/div[2]') == True:
    # driver.find_element_by_xpath.('')
# //*[@id="ember143"]/div[2]
# //*[@id="ember143"]/div[2]
# https://www.linkedin.com/in/nachiket-patel-031770193/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BVIVqHPc6QUqrQEzLvJRY1A%3D%3D
# //*[@id="ember1531"]
# //*[@id="ember143"]/div[2]
# //*[@id="ember677"]

# //*[@id="ember111"]
# //*[@id="ember1531"]
# //*[@id="ember143"]
# //*[@id="ember143"]
# driver.find_element_by_xpath('//*[@id="ember40"]').click()
# driver.find_element_by_xpath('//*[@id="ember43"]').click()
# print(driver.find_element_by_xpath("//p[@class='block ember-view']/a").get_attribute('href'))
# # //*[@id="ember143"]
# <a href="/in/nachiket-patel-031770193/" id="ember143" class="block ember-view">    <div data-control-name="identity_profile_photo">
#       <img width="64" src="https://media-exp1.licdn.com/dms/image/C4D35AQEOh73Hg0cR3w/profile-framedphoto-shrink_100_100/0/1614869171125?e=1620237600&amp;v=beta&amp;t=xSx3AXnZKTeSM-8dC9now8Tdtuql5gatlZNzOiMRRcw" loading="lazy" height="64" alt="Photo of Nachiket Patel" id="ember144" class="feed-identity-module__member-photo profile-rail-card__member-photo EntityPhoto-circle-5 lazy-image ember-view">
#     </div>
#     <div class="profile-rail-card__actor-link t-16 t-black t-bold" data-control-name="identity_welcome_message">
#         Nachiket Patel
#     </div>
# </a>
# https://www.linkedin.com/in/nachiket-patel-031770193/