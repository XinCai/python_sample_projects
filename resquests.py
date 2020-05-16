import requests

#x = requests.get('https://w3schools.com/python/demopage.htm')
x = requests.get('https://www.abs.gov.au/')
print(x.text)
