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

data = [];
table = soup.find('table', attrs={'class':'lineItemsTable'})

table_body = table.find('tbody')

rows = table_body.find_all('td')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

print(data)