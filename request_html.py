from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://www.abs.gov.au/')
#r = session.get('https://www.abs.gov.au/AUSSTATS/abs@.nsf/Web+Pages/Population+Clock?opendocument&ref=HPKI')

#print(r.html.html)
#print(r.html.links)
#print(r.html.absolute_links)
#print(r.html.xpath("//*[@id="KeyIndicators"]/a[1]/text()"))
#print(r.html.find('div#KeyIndicators  a:nth-child(2)  span:nth-child(2)'))
print(r.html.find('div#KeyIndicators > a:nth-child(2)')[0])
# print(help(r))
#print(r.html.find('div#middle tbody  tr  td  ul:nth-child(2)  div'))
#middle > tbody > tr > td > ul:nth-child(2) > div > b > font
##KeyIndicators > a:nth-child(2)
#print(list(map(lambda x: x.text, r.html.find('div.content span'))))
