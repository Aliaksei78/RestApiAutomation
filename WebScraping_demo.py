import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.imdb.com/find?s=ep&q=triller&ref_=nv_sr_sm')
assert response.status_code == 200

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
movies_table = soup.find('table', {'class': 'findList'})
# print(movies_table.prettify())
rows = movies_table.findAll('tr')
thrillers = []
for row in rows:
    thriller_row = row.find('td', {'class': 'result_text'})
    # print(thriller_row.text)
    thrillers.append(thriller_row.text)
print('-------------------------')
print('Amount of thrillers: '+str(len(thrillers)))
thrillers.sort()
for data in thrillers:
    print(data)
print('-------------------------')

data = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
rest_api = soup.find('a', string='REST API')
print(rest_api['href'])
