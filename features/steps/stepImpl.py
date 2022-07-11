import requests
from behave import *
from utilities.resources import ApiResources
from utilities.configurations import get_config, get_user, get_password
# from utilities.Payloads import build_add_book_payload_from_db  # for Add Book from database
from utilities.Payloads import add_book_payload


# # for Add Book from database
# @given('the Book details which need to be added to Library')
# def step_impl(context):
#     context.url_add_book = get_config()['API']['endpoint'] + ApiResources.addBook
#     context.headers_add_book = {"Content-Type": "application/json"}
#     context.query = 'select * from Books'

# # for Add Book from database
# @when('execute the AddBook Post API method')
# def step_impl(context):
#     context.response_add_book = requests.post(context.url_add_book, json=build_add_book_payload_from_db(context.query),
#                                               headers=context.headers_add_book)


# for Add Book with our own parameters:
@given('the Book details which need to be added to Library')
def step_impl(context):
    context.url_add_book = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers_add_book = {"Content-Type": "application/json"}
    context.payload = add_book_payload('HoHoHo', 55555)


# for Add Book with our own different parameters = parametrization:
@given('the Book details which need to be added to Library with different {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url_add_book = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers_add_book = {"Content-Type": "application/json"}
    context.payload = add_book_payload(isbn, aisle)


# for Add Book with our own parameters:
@when('execute the AddBook Post API method')
def step_impl(context):
    context.response = requests.post(context.url_add_book, json=context.payload,
                                     headers=context.headers_add_book)


@then('the Book is added successfully')
def step_impl(context):
    context.add_book_response_json = context.response.json()
    print(context.add_book_response_json)
    assert context.response.status_code == 200
    assert context.add_book_response_json["Msg"] == "successfully added"


@given('I have GitHub auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = (get_user(), get_password())
    context.url2 = ApiResources.githubRepo


@when('I hit /user/repos API of GitHub (https://api.github.com/user/repos)')
def step_impl(context):
    context.response = context.se.get(context.url2)


@then('Status code of response should be {tested_status_code:d}')
def step_impl(context, tested_status_code):
    assert context.response.status_code == tested_status_code, f'Status code = {context.response.status_code}'
