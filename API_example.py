import requests
from utilities.resources import ApiResources
from utilities.configurations import get_config, get_user, get_password
# from utilities.Payloads import build_add_book_payload_from_db  # for Add Book from database
from utilities.Payloads import add_book_payload
import urllib3

# # Add Book. We have taken the book from database:
# url_add_book = get_config()['API']['endpoint'] + ApiResources.addBook
# headers_add_book = {"Content-Type": "application/json"}
# query = 'select * from Books'
# response_add_book = requests.post(url_add_book, json=build_add_book_payload_from_db(query), headers=headers_add_book)
# add_book_response_json = response_add_book.json()
# print(add_book_response_json)
# assert response_add_book.status_code == 200
# assert add_book_response_json["Msg"] == "successfully added"

# Add Book with our own parameters:
url_add_book = get_config()['API']['endpoint'] + ApiResources.addBook
headers_add_book = {"Content-Type": "application/json"}
query = 'select * from Books'
response_add_book = requests.post(url_add_book, json=add_book_payload(), headers=headers_add_book)
add_book_response_json = response_add_book.json()
print(add_book_response_json)
assert response_add_book.status_code == 200
assert add_book_response_json["Msg"] == "successfully added"

# Delete Book:
url_delete_book = get_config()['API']['endpoint'] + ApiResources.deleteBook
bookId = add_book_response_json['ID']
body_delete_book = {"ID": bookId}
headers_delete_book = {"Content-Type": "application/json"}
response_deleteBook = requests.post(url_delete_book, json=body_delete_book, headers=headers_delete_book)
response_deleteBook_json = response_deleteBook.json()
print(response_deleteBook_json)
assert response_deleteBook.status_code == 200
assert response_deleteBook_json["msg"] == "book is successfully deleted"


# Authentication:
urllib3.disable_warnings() #убираю сообщение что мой https запрос не безопасен. Не лучший путь, лучше получить сертификат

# Можно и так
url1 = "https://api.github.com/user"
github_response1 = requests.get(url1, auth=(get_user(), get_password()))
assert github_response1.status_code == 200, f'Status code = {github_response1.status_code}'
# Но лучше так - открывать сессию и не надо в каждом запросе аутентификацию прописывать
se = requests.session()
se.auth = (get_user(), get_password())
url2 = "https://api.github.com/user/repos"
github_response2 = se.get(url2)
assert github_response2.status_code == 200, f'Status code = {github_response2.status_code}'


# НА httpbin.org МОЖНО ТРЕНИРОВАТЬСЯ ОТПРАВЛЯТЬ ВСЯКИЕ ЗАПРОСЫ !!!
# Как работать с cookies
# Если эндпоинт ожидает куки вида {'visit-month': 'month_of_year'}
cookie = {'visit-month': 'July'}
response3 = requests.get('http://rahulshettyacademy.com', cookies=cookie)
assert response3.status_code == 200, f'Status code = {response3.status_code}'
# Но лучше так - открывать сессию
se = requests.session()
se.cookies.update({'visit-month': 'July'})
response4 = se.get('http://rahulshettyacademy.com', allow_redirects=True, timeout=1)
print(response4.history)  # покажет промежуточный код, здесь 301 т.к. был rederection
assert response4.status_code == 200, f'Status code = {response4.status_code}'


# How to send attachment (file) to the endpoint
se = requests.session()
url5 = 'https://petstore.swagger.io/v2/pet/98432/uploadImage'
file = {'file': open('D:\\regexp.png', 'rb')}
response5 = se.post(url5, files=file)
print(response5.text)
assert response5.status_code == 200, f'Status code = {response5.status_code}'
