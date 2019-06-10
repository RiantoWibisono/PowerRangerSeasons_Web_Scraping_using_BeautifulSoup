# scraping html from website
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

m = y.find('table', class_='wikitable')

for i in m.find_all('tr'):
    if i.find('i') == None:
        continue
    else:
        if i.find('span', class_='bday dtstart published updated') == None:
            n = i.find_all('td')[4]
            if n.text.find('\n'):
                n.text.replace('\n', '')
        else:
            n = i.find('span', class_='bday dtstart published updated')
        if i.find('span', class_='dtend') == None:
            if len(i.find_all('td')) == 5:
                o = i.find_all('td')[4]
            elif len(i.find_all('td')) == 6:
                o = i.find_all('td')[5]
            if o.text.find('[3]') or o.text.find('\n'):
                o.text.replace('[3]', '').replace('\n','')
        else:
            o = i.find('span', class_='dtend')
        p = i.find('i')
        print('Season =', p.text, '\n First Aired =', n.text.replace('\n',''), '\n Last Aired =', o.text.replace('[3]','').replace('\n',''))

print()