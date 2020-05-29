import json
import requests
from bs4 import BeautifulSoup

x = requests.get('https://www.abs.gov.au/')

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

#dictionary
aus_data = {}

#population
population = soup.select('#KeyIndicators > a:nth-child(2)')

aus_data['population'] = population[0].contents[4]
#austrlian population live number
# print('population: ' + population[0].contents[4])

#unemployment rate
unemployment = soup.select('#KeyIndicators > a:nth-child(6)')
aus_data['unemployment_rate'] = unemployment[0].contents[4]

#Average Weekly Earnings
weeklyEarnings = soup.select('#KeyIndicators > a:nth-child(5)')
aus_data['weekly_earnings'] = weeklyEarnings[0].contents[4]

#consumer price index (CPI)
consumerPriceIndex = soup.select('#KeyIndicators > a:nth-child(3)')
aus_data['cpi'] = consumerPriceIndex[0].contents[4]
aus_data['cpi_date'] = soup.select('#KeyIndicators > a:nth-child(3) > span:nth-child(3)')[0].contents[0]

#gross domestic product
grossDomesticProduct = soup.select('#KeyIndicators > a:nth-child(4)')
aus_data['gdp'] = grossDomesticProduct[0].contents[4]
aus_data['gdp_date'] = soup.select('#KeyIndicators > a:nth-child(4) > span:nth-child(3)')[0].contents[0]

# print(aus_data)
json_data = json.dumps(aus_data, indent=4)
print(json_data)