import json

import requests
from bs4 import BeautifulSoup

x = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')

# https://requests.readthedocs.io/en/latest/api/
# r=requests.get("http://www.example.com/", headers={"content-type":"text"})


# url = 'SOME URL'
#
# headers = {
#     'User-Agent': 'My User Agent 1.0',
#     'From': 'youremail@domain.com'  # This is another valid field
# }
#
# response = requests.get(url, headers=headers)

#print(x)
soup = BeautifulSoup(x.content, 'html.parser')

#data by country
#table_body = soup.select('#covid19-container > #thetable > tbody')
#people = soup.select('#thetable > tbody > tr:nth-child(1) > td:nth-child(3)')

#austrlian population live number
#print(table_body)

table = soup.find('div', {"id": "covid19-container"})

#print(table)
rows = table.find_all('tr')

print(len(rows))

#table_body = table.find('tbody')
#rows = table_body.find_all('td')
data_by_country = {}
data = []
for row in rows:
   data.append(row.text)
   # if row.contents[3] is not None:
   #      data_by_country['location'] = row.contents[3].text
   # data_by_country['case'] = row.contents[5].text
   # data_by_country['deaths'] = row.contents[7].text
   # data_by_country['recover'] = row.contents[9].text

# print(data)
json_data = json.dumps(data, indent=4)
print(json_data)

