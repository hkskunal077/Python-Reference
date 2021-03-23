import bs4 as bs
import urllib.request
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()


soup = bs.BeautifulSoup(source, 'lxml')
""" print(soup)
print(source) """

""" print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)

print(soup.find_all('p')) """

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.xt))   

#Grabbing Links
#for url in soup.find_all('a'):
    #print(url.get('href'))

#Grabbing Text
#print(soup.get_text())

nav = soup.nav
print(nav)

for url in nav.find_all('a'):
    print(url.get('href'))


body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)


for div in soup.find_all('div', class_='body'):
    print(div.text)


table = soup.table
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

