import requests
from bs4 import BeautifulSoup
import re

url = 'http://tureng.com/en/turkish-english/house'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find_all('table', {'class':'table table-hover table-striped searchResultsTable'})
data = re.findall(r'^.*[^<td class="rc4 hidden-xs">]', str(data).replace('\n', ' '))

data = re.findall('<td class="tr ts" lang="tr">(.*?)</td>', str(data))

for i in data:
    print(re.findall('>(.*?)<', i)[0])

























##data = soup.find_all('table', {'class':'chart full-width', 'data-caller-name':'chart-top250movie'})
##film_tablosu = (data[0].contents)[5].find_all('tr')
##titles = [film.find_all('td', {'class':'titleColumn'})[0].text.replace('\n', '').replace(' ', '', 11) for film in film_tablosu]
##print(titles)

