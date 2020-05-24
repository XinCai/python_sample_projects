import requests
from bs4 import BeautifulSoup

x = requests.get('https://www.abs.gov.au/')
#print(x)
soup = BeautifulSoup(x.content, 'html.parser')

#population
population = soup.select('#KeyIndicators > a:nth-child(2)')

#austrlian population live number
print('population: ' + population[0].contents[4])

#unemployment rate
unemployment = soup.select('#KeyIndicators > a:nth-child(6)')
print('unemployment rate: ' + unemployment[0].contents[4])

#Average Weekly Earnings
weeklyEarnings = soup.select('#KeyIndicators > a:nth-child(5)')
print('average weekly earnings: ' + weeklyEarnings[0].contents[4])

#consumer price index (CPI)
consumerPriceIndex = soup.select('#KeyIndicators > a:nth-child(3)')
print('CPI: ' +soup.select('#KeyIndicators > a:nth-child(3) > span:nth-child(3)')[0].contents[0]+ consumerPriceIndex[0].contents[4])

#gross domestic product
grossDomesticProduct = soup.select('#KeyIndicators > a:nth-child(4)')
print('GDP: '+ soup.select('#KeyIndicators > a:nth-child(4) > span:nth-child(3)')[0].contents[0] + grossDomesticProduct[0].contents[4])


