# from utilities.configurations import get_query  # for Add Book from database

# for Add Book with our own parameters:
def add_book_payload(isbn, aisle):
    body = dict(name="Learn Appium Automation with Java", isbn=isbn, aisle=aisle, author="John foe")
    return body


# # for Add Book from database
# def build_add_book_payload_from_db(query):
#     add_body = {}
#     tp = get_query(query)
#     print(tp)
#     add_body['name'] = tp[0]
#     add_body['isbn'] = tp[1]
#     add_body['aisle'] = tp[2]
#     add_body['author'] = tp[3]
#     return add_body
