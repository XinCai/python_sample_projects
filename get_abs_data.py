import json
import requests
from bs4 import BeautifulSoup

# x = requests.get('https://www.abs.gov.au/')
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
# soup = BeautifulSoup(x.content, 'html.parser')

#dictionary
# aus_data = {}

# #population
# population = soup.select('#KeyIndicators > a:nth-child(2)')
#
# aus_data['population'] = population[0].contents[4]
# #austrlian population live number
# # print('population: ' + population[0].contents[4])
#
# #unemployment rate
# unemployment = soup.select('#KeyIndicators > a:nth-child(6)')
# aus_data['unemployment_rate'] = unemployment[0].contents[4]
#
# #Average Weekly Earnings
# weeklyEarnings = soup.select('#KeyIndicators > a:nth-child(5)')
# aus_data['weekly_earnings'] = weeklyEarnings[0].contents[4]
#
# #consumer price index (CPI)
# consumerPriceIndex = soup.select('#KeyIndicators > a:nth-child(3)')
# aus_data['cpi'] = consumerPriceIndex[0].contents[4]
# aus_data['cpi_date'] = soup.select('#KeyIndicators > a:nth-child(3) > span:nth-child(3)')[0].contents[0]
#
# #gross domestic product
# grossDomesticProduct = soup.select('#KeyIndicators > a:nth-child(4)')
# aus_data['gdp'] = grossDomesticProduct[0].contents[4]
# aus_data['gdp_date'] = soup.select('#KeyIndicators > a:nth-child(4) > span:nth-child(3)')[0].contents[0]
#
# # print(aus_data)
# json_data = json.dumps(aus_data, indent=4)
# print(json_data)

class ABSData:

    cpi = ""
    gdp = ""
    population = ""
    unemployment = ""
    weekly_earnings = ""
    soup = BeautifulSoup
    aus_data = {}

    def __init__(self,url):
        self.url = url
        res = requests.get(url)
        self.soup = BeautifulSoup(res.content, 'html.parser')
        cpi = self.soup.select('#KeyIndicators > a:nth-child(3)')
        self.aus_data['cpi'] = cpi[0].contents[4]
        self.cpi = self.aus_data['cpi']
        population = self.soup.select('#KeyIndicators > a:nth-child(2)')
        self.aus_data['population'] = population[0].contents[4]
        self.population = self.aus_data['population']
        gdp = self.soup.select('#KeyIndicators > a:nth-child(4)')
        self.aus_data['gdp'] = gdp[0].contents[4]
        self.gdp = self.aus_data['gdp']
        weekly_earnings = self.soup.select('#KeyIndicators > a:nth-child(5)')
        self.aus_data['weekly_earnings'] = weekly_earnings[0].contents[4]
        self.weekly_earnings = self.aus_data['weekly_earnings']
        self.unemployment = self.soup.select('#KeyIndicators > a:nth-child(6)')
        self.aus_data['unemployment_rate'] = self.unemployment[0].contents[4]
        self.unemployment = self.aus_data['unemployment_rate']

    def show_cpi(self):
        print(self.cpi)

    def show_population(self):
        print(self.population)

    def show_gdp(self):
        print(self.gdp)

    def show_earnings(self):
        print(self.weekly_earnings)

    def show_unemployment(self):
        print(self.unemployment)

    def get_data(self):
        return json.dumps(self.aus_data, indent=4)

obj = ABSData('https://www.abs.gov.au/')
obj.show_cpi()
# obj.show_population()
# obj.show_unemployment()
print(obj.get_data())